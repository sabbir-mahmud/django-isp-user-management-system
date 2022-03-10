# imports
import django_filters
from .models import Resellers_Commission


# client filter
class ComissionFilter(django_filters.FilterSet):

    class Meta:
        model = Resellers_Commission
        fields = ['month', 'year']
