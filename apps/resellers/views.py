# imports
from django.shortcuts import render, redirect
from .models import Resellers
from apps.clients.models import Clients
from .models import Resellers_Commission
from apps.core.models import Isp_info
from django.core.paginator import Paginator
from django.db.models import Sum, Q
from .filters import ComissionFilter
from .forms import Resellers_CommissionForm

# reseller_dashboard view


def reseller_dashboard(request):
    isp_info = Isp_info.objects.filter(id=1).first()

    # reseller clients
    rid = request.user
    reseller = Resellers.objects.filter(user=rid).first()
    clients = Clients.objects.filter(reseller=reseller).order_by('-id')
    p = Paginator(clients, 50)
    n = request.GET.get('p')
    clients = p.get_page(n)
    count = Clients.objects.filter(reseller=reseller).count()
    active_count = Clients.objects.filter(
        Q(status='Active') & Q(reseller=reseller)).count()
    inactive_count = Clients.objects.filter(
        Q(status='Inactive') & Q(reseller=reseller)).count()
    paid_count = Clients.objects.filter(Q(paid=True)
                                        & Q(status='Active') & Q(reseller=reseller)).count()
    unpaid_count = Clients.objects.filter(Q(paid=False)
                                          & Q(status='Active') & Q(reseller=reseller)).count()
    if request.method == 'POST':
        qs = request.POST.get('clients-id')
        print(qs)
        clients = Clients.objects.filter(
            reseller=reseller, client_id=qs).order_by('-id')
        print(clients)

    # context data
    context = {
        'isp_info': isp_info,
        'clients': clients,
        'count': count,
        'active': active_count,
        'inactive': inactive_count,
        'paid_count': paid_count,
        'unpaid_count': unpaid_count,
    }
    return render(request, 'resellers/reseller_dashboard.html', context)


# reseller_dashboard paid user view
def reseller_dashboard_paid(request):
    isp_info = Isp_info.objects.filter(id=1).first()

    # reseller clients
    rid = request.user
    reseller = Resellers.objects.filter(user=rid).first()
    clients = Clients.objects.filter(Q(paid=True)
                                     & Q(status='Active') & Q(reseller=reseller)).order_by('-id')
    p = Paginator(clients, 50)
    n = request.GET.get('p')
    clients = p.get_page(n)
    count = Clients.objects.filter(reseller=reseller).count()
    active_count = Clients.objects.filter(
        Q(status='Active') & Q(reseller=reseller)).count()
    inactive_count = Clients.objects.filter(
        Q(status='Inactive') & Q(reseller=reseller)).count()
    paid_count = Clients.objects.filter(Q(paid=True)
                                        & Q(status='Active') & Q(reseller=reseller)).count()
    unpaid_count = Clients.objects.filter(Q(paid=False)
                                          & Q(status='Active') & Q(reseller=reseller)).count()

    # context data
    context = {
        'isp_info': isp_info,
        'clients': clients,
        'count': count,
        'active': active_count,
        'inactive': inactive_count,
        'paid_count': paid_count,
        'unpaid_count': unpaid_count,
    }
    return render(request, 'resellers/reseller_dashboard.html', context)


# reseller_dashboard unpaid user view


def reseller_dashboard_unpaid(request):
    isp_info = Isp_info.objects.filter(id=1).first()

    # reseller clients
    rid = request.user
    reseller = Resellers.objects.filter(user=rid).first()
    clients = Clients.objects.filter(Q(paid=False)
                                     & Q(status='Active') & Q(reseller=reseller)).order_by('-id')
    p = Paginator(clients, 50)
    n = request.GET.get('p')
    clients = p.get_page(n)
    count = Clients.objects.filter(reseller=reseller).count()
    active_count = Clients.objects.filter(
        Q(status='Active') & Q(reseller=reseller)).count()
    inactive_count = Clients.objects.filter(
        Q(status='Inactive') & Q(reseller=reseller)).count()
    paid_count = Clients.objects.filter(Q(paid=True)
                                        & Q(status='Active') & Q(reseller=reseller)).count()
    unpaid_count = Clients.objects.filter(Q(paid=False)
                                          & Q(status='Active') & Q(reseller=reseller)).count()

    # context data
    context = {
        'isp_info': isp_info,
        'clients': clients,
        'count': count,
        'active': active_count,
        'inactive': inactive_count,
        'paid_count': paid_count,
        'unpaid_count': unpaid_count,
    }
    return render(request, 'resellers/reseller_dashboard.html', context)


# reseller_accounts view
def reseller_accounts(request):
    isp_info = Isp_info.objects.filter(id=1).first()

    # reseller clients
    rid = request.user
    reseller = Resellers.objects.filter(user=rid).first()
    clients = Clients.objects.filter(reseller=reseller)

    # reseller commission
    filters = ComissionFilter(
        request.GET, queryset=Resellers_Commission.objects.filter(resellerName=reseller))
    commissions = Resellers_Commission.objects.filter(
        resellerName=reseller)
    commissions = filters.qs
    # context data
    context = {
        'isp_info': isp_info,
        'commissions': commissions,
        'filters': filters,
    }
    return render(request, 'resellers/reseller_accounts.html', context)

#  add reseller commission


def addComission(request, pk):
    isp_info = Isp_info.objects.filter(id=1).first()
    reseller = Resellers.objects.filter(id=pk).first()
    if request.method == 'POST':
        form = Resellers_CommissionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reseller-list')
    else:
        form = Resellers_CommissionForm(initial={'resellerName': reseller})
    context = {
        'isp_info': isp_info,
        'form': form,
        'reseller': reseller,
    }
    return render(request, 'resellers/add_commission.html', context)
