# imports
from django.urls import path
from . import views

# urls patterns
urlpatterns = [
    path('', views.client_list, name='client-show'),
    path('paid_clients', views.paid_client_list, name='paid-client-show'),
    path('unpaid_clients', views.unpaid_client_list, name='unpaid-client-show'),
    path('client_add/', views.client_register, name='client-add'),
    path('client_update/<str:pk>/', views.client_edit, name='client-update'),
    path('profile/<str:pk>/', views.client_Profile, name='client-profile'),
    
    path('profile/user_dashboard', views.client_profile,
         name='user_dashboard'),
    path('profile/user_payments', views.clients_payment, name='user_payments'),
   
    # staff urls
    path('staff show', views.staffShow, name='staff-show'),
    path('staff Add', views.staff_add, name='staff-add'),
    path('staff Add/<str:pk>', views.staff_edit, name='staff-edit'),
    path('staff delete/<str:pk>', views.staff_delete, name='staff-del'),
]
