from django.http import HttpResponse, Http404, JsonResponsefrom django.template import RequestContextfrom django.shortcuts import render_to_responsefrom django.conf import settingsfrom equity.models import Account, ClassificationNames, AllocationNodes, UserSecuritySelectionModelfrom django.views.decorators.csrf import csrf_exemptfrom rest_framework.renderers import JSONRendererfrom rest_framework.parsers import JSONParser, FormParserfrom equity.serializers import AccountSerializer, \    ClassificationNamesSerializer, UserSecuritySelectionModelSerializers, SecuritySelectionModelSerializersfrom rest_framework.decorators import parser_classesfrom equity.models import AllocationModels, AccountFilters, SecuritySelectionModels, UserSecuritySelectionModelfrom django.core import serializersfrom django.shortcuts import renderfrom forms import ModelNameForm, AccountParametersForm, AccountFilterForm, AccountSelectionForm, \    SecuritySelectionModelFormfrom django.contrib import messagesfrom utils import JSONTree, UpdateJSONTreeimport jsonfrom equity.algorithims import SumOfNodesget = lambda node_id: UserSecuritySelectionModel.objects.get(pk=node_id)class JSONResponse(HttpResponse):    """    An HttpResponse that renders its content into JSON.    """    def __init__(self, data, **kwargs):        content = JSONRenderer().render(data)        kwargs['content_type'] = 'application/json'        super(JSONResponse, self).__init__(content, **kwargs)# Create your views here.def custom_proc(request):    "A context processor that provides 'app', 'user' and 'ip_address'."    return {        'app': 'My app',        'user': request.user,        'ip_address': request.META['REMOTE_ADDR'],    }def home(request):    return render(request, "home.html", {})def index(request):    return render(request, "index.html", {'STATIC_URL': settings.STATIC_URL})def newRebalance(request):  # 1st Page for New Rebalance => NewRebalance2    if request.method == "POST":        form = AccountParametersForm(request.POST)        if form.is_valid():            rebalanceName = form.cleaned_data['rebalanceName']            saleType = form.cleaned_data['saleType']            buySell = form.cleaned_data['buySell']            reviewCurrentSale = form.cleaned_data['reviewCurrentSale']            adjustCashAfterRebal = form.cleaned_data['adjustCashAfterRebal']            adjustWgtAfterRebal = form.cleaned_data['adjustWgtAfterRebal']            taxLots = form.cleaned_data['taxLots']            form.save()            return render(request, 'NewRebalance_2.html', {'account_selection_form': AccountSelectionForm()})    else:        form = AccountParametersForm()    return render(request, 'NewRebalance.html', {'account_parameters_form': form})def accountSelections(request):  # NewRebalnce 2: AccountParameters with Accounts and Trading Form    if request.method == "POST":        form = AccountSelectionForm(request.POST)        if form.is_valid():            acctFilterName = form.data['acctFilterName']            excludeClassification = form.data['excludeClassification']            tradingCash = form.data['tradingCash']            form.save()            return render(request, 'NewRebalance_3.html')    else:        form = AccountSelectionForm()    return render(request, 'NewRebalance2.html', {'account_selections_form': form})def accounts(request):    c = RequestContext(request, '', processors=[custom_proc])    return render(request, 'accounts.html', context=c)def accountsByFilter(request):    if request.is_ajax():        id = request.GET.get('id')        acctFilter = AccountFilters.objects.get(acctFilterName=id)        accounts = acctFilter.accountName.all()        acctSerializer = AccountSerializer(accounts, many=True)        # serializers.serialize('json', accounts)    return JSONResponse(acctSerializer.data, status=201)def referenceData(request):    c = RequestContext(request, '', processors=[custom_proc])    return render(request, 'referenceData.html', context=c)def securities(request):    passdef rulesCreation(request):    passdef accountParameters(request):    passdef modelParameters(request):    passdef accountSearchFilter(request):    # Saving and doing account Parameters    if request.method == "POST" or request.is_ajax():        form = AccountFilterForm(request.POST)        if form.is_valid():            acctFilterName = form.cleaned_data['acctFilterName']            accountName = form.cleaned_data['accountName']            o = form.save(commit=False)            o.save()            form.save_m2m()            return render(request, 'index.html')  # TODO: Create a modal popup to say it saved    else:        form = AccountFilterForm()    return render(request, 'AccountSearchFilter.html', {'account_filter_form': form})@csrf_exempt@parser_classes((JSONParser, FormParser,))def save_account_list(request):    """    List all Accounts, or create a new account.    """    try:        data = FormParser().parse(request)        serializer = AccountSerializer(data=data)        if serializer.is_valid():            serializer.save()            return JSONResponse(dict(Result='OK', Record=serializer.data), status=201)        return JSONResponse(serializer.errors, status=400)    except Exception:  # //TODO This may require more investigation. The original line of code here was to handle an issue on POST        # where the account needed to do a post request to get the data from the database. I'm leaving it here temporarily until more testing        accounts = Account.objects.all()        serializer = AccountSerializer(accounts, many=True)        return JSONResponse(dict(Result='OK', Records=serializer.data), status=201)@csrf_exemptdef get_account_list(request):    accounts = Account.objects.all()    serializer = AccountSerializer(accounts, many=True)    return JSONResponse(serializer.data, status=201)def getClassifications(request):    if request.is_ajax():        if request.GET.get('id') is not None:            id = request.GET['id']            rootNode = ClassificationNames.objects.get(id=id)            childNodes = rootNode.get_children()            classNameSerializers = ClassificationNamesSerializer(childNodes, many=True)        else:            baseClassName = ClassificationNames.objects.get(classificationName='Classification')            rootNode = baseClassName.get_root()            classNameSerializers = ClassificationNamesSerializer(rootNode)    return JsonResponse(classNameSerializers.data, safe=False)def getSavedClassificationModel(request, id):  # Comes from updateSecuritySelectionModels.html    if (len(request.GET) == 0):  # Get the Root Node TODO: Need to change the SSM to an actual name and not a SSM        userSecuritySelectionModels = UserSecuritySelectionModel.objects.get(ext_model_id=id)        rootNode = userSecuritySelectionModels.get_root()    elif request.is_ajax() and request.GET['ext_model_id'] is not None:        id = request.GET['ext_model_id']        userSecuritySelectionModels = UserSecuritySelectionModel.objects.get(ext_model_id=id)        childrenNodes = userSecuritySelectionModels.get_children()        SSMSerializer = UserSecuritySelectionModelSerializers(childrenNodes, many=True)        return JsonResponse(SSMSerializer.data, status=201, safe=False)    SSMSerializer = UserSecuritySelectionModelSerializers(rootNode)    return JsonResponse(SSMSerializer.data, status=201, safe=False)def saveClassifications(request):    if request.is_ajax():        dataSource = request.POST.get('dataSource')        id = request.POST.get('ssmModel')        ssmModel = SecuritySelectionModels.objects.get(pk=id)        ssmModel.userCreatedModel = dataSource        result = JSONTree.JSONtoTreeBeard(dataSource)        ssmModel.save()    return JSONResponse(id, status=201)def updateSecuritySelectionModels(request):  # First Call for Update Workflow #1    return render(request, "updateModel.html")def updateModelWithSecurity(request, id):  # Second Call for Update    ModelName = SecuritySelectionModels.objects.get(id=id)    return render(request, "updateModelWithSecurity.html",                  {'id': id, 'securitySelectionModelName': ModelName.securitySelectionModelName})def deleteModel(request):    return render(request, "deleteModel.html")def deleteSecuritySelectionModels(request, id):    SecuritySelectionModels.objects.get(pk=id).delete()    return JsonResponse({'success': 'success'})def updateModelNodes(request):    get = lambda node_id: UserSecuritySelectionModel.objects.get(pk=node_id)    try:        if request.is_ajax():            SSMModel = request.POST['ssmModel']            dataSource = json.loads(request.POST['dataSource'])            result = UpdateJSONTree.UpdateSSM(dataSource, SSMModel)    except AllocationModels.DoesNotExist:        raise Http404("Allocation Model does not exist")    return render(request, "createUpdateNewModelWeights.html",                  {'id': SSMModel, 'securitySelectionModelName': 'test'})  # TODO: Send the Model name back# Returns a newModel page for an ask to create a new modeldef updateModelWithTargetWeights(request):    get = lambda node_id: UserSecuritySelectionModel.objects.get(pk=node_id)    try:        if request.method == 'POST':            id = request.POST['models[0][id]']            ext_model_id = request.POST['models[0][ext_model_id]']            parent_id = request.POST['models[0][parentId]']            SSM_id = request.POST['models[0][SSM_id]']            tgt_weight = request.POST['models[0][tgtWeight]']            # Go to Rebalancer algorithim            updatedNodes = SumOfNodes.returnPercentOfNodeRoot(SSM_id, ext_model_id, tgt_weight)        userSelectionModelSerializer = UserSecuritySelectionModelSerializers(updatedNodes, many=True)    except AllocationModels.DoesNotExist:        raise Http404("Allocation Model does not exist")    json = JsonResponse(userSelectionModelSerializer.data, status=201, safe=False)    json['Model_Transaction_Type'] = 'Update'    return json    # return render('models', {'allocationModel': allocationModel})def get_SSMList(request):    if request.is_ajax():        SSMList = SecuritySelectionModels.objects.all();        serializer = SecuritySelectionModelSerializers(SSMList, many=True)    return JsonResponse(serializer.data, safe=False)def createModelWeights(request):    id = request.GET.get('id', '')    SSMModel = request.GET.get('SSMModel', None)    return render(request, "createUpdateNewModelWeights.html", {'id': id, 'securitySelectionModelName': SSMModel})def getModelTargetWeights(request):    #get = lambda node_id: UserSecuritySelectionModel.objects.get(pk=node_id)    SSM_id = request.GET.get('SSM_id', '')    id = request.GET.get('id', '')    if id == '':        rootNode = UserSecuritySelectionModel.objects.get(SSM_id=SSM_id, classificationName__isnull=True)    else:        rootNode = UserSecuritySelectionModel.objects.get(pk=id)    if request.is_ajax() and SSM_id is not None and id == "":        userSelectionModelSerializer = UserSecuritySelectionModelSerializers(rootNode)        if not rootNode.is_root():            node = rootNode.get_root()            data = serializers.serialize('json', node, use_natural_foreign_keys=True)            return JsonResponse(data, safe=False)        return JsonResponse(userSelectionModelSerializer.data, status=201, safe=False)    elif request.is_ajax() and id is not "" and SSM_id is not "":        childrenNodes = get(rootNode.pk).get_children()        userSelectionModelSerializer = UserSecuritySelectionModelSerializers(childrenNodes, many=True)        # if userSelectionModelSerializer.data is not None:        #     rootNode = flatten(userSelectionModelSerializer.data)    return JsonResponse(userSelectionModelSerializer.data, status=201, safe=False)  # ->> Add if we wnat to use this    #return JsonResponse (rootNode, status=201, safe=False)def Create_Model_Name(request):    # if this is a POST request we need to process the form data    errors_dict = {}    if request.method == "POST":        form = ModelNameForm(request.POST)        if request.is_ajax():            # TODO What do we do about primary key collision? How do we send a validation back?            # check whether it's valid:            if form.is_valid():                # process the data in form.cleaned_data as required                newModel = form.save(commit=False)                newModel.created_by = request.user                newModel.edited_by = request.user                newModel.save()                messages.success(request, 'New Model Created.')                classificationName = ClassificationNames.objects.get(id=1)                node = AllocationNodes(                        allocationModel=newModel,                        classificationName=classificationName,                        level=1                )                node.save()                allocNodes = AllocationNodes.objects.get(allocationModel=newModel.id)                data = serializers.serialize('json', [allocNodes], indent=2, use_natural_foreign_keys=True,                                             use_natural_primary_keys=True)                return JSONResponse(data, status=201)            else:                if form.errors:                    if form.errors:                        for error in form.errors:                            e = form.errors[error]                            errors_dict[error] = e                messages.error(request, e)                return JSONResponse(errors_dict, status=404)    else:        form = ModelNameForm()    return render(request, 'createNewModel.html', {'form': form})def createSecuritySelectionModels(request):    storage = messages.get_messages(request)    if request.is_ajax():        return JSONResponse(accounts, status=201)    elif request.method == 'POST':        form = SecuritySelectionModelForm(request.POST)        if form.is_valid():            ssm = form.save();            messages.add_message(request, messages.SUCCESS, 'Successful Save.')            c = {                "id": ssm.id,                "securitySelectionModelName": ssm.securitySelectionModelName            }            return render(request, 'createNewModelWithSecurity.html', c)        else:            return render(request, 'createNewModel.html', {'security_selection_model_form': form})    else:        form = SecuritySelectionModelForm()    return render(request, 'createNewModel.html', {'security_selection_model_form': form})def createSSMModels(request, clean_data):    passdef flatten(item):    myArray = {}    for i in item:        for k, v in i.items():            if k == "parent":                print k, v['id']                myArray[k] = v['id']            elif k == 'SSM':                myArray['securitySelectionModelName'] = v['securitySelectionModelName']            elif k == "classificationName":                myArray[k] = v['classificationName']            else:                myArray[k] = v    return myArray