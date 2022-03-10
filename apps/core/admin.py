from django.contrib import admin
from .models import Isp_info, Fiber, Mikrotik, Olt, Onu, Switch, Router, Package, Pop

# Register your models here.
admin.site.register(Isp_info)
admin.site.register(Fiber)
admin.site.register(Mikrotik)
admin.site.register(Olt)
admin.site.register(Onu)
admin.site.register(Switch)
admin.site.register(Router)
admin.site.register(Package)
admin.site.register(Pop)
