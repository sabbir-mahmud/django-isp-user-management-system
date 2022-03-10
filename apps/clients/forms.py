# imports
from django.forms import ModelForm
from .models import Clients
from apps.users.models import Staffs


# client forms
class ClientForm(ModelForm):

    class Meta:
        model = Clients
        fields = '__all__'
        exclude = ['user', 'client_id']


# client forms
class StaffForm(ModelForm):

    class Meta:
        model = Staffs
        fields = '__all__'
