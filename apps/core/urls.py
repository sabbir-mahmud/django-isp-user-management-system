# imports
from django.urls import path
from . import views

# urls
urlpatterns = [
    # inside urls
    path('', views.insideView, name='inside'),
    path('devices', views.devicesInfo, name='devicesInfo'),
    path('isp_info/<str:pk>', views.ispUpdate, name='updateInfo'),
    # fiber urls
    path('fiber/', views.fiberShow, name='fiber-show'),
    path('fiber_add/', views.fiberAdding, name='fiber-add'),
    path('fiber_edit/<str:pk>/', views.fiberEdit, name='fiber-edit'),
    path('fiber_del/<str:pk>/', views.fiberDelete, name='fiber-del'),
    # mikrotik urls
    path('mikrotik/', views.mikrotikShow, name='mikrotik-show'),
    path('mikrotik_add/', views.mikrotikAdding, name='mikrotik-add'),
    path('mikrotik_edit/<str:pk>/', views.mikrotikEdit,
         name='mikrotik-update'),
    path('mikrotik_del/<str:pk>/', views.mikrotikDelete, name='mikrotik-del'),
    # olt urls
    path('olt/', views.oltShowing, name='olt-show'),
    path('olt_add/', views.oltAdding, name='olt-add'),
    path('olt_edit/<str:pk>/', views.oltEdit, name='olt-update'),
    path('olt_del/<str:pk>/', views.oltDelete, name='olt-del'),
    # onu urls
    path('onu/', views.onuShowing, name='onu-show'),
    path('onu_add/', views.onuAdding, name='onu-add'),
    path('onu_edit/<str:pk>/', views.onuEdit, name='onu-update'),
    path('onu_del/<str:pk>/', views.onuDelete, name='onu-del'),
    # switch urls
    path('switch/', views.switchShowing, name='switch-show'),
    path('switch_add/', views.switchAdding, name='switch-add'),
    path('switch_edit/<str:pk>/', views.switchEdit, name='switch-update'),
    path('switch_del/<str:pk>/', views.switchDelete, name='switch-del'),
    # router urls
    path('router/', views.routerShowing, name='router-show'),
    path('router_add/', views.routerAdding, name='router-add'),
    path('router_edit/<str:pk>/', views.routerEdit, name='router-update'),
    path('router_del/<str:pk>/', views.routerDelete, name='router-del'),
    # package urls
    path('package/', views.packageShowing, name='package-show'),
    path('package_add/', views.packageAdding, name='package-add'),
    path('package_edit/<str:pk>/', views.packageEdit, name='package-update'),
    path('package_del/<str:pk>/', views.packageDelete, name='package-del'),
    # pop urls
    path('pop/', views.popShowing, name='pop-show'),
    path('pop_add/', views.popAdding, name='pop-add'),
    path('pop_edit/<str:pk>/', views.popEdit, name='pop-update'),
    path('pop_del/<str:pk>/', views.packageDelete, name='package-del'),
]
