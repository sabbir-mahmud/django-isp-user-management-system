# imports
import django_filters
from .models import Clients


# client filter
class ClientFilter(django_filters.FilterSet):

    class Meta:
        model = Clients
        fields = ['client_id', 'ip_username', 'pop_details']
