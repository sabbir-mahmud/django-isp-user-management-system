import django_filters
from .models import Fiber, Mikrotik, Olt, Onu, Switch, Router, Pop


# fiber filter
class FiberFilter(django_filters.FilterSet):

    class Meta:
        model = Fiber
        fields = ['code']


# mikrotik filter
class MikrotikFilter(django_filters.FilterSet):

    class Meta:
        model = Mikrotik
        fields = ['serial_number']


# olt filter
class OltFilter(django_filters.FilterSet):

    class Meta:
        model = Olt
        fields = ['serial_number']


# onu filter
class OnuFilter(django_filters.FilterSet):

    class Meta:
        model = Onu
        fields = ['pon_mac']


# switch filter
class SwitchFilter(django_filters.FilterSet):

    class Meta:
        model = Switch
        fields = ['serial_number', 'ethernet_ports']


# router filter
class RouterFilter(django_filters.FilterSet):

    class Meta:
        model = Router
        fields = ['mac']


# pop filter
class PopFilter(django_filters.FilterSet):

    class Meta:
        model = Pop
        fields = ['pop_name']
