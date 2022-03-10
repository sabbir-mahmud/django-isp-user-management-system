# Accounts urls
# imports
from django.urls import path
from . import views

# urls
urlpatterns = [
    # Accounts Dashboard
    path('', views.account_dashboard, name='account-dashboard'),
    path('commission_info/<str:pk>',
         views.commissionUpdate,
         name='commissionUpdate'),
    # owner urls
    path('owner/', views.ownerShowing, name='owner-list'),
    path('owner/add/', views.addOwner, name='owner-add'),
    path('owner/edit/<str:pk>', views.editOwner, name='owner-edit'),
    path('owner/del/<str:pk>', views.delOwner, name='owner-del'),
    # reseller urls
    path('reseller/', views.resellerShowing, name='reseller-list'),
    path('reseller/add', views.addReseller, name='reseller-add'),
    path('reseller/edit/<str:pk>', views.editReseller, name='reseller-edit'),
    path('reseller/del/<str:pk>', views.delReseller, name='reseller-del'),
    # date urls
    path('month/', views.months, name='month-list'),
    path('month_edit/<str:pk>', views.monthEdit, name='month-edit'),
    path('month_active/<str:pk>', views.monthActive, name='month-active'),
    path('year/', views.years, name='year-list'),
    path('year_edit/<str:pk>', views.yearEdit, name='year-edit'),
    path('year_active/<str:pk>', views.yearActive, name='year-active'),
    # investment urls
    path('investment/', views.investmentShowing, name='investment-show'),
    path('investment_add/', views.investmentAdding, name='investment-add'),
    path('investment_edit/<str:pk>/',
         views.investmentEdit,
         name='investment-update'),
    path('investment_del/<str:pk>/',
         views.investmentDelete,
         name='investment-del'),
    # earning urls
    path('earning/', views.earningShowing, name='earning-show'),
    path('profit_add/', views.profitAdding, name='profit-add'),
    path('profit_edit/<str:pk>/', views.profitEdit, name='profit-update'),
    path('profit_del/<str:pk>/', views.profitDelete, name='profit-del'),
    # daily invoice urls
    path('daily_invoice/', views.dailyInvoiceShowing, name='daily-invoice'),
    path('daily_invoice_add/', views.dailyInvoiceAdd, name='daily-add'),
    path('daily_invoice_edit/<str:pk>/',
         views.dailyInvoicEdit, name='daily-edit'),
    path('daily_invoice_delete/<str:pk>/',
         views.dailyInvoiceDelete, name='daily-del'),
    # daily earning urls
    path('daily_earning/', views.dailyEarningShowing, name='daily-earning'),
    path('daily_earning_add/', views.dailyEarningAdd,
         name='daily-earning-add'),
    path('daily_earning_edit/<str:pk>/',
         views.dailyEarningEdit, name='daily-earning-edit'),
    path('daily_earning_del/<str:pk>/',
         views.dailyEarningDelete, name='daily-earning-del'),
    # monthly invoice urls
    path('monthly_invoice/', views.monthlyInvoiceShowing, name='monthly-invoice'),
    path('monthly_invoice_add/', views.monthlyInvoiceAdd, name='monthly-add'),
    path('monthly_invoice_edit/<str:pk>/',
         views.monthlyInvoicEdit, name='monthly-edit'),
    path('monthly_invoice_delete/<str:pk>/',
         views.monthlyInvoiceDelete, name='monthly-del'),
    # monthly earning urls
    path('monthly_earning/', views.monthlyEarningShowing, name='monthly-earning'),
    path('monthly_earning_add/', views.monthlyEarningAdd,
         name='monthly-earning-add'),
    path('monthly_earning_edit/<str:pk>/',
         views.monthlyEarningEdit, name='monthly-earning-edit'),
    path('monthly_earning_del/<str:pk>/',
         views.monthlyEarningDelete, name='monthly-earning-del'),
    # yearly invoice urls
    path('yearly_invoice/', views.yearlyInvoiceShowing, name='yearly-invoice'),
    path('yearly_invoice_add/', views.yearlyInvoiceAdd, name='yearly-add'),
    path('yearly_invoice_edit/<str:pk>/',
         views.yearlyInvoicEdit, name='yearly-edit'),
    path('yearly_invoice_delete/<str:pk>/',
         views.yearlyInvoiceDelete, name='yearly-del'),
    # yearly earning urls
    path('yearly_earning/', views.yearlyEarningShowing, name='yearly-earning'),
    path('yearly_earning_add/', views.yearlyEarningAdd, name='yearly-earning-add'),
    path('yearly_earning_edit/<str:pk>/',
         views.yearlyEarningEdit, name='yearly-earning-edit'),
    path('yearly_earning_del/<str:pk>/',
         views.yearlyEarningDelete, name='yearly-earning-del'),
]
