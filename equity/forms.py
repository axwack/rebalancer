__author__ = 'vincentlee'

from crispy_forms.helper import FormHelper
from django import forms
from crispy_forms.layout import Submit, Layout, Button
from crispy_forms.bootstrap import Tab, TabHolder, FormActions
from equity.models import RebalanceParameters, AccountFilters, ClassificationNames, AccountParameters, \
    SecuritySelectionModels
from django.utils.translation import ugettext_lazy as _
from equity.models import Securities, Feeds


class ModelNameForm(forms.Form):
    modelName = forms.CharField(label='Model Name', max_length=100)


class AccountParametersForm(forms.ModelForm):
    class Meta:
        model = RebalanceParameters
        fields = ['rebalanceName', 'saleType', 'buySell', 'reviewCurrentSale', 'adjustCashAfterRebal',
                  'adjustWgtAfterRebal', 'taxLots']

    TAXLOT = (('FIFO', 'FIFO',), ('LIFO', 'LIFO',), ('AVGCOST', 'Average Cost',))

    rebalanceName = forms.CharField(
            widget=forms.TextInput,
            label="Rebalance Name",
            required=True,
    )

    saleType = forms.ChoiceField(
            label="Sale Type:",
            choices=(('New', "New"), ('Existing', "Existing")),
            widget=forms.RadioSelect,
            initial='New',
            required=True,
    )

    buySell = forms.ChoiceField(
            label="Type of Rebalance:",
            choices=(("B", "Buy"), ("S", "Sell")),
            widget=forms.RadioSelect,
            initial='B',
            required=True,
    )

    reviewCurrentSale = forms.BooleanField(
            label="Review a Current Sale:",
            widget=forms.CheckboxInput,
            required=False,
    )

    adjustCashAfterRebal = forms.BooleanField(
            label="Adjust Cash after Rebalance:",
            widget=forms.CheckboxInput,
            required=False,

    )

    adjustWgtAfterRebal = forms.BooleanField(
            label="Adjust Weight after Rebalance:",
            widget=forms.CheckboxInput,
            required=False,

    )

    taxLots = forms.ChoiceField(
            label="Adjust Weight after Rebalance:",
            choices=TAXLOT,
            widget=forms.Select,
            initial='0',

    )

    def __init__(self, *args, **kwargs):
        super(AccountParametersForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-group'
        self.helper.form_method = 'post'
        self.helper.form_action = 'newRebalanceRequest'

        self.helper.add_input(Submit('submit', 'Submit'))


class AccountFilterForm(forms.ModelForm):
    class Meta:
        model = AccountFilters
        fields = ['acctFilterName', 'accountName']
        labels = {
            'accountName': _('Accounts:'),
            'acctFilterName': _('Filter Name:')
        }


class AccountSelectionForm(forms.ModelForm):
    acctFilterName = forms.ModelChoiceField(queryset=AccountFilters.objects.all(),
                                            label="Account Filters:",
                                            empty_label="Select Here...",
                                            to_field_name="acctFilterName"
                                            )

    excludeClassification = forms.ModelMultipleChoiceField(
            queryset=ClassificationNames.objects.all().values_list('classificationName', flat=True),
            label="Classifications Exclusion:",
            to_field_name="classificationName"
    )

    # tradingCash = forms.IntegerField(label="Remove accounts whose trading cash < % of AUM")
    # def __init__(self, *args, **kwargs):
    #
    #     super(AccountSelectionForm, self).__init__(*args, **kwargs)
    #     self.fields['acctFilterName']=forms.ModelChoiceField(queryset=AccountFilters.objects.all().values_list('acctFilterName'),
    #                                  empty_label="Select...",
    #                                  label="Account Filter Name:")
    #     self.fields['excludeClassification']=forms.ModelChoiceField(queryset=ClassificationNames.objects.all().values_list('classificationName'),
    #                                  widget=forms.SelectMultiple,
    #                                  empty_label=None,
    #                                  label="Exclude Classifications:")
    #                                   )
    class Meta:
        model = AccountParameters
        fields = ['acctFilterName', 'excludeClassification', 'tradingCash', ]
        labels = {
            'acctFilterName': _('Account Filters:'),
            'excludeClassification': _('Exclude Classifications: '),
            'tradingCash': _('Remove accounts whose trading cash < % of AUM: ')
        }


class SecuritySelectionModelForm(forms.ModelForm):
    class Meta:
        model = SecuritySelectionModels
        fields = ['securitySelectionModelName', ]
        labels = {
            'securitySelectionModelName': _('Selection Model:'),

        }
        exclude = ['classificationNames']

    def __init__(self, *args, **kwargs):
        super(SecuritySelectionModelForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-securitySelectionModelForm'
        self.helper.form_class = 'SecuritySelectionModelForm'
        self.helper.form_method = 'post'
        self.helper.form_action = 'createSecuritySelectionModels'
        self.helper.add_input(Submit('submit', 'Submit'))

    def clean(self):
        super(SecuritySelectionModelForm, self).clean()

        cleaned_data = self.cleaned_data
        ssm = SecuritySelectionModels.objects.filter(
                securitySelectionModelName=cleaned_data['securitySelectionModelName'])

        if ssm.exists() == 'True':
            raise forms.ValidationError("Model Already exists.")

        # Always return the full collection of cleaned data.
        return cleaned_data


class AccountsForm(forms.ModelForm):
    pass


class FeedsForm(forms.ModelForm):
    class Meta:
        model = Feeds
        exclude = []


class SecuritiesForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_tag = False

        self.helper.layout = Layout(
            TabHolder(
                Tab(
                    'Base',
                    'secName',
                    'shortName',
                    'mktPrice',
                    'secType',
                    'listExchCd',
                    'issueDate',
                    'issueState',
                    'issueCountry',
                    'baseCurrency',
                    'listExchCd',
                    FormActions(
                        Submit('save', 'Save changes'),
                        Button('cancel', 'Cancel')
                    )
                ),
                Tab(
                    'Fixed Income',
                    'couponRate',
                    'matureDate'
                ),
                Tab(
                    'Derivative',

                ),
                Tab(
                    'Identifiers',
                    'cusip',
                    'ticker',
                    'isin',
                    'sedol',
                    'valoran',
                    'ric'
                )
            )

        )
        super(SecuritiesForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Securities  # Your User model
        exclude = ('secId',)


class NoFormTagCrispyFormMixin(object):
    @property
    def helper(self):
        if not hasattr(self, '_helper'):
            self._helper = FormHelper()
            self._helper.form_tag = False
        return self._helper