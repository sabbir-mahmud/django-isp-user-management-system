# imports
from django.forms import ModelForm
from .models import Resellers_Commission

# Resellers_CommissionForm


class Resellers_CommissionForm(ModelForm):
    class Meta:
        model = Resellers_Commission
        fields = ['resellerName', 'month', 'year', 'commission_amount']
        labels = {
            'resellerName': 'Reseller Name',
            'month': 'Month',
            'year': 'Year',
            'commission_amount': 'Commission Amount',
        }
