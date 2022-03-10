# imports
from django.forms import ModelForm
from .models import Isp_info, Fiber, Mikrotik, Olt, Onu, Switch, Router, Package, Pop


# fiber form
class FiberAdd(ModelForm):

    class Meta:
        model = Fiber
        fields = '__all__'


# Mikrotik form
class MikrotikAdd(ModelForm):

    class Meta:
        model = Mikrotik
        fields = '__all__'


# Olt form
class OltAdd(ModelForm):

    class Meta:
        model = Olt
        fields = '__all__'


# Onu form
class OnuAdd(ModelForm):

    class Meta:
        model = Onu
        fields = '__all__'


# Switch form
class SwitchAdd(ModelForm):

    class Meta:
        model = Switch
        fields = '__all__'


# Router form
class RouterAdd(ModelForm):

    class Meta:
        model = Router
        fields = '__all__'


# Package form
class PackageAdd(ModelForm):

    class Meta:
        model = Package
        fields = '__all__'


# Isp info form
class IspUpdate(ModelForm):

    class Meta:
        model = Isp_info
        fields = '__all__'


# Commission update form
class PopForm(ModelForm):

    class Meta:
        model = Pop
        fields = '__all__'
