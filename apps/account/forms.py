from .models import Investment, Earning, Upsteam_deal, Month, Year, Daily_Invoice, Monthly_Invoice, Yearly_Invoice, Daily_Earn, Monthly_Earn, Yearly_Earn
from django.forms import ModelForm
from apps.users.models import Owners
from apps.resellers.models import Resellers

# owner form


class OwnerForm(ModelForm):
    class Meta:
        model = Owners
        fields = '__all__'

# reseller form


class ResellerForm(ModelForm):
    class Meta:
        model = Resellers
        fields = '__all__'

# Investment form


class InvestmentAdd(ModelForm):

    class Meta:
        model = Investment
        fields = '__all__'


# earning form
class EarningAdd(ModelForm):

    class Meta:
        model = Earning
        fields = '__all__'


# Commission update form
class CommissionUpdate(ModelForm):

    class Meta:
        model = Upsteam_deal
        fields = '__all__'

# Month form


class MonthAdd(ModelForm):
    class Meta:
        model = Month
        fields = '__all__'

# Year form


class YearAdd(ModelForm):
    class Meta:
        model = Year
        fields = '__all__'


# Daily invoice form


class DailyInvoiceAdd(ModelForm):

    class Meta:
        model = Daily_Invoice
        fields = '__all__'


# Monthly invoice form


class MonthlyInvoiceAdd(ModelForm):

    class Meta:
        model = Monthly_Invoice
        fields = '__all__'


# Yearly invoice form


class YearlyInvoiceAdd(ModelForm):

    class Meta:
        model = Yearly_Invoice
        fields = '__all__'


# Daily Earning form


class DailyEarnAdd(ModelForm):

    class Meta:
        model = Daily_Earn
        fields = '__all__'

# Monthly Earning form


class MonthlyEarnAdd(ModelForm):

    class Meta:
        model = Monthly_Earn
        fields = '__all__'


# Yearly Earning form


class YearlyEarnAdd(ModelForm):

    class Meta:
        model = Yearly_Earn
        fields = '__all__'
