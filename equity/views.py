from django.http import HttpResponse, Http404, JsonResponse
from django.template import RequestContext, Context
from django.shortcuts import render_to_response
from django.conf import settings
from equity.models import Account, ClassificationNames, AllocationNodes
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser, FormParser
from equity.serializers import AccountSerializer, ClassificationNamesSerializer
from rest_framework.decorators import parser_classes
from equity.models import AllocationModels, AccountFilters, SecuritySelectionModels
from django.core import serializers
from django.shortcuts import render
from django.contrib import messages
from forms import ModelNameForm, AccountParametersForm, AccountFilterForm, AccountSelectionForm, \
    SecuritySelectionModelForm


class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """

    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


# Create your views here.
def custom_proc(request):
    "A context processor that provides 'app', 'user' and 'ip_address'."
    return {
        'app': 'My app',
        'user': request.user,
        'ip_address': request.META['REMOTE_ADDR'],
    }


def home(request):
    return render_to_response("index.html", {'STATIC_URL': settings.STATIC_URL})


def newRebalance(request):  # 1st Page for New Rebalance => NewRebalance2

    if request.method == "POST":
        form = AccountParametersForm(request.POST)
        if form.is_valid():
            rebalanceName = form.cleaned_data['rebalanceName']
            saleType = form.cleaned_data['saleType']
            buySell = form.cleaned_data['buySell']
            reviewCurrentSale = form.cleaned_data['reviewCurrentSale']
            adjustCashAfterRebal = form.cleaned_data['adjustCashAfterRebal']
            adjustWgtAfterRebal = form.cleaned_data['adjustWgtAfterRebal']
            taxLots = form.cleaned_data['taxLots']
            form.save()

            return render(request, 'NewRebalance_2.html', {'account_selection_form': AccountSelectionForm()})
    else:
        form = AccountParametersForm()
    return render(request, 'NewRebalance.html', {'account_parameters_form': form})


def accountSelections(request):  # NewRebalnce 2: AccountParameters with Accounts and Trading Form

    if request.method == "POST":
        form = AccountSelectionForm(request.POST)

        if form.is_valid():
            acctFilterName = form.data['acctFilterName']
            excludeClassification = form.data['excludeClassification']
            tradingCash = form.data['tradingCash']
            form.save()

            return render(request, 'NewRebalance_3.html')
    else:
        form = AccountSelectionForm()
    return render(request, 'NewRebalance2.html', {'account_selections_form': form})


def accounts(request):
    c = RequestContext(request, '', processors=[custom_proc])
    return render(request, 'accounts.html', context=c)


def accountsByFilter(request):
    if request.is_ajax():
        id = request.GET.get('id')
        acctFilter = AccountFilters.objects.get(acctFilterName=id)
        accounts = acctFilter.accountName.all()

        acctSerializer = AccountSerializer(accounts, many=True)

        # serializers.serialize('json', accounts)

    return JSONResponse(acctSerializer.data, status=201)


def referenceData(request):
    c = RequestContext(request, '', processors=[custom_proc])
    return render(request, 'referenceData.html', context=c)


def securities(request):
    pass


def rulesCreation(request):
    pass


def accountParameters(request):
    pass


def modelParameters(request):
    pass


def accountSearchFilter(request):
    # Saving and doing account Parameters
    if request.method == "POST" or request.is_ajax():

        form = AccountFilterForm(request.POST)

        if form.is_valid():
            acctFilterName = form.cleaned_data['acctFilterName']
            accountName = form.cleaned_data['accountName']

            o = form.save(commit=False)
            o.save()
            form.save_m2m()
            return render(request, 'index.html')  # TODO: Create a modal popup to say it saved
    else:
        form = AccountFilterForm()
    return render(request, 'AccountSearchFilter.html', {'account_filter_form': form})


@csrf_exempt
@parser_classes((JSONParser, FormParser,))
def save_account_list(request):
    """
    List all Accounts, or create a new account.
    """
    try:
        data = FormParser().parse(request)
        serializer = AccountSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JSONResponse(dict(Result='OK', Record=serializer.data), status=201)

        return JSONResponse(serializer.errors, status=400)

    except Exception:  # //TODO This may require more investigation. The original line of code here was to handle an issue on POST
        # where the account needed to do a post request to get the data from the database. I'm leaving it here temporarily until more testing

        accounts = Account.objects.all()
        serializer = AccountSerializer(accounts, many=True)
        return JSONResponse(dict(Result='OK', Records=serializer.data), status=201)


@csrf_exempt
def get_account_list(request):
    accounts = Account.objects.all()
    serializer = AccountSerializer(accounts, many=True)
    return JSONResponse(serializer.data, status=201)


# Returns a newModel page for an ask to create a new model
def Update_Models(request, modelID):
    try:
        allocationModel = AllocationModels.objects.get(pk=modelID)
        # serializer = AllocationModelsSerializer(allocationModel, many=True)

    except AllocationModels.DoesNotExist:
        raise Http404("Allocation Model does not exist")

    # return JSONResponse(serializer.data, status=201)
    return render('models', {'allocationModel': allocationModel})


def get_classifications(request):
    if request.is_ajax():
        if request.GET.get('id') is not None:
            id = request.GET['id']

            rootNode = ClassificationNames.objects.get(id=id)

            childNodes = rootNode.get_children()
            classNameSerializers = ClassificationNamesSerializer(childNodes, many=True)

        else:

            baseClassName = ClassificationNames.objects.get(classificationName='Classification')

            rootNode = baseClassName.get_root()

            classNameSerializers = ClassificationNamesSerializer(rootNode)

    return JsonResponse(classNameSerializers.data, safe=False)


def save_classifications(request):
    if request.is_ajax():
        dataSource = request.POST.get('dataSource')
        id = request.POST.get('ssmModel')
        ssmModel = SecuritySelectionModels.objects.get(pk=id)
        ssmModel.userCreatedModel = dataSource
        ssmModel.save()

    return render('index.html', status=200)


def Create_Model_Name(request):
    # if this is a POST request we need to process the form data
    errors_dict = {}
    if request.method == "POST":
        form = ModelNameForm(request.POST)
        if request.is_ajax():
            # TODO What do we do about primary key collision? How do we send a validation back?

            # check whether it's valid:
            if form.is_valid():
                # process the data in form.cleaned_data as required
                newModel = form.save(commit=False)
                newModel.created_by = request.user
                newModel.edited_by = request.user
                newModel.save()
                messages.success(request, 'New Model Created.')

                classificationName = ClassificationNames.objects.get(id=1)
                node = AllocationNodes(
                        allocationModel=newModel,
                        classificationName=classificationName,
                        level=1
                )

                node.save()
                allocNodes = AllocationNodes.objects.get(allocationModel=newModel.id)

                data = serializers.serialize('json', [allocNodes], indent=2, use_natural_foreign_keys=True,
                                             use_natural_primary_keys=True)

                return JSONResponse(data, status=201)
            else:
                if form.errors:
                    if form.errors:
                        for error in form.errors:
                            e = form.errors[error]
                            errors_dict[error] = e
                messages.error(request, e)
                return JSONResponse(errors_dict, status=404)
    else:
        form = ModelNameForm()
    return render(request, 'createNewModel.html', {'form': form})


def createSecuritySelectionModels(request):
    storage = messages.get_messages(request)
    if request.is_ajax():
        return JSONResponse(accounts, status=201)

    elif request.method == 'POST':
        form = SecuritySelectionModelForm(request.POST)
        if form.is_valid():
            id = form.save();
            messages.add_message(request, messages.SUCCESS, 'Successful Save.')
            c = {
                "id": id.id
            }
            return render_to_response('createNewModelWithSecurity.html', c, context_instance=RequestContext(request))

        else:
            form = SecuritySelectionModelForm()
    else:
        form = SecuritySelectionModelForm()
    return render(request, 'createNewModel.html', {'security_selection_model_form': form})


def createSSMModels(request, clean_data):
    pass


class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """

    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)
