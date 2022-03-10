# imports
from django.urls import path
from . import views

urlpatterns = [
    path('', views.reseller_dashboard, name='reseller_dashboard'),
    path('paid', views.reseller_dashboard_paid, name='reseller_dashboard_paid'),
    path('unpaid', views.reseller_dashboard_unpaid,
         name='reseller_dashboard_unpaid'),
    path('accounts', views.reseller_accounts, name='reseller_accounts'),
    # reseller comission add
    path('commission/add/<str:pk>', views.addComission,
         name='reseller_commission_add'),
]
