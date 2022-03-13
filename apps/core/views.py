# imports
from django.shortcuts import render, redirect
from .models import Fiber, Mikrotik, Olt, Onu, Switch, Router, Package, Isp_info, Pop
from apps.account.models import Investment, Earning, Upsteam_deal, Month, Year, Daily_Invoice, Monthly_Invoice, Daily_Earn, Monthly_Earn, Yearly_Earn, Yearly_Invoice
from apps.clients.models import Clients
from apps.users.models import Owners, Staffs
from .forms import FiberAdd, MikrotikAdd, OltAdd, OnuAdd, SwitchAdd, RouterAdd, PackageAdd, IspUpdate, PopForm
from django.db.models import Sum
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from apps.clients.decorators import user_roles, admin_roles, staff_roles
from .filters import FiberFilter, MikrotikFilter, OltFilter, OnuFilter, SwitchFilter, RouterFilter, PopFilter
from django.db.models import Q
from apps.resellers.models import Resellers

# isp inside view


@login_required(login_url='client-login')
@user_roles
def insideView(request):
    # Isp details
    isp_info = Isp_info.objects.filter(id=1).first()
    # clients details
    count = Clients.objects.filter().count()
    active_count = Clients.objects.filter(status='Active').count()
    inactive_count = Clients.objects.filter(status='Inactive').count()
    paid_count = Clients.objects.filter(Q(paid=True)
                                        & Q(status='Active')).count()
    unpaid_count = Clients.objects.filter(Q(paid=False)
                                          & Q(status='Active')).count()
    # Investment and profit details
    total_investment = Investment.objects.aggregate(
        Sum('invest_amount'))['invest_amount__sum'] if Investment.objects.filter().exists() else 0
    total_earning = Earning.objects.aggregate(
        Sum('earning_amount'))['earning_amount__sum'] if Earning.objects.filter().exists() else 0
    # profit calculator

    def total_profit(invest, earn):
        if invest > earn:
            return 0
        else:
            return earn - invest
    # loss calculator

    def total_loss(invest, earn):
        if invest < earn:
            return 0
        else:
            return invest - earn
    # profit and loss details
    profit = total_profit(total_investment,
                          total_earning)
    loss = total_loss(total_investment,
                      total_earning)
    # billing details
    total_bill = Clients.objects.filter(status='Active').aggregate(
        Sum('package_details__price'))['package_details__price__sum'] if Clients.objects.filter().exists() else 0
    billprofit = Upsteam_deal.objects.get(id=1)
    billearn = (total_bill *
                billprofit.upsteam_deal) / 100
    upsteamBill = total_bill - billearn
    collectedBill = Clients.objects.filter(paid=True).aggregate(
        Sum('package_details__price'))['package_details__price__sum'] if Clients.objects.filter(paid=True).exists() else 0
    pendingbill = total_bill - collectedBill

    # devices
    total_olt = Olt.objects.filter(status='Active').count()
    total_onu = Onu.objects.filter(status='Active').count()
    total_switch = Switch.objects.filter(status='Active').count()

    # owner details
    cid = request.user
    owner = Owners.objects.filter(user=cid).first()
    share_amount = owner.commission
    invest_amount = owner.invest_amount
    profit_amount = billearn*share_amount/100

    # reseller and staff details
    reseller_count = Resellers.objects.all().count()
    staff_count = Staffs.objects.all().count()

    context = {
        'isp_info': isp_info,
        'count': count,
        'active': active_count,
        'inactive': inactive_count,
        'paid_count': paid_count,
        'unpaid_count': unpaid_count,
        'total_olt': total_olt,
        'total_onu': total_onu,
        'total_switch': total_switch,
        'share_amount': share_amount,
        'invest_amount': invest_amount,
        'profit_amount': profit_amount,
        'pendingbill': pendingbill,
        'collectedBill': collectedBill,
        'reseller_count': reseller_count,
        'staff_count': staff_count,

    }
    # returning html file
    return render(request, 'core/inside.html', context)


# devices insider view
@login_required(login_url='client-login')
@staff_roles
def devicesInfo(request):
    # Isp details
    isp_info = Isp_info.objects.filter(id=1).first()

    # fiber details
    total_fiber_price = Fiber.objects.aggregate(Sum('price'))
    total_fiber = Fiber.objects.aggregate(Sum('metre'))
    active_fiber = Fiber.objects.filter(status='Active').count()
    store_fiber = Fiber.objects.filter(status='Stored').count()
    damage_fiber = Fiber.objects.filter(status='Damaged').count()

    # mikrotik details
    total_mikrotik_price = Mikrotik.objects.aggregate(Sum('price'))
    total_mikrotik = Mikrotik.objects.all().count()
    active_mikrotik = Mikrotik.objects.filter(status='Active').count()
    store_mikrotik = Mikrotik.objects.filter(status='Stored').count()
    damage_mikrotik = Mikrotik.objects.filter(status='Damaged').count()

    # olt details
    total_olt_price = Olt.objects.aggregate(Sum('price'))
    total_olt = Olt.objects.all().count()
    active_olt = Olt.objects.filter(status='Active').count()
    store_olt = Olt.objects.filter(status='Stored').count()
    damage_olt = Olt.objects.filter(status='Damaged').count()

    # Onu details
    total_onu_price = Onu.objects.aggregate(Sum('price'))
    total_onu = Onu.objects.all().count()
    active_onu = Onu.objects.filter(status='Active').count()
    store_onu = Onu.objects.filter(status='Stored').count()
    damage_onu = Onu.objects.filter(status='Damaged').count()

    # Switch details
    total_switch_price = Switch.objects.aggregate(Sum('price'))
    total_switch = Switch.objects.all().count()
    active_switch = Switch.objects.filter(status='Active').count()
    store_switch = Switch.objects.filter(status='Stored').count()
    damage_switch = Switch.objects.filter(status='Damaged').count()

    # Router details
    total_router_price = Router.objects.aggregate(Sum('price'))
    total_router = Router.objects.all().count()
    active_router = Router.objects.filter(status='Active').count()
    store_router = Router.objects.filter(status='Stored').count()
    damage_router = Router.objects.filter(status='Damaged').count()

    context = {
        'isp_info': isp_info,
        'total_onu_price': total_onu_price,
        'total_onu': total_onu,
        'active_onu': active_onu,
        'store_onu': store_onu,
        'damage_onu': damage_onu,
        'total_switch_price': total_switch_price,
        'total_switch': total_switch,
        'active_switch': active_switch,
        'store_switch': store_switch,
        'damage_switch': damage_switch,
        'total_router_price': total_router_price,
        'total_router': total_router,
        'active_router': active_router,
        'store_router': store_router,
        'damage_router': damage_router,
        'total_fiber_price': total_fiber_price,
        'total_fiber': total_fiber,
        'active_fiber': active_fiber,
        'store_fiber': store_fiber,
        'damage_fiber': damage_fiber,
        'total_mikrotik_price': total_mikrotik_price,
        'total_mikrotik': total_mikrotik,
        'active_mikrotik': active_mikrotik,
        'store_mikrotik': store_mikrotik,
        'damage_mikrotik': damage_mikrotik,
        'total_olt_price': total_olt_price,
        'total_olt': total_olt,
        'active_olt': active_olt,
        'store_olt': store_olt,
        'damage_olt': damage_olt,
        'total_router_price': total_router_price,
        'total_router': total_router,
        'active_router': active_router,
        'store_router': store_router,
        'damage_router': damage_router,

    }
    return render(request, 'core/inside_devices.html', context)


# fiber view
# fiber details showing viewSwitchAdd
@login_required(login_url='client-login')
@staff_roles
def fiberShow(request):
    fiber = Fiber.objects.all().order_by('-id')
    filters = FiberFilter(request.GET, queryset=fiber)
    fiber = filters.qs
    # Isp details
    isp_info = Isp_info.objects.filter(id=1).first()
    p = Paginator(fiber, 50)
    n = request.GET.get('p')
    fiber = p.get_page(n)
    total = Fiber.objects.aggregate(Sum('price'))
    context = {
        'isp_info': isp_info,
        'fibers': fiber,
        'total': total,
        'filters': filters
    }
    return render(request, 'core/fiber/fiber_show.html', context)


# add new fiber entry
@login_required(login_url='client-login')
@staff_roles
def fiberAdding(request):
    # Isp details
    isp_info = Isp_info.objects.filter(id=1).first()
    form = FiberAdd()
    if request.method == 'POST':
        form = FiberAdd(request.POST)
        if form.is_valid():
            form.save()
            return redirect('fiber-show')
    context = {'isp_info': isp_info, 'form': form}
    return render(request, 'core/fiber/fiber_add.html', context)


# Edit fiber entry

@login_required(login_url='client-login')
@staff_roles
def fiberEdit(request, pk):
    # Isp details
    isp_info = Isp_info.objects.filter(id=1).first()
    instance = Fiber.objects.get(id=pk)
    form = FiberAdd(instance=instance)
    if request.method == 'POST':
        form = FiberAdd(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('fiber-show')
    context = {'isp_info': isp_info, 'form': form}
    return render(request, 'core/fiber/fiber_edit.html', context)


# fiber delete
@login_required(login_url='client-login')
@staff_roles
def fiberDelete(request, pk):
    fiber = Fiber.objects.get(id=pk)
    fiber.delete()
    return redirect('fiber-show')


# Mikrotik view
# Mikrotik details showing view
@login_required(login_url='client-login')
@staff_roles
def mikrotikShow(request):
    # Isp details
    isp_info = Isp_info.objects.filter(id=1).first()
    mikrotik = Mikrotik.objects.all().order_by('-id')
    filters = MikrotikFilter(request.GET, queryset=mikrotik)
    mikrotik = filters.qs
    p = Paginator(mikrotik, 5)
    n = request.GET.get('p')
    mikrotik = p.get_page(n)
    total = Mikrotik.objects.aggregate(Sum('price'))
    context = {
        'isp_info': isp_info,
        'mikrotiks': mikrotik,
        'total': total,
        'filters': filters
    }
    return render(request, 'core/mikrotik/mikrotik_show.html', context)


# add new Mikrotik entry
@login_required(login_url='client-login')
@staff_roles
def mikrotikAdding(request):
    # Isp details
    isp_info = Isp_info.objects.filter(id=1).first()
    form = MikrotikAdd()
    if request.method == 'POST':
        form = MikrotikAdd(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mikrotik-show')
    context = {'isp_info': isp_info, 'form': form}
    return render(request, 'core/mikrotik/mikrotik_add.html', context)


# Edit Mikrotik entry
@login_required(login_url='client-login')
@staff_roles
def mikrotikEdit(request, pk):
    # Isp details
    isp_info = Isp_info.objects.filter(id=1).first()
    instance = Mikrotik.objects.get(id=pk)
    form = MikrotikAdd(instance=instance)
    if request.method == 'POST':
        form = MikrotikAdd(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('mikrotik-show')
    context = {'isp_info': isp_info, 'form': form}
    return render(request, 'core/mikrotik/mikrotik_edit.html', context)


# Delete Mikrotik entry
@login_required(login_url='client-login')
@staff_roles
def mikrotikDelete(request, pk):
    mikrotik = Mikrotik.objects.get(id=pk)
    mikrotik.delete()
    return redirect('mikrotik-show')


# Olt view
# olt details showing view
@login_required(login_url='client-login')
@staff_roles
def oltShowing(request):
    olt = Olt.objects.all().order_by('-id')
    filters = OltFilter(request.GET, queryset=olt)
    olt = filters.qs
    # Isp details
    isp_info = Isp_info.objects.filter(id=1).first()
    p = Paginator(olt, 10)
    n = request.GET.get('p')
    olt = p.get_page(n)
    total = Olt.objects.aggregate(Sum('price'))
    context = {
        'isp_info': isp_info,
        'olts': olt,
        'total': total,
        'filters': filters
    }
    return render(request, 'core/olt/olt_show.html', context)


# add new olt entry
@login_required(login_url='client-login')
@staff_roles
def oltAdding(request):
    # Isp details
    isp_info = Isp_info.objects.filter(id=1).first()
    form = OltAdd()
    if request.method == 'POST':
        form = OltAdd(request.POST)
        if form.is_valid():
            form.save()
            return redirect('olt-show')
    context = {'isp_info': isp_info, 'form': form}
    return render(request, 'core/olt/olt_add.html', context)


# Edit olt entry
@login_required(login_url='client-login')
@staff_roles
def oltEdit(request, pk):
    # Isp details
    isp_info = Isp_info.objects.filter(id=1).first()
    instance = Olt.objects.get(id=pk)
    form = OltAdd(instance=instance)
    if request.method == 'POST':
        form = OltAdd(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('olt-show')
    context = {'isp_info': isp_info, 'form': form}
    return render(request, 'core/olt/olt_edit.html', context)


# Delete olt entry
@login_required(login_url='client-login')
@staff_roles
def oltDelete(request, pk):
    olt = Olt.objects.get(id=pk)
    olt.delete()
    return redirect('olt-show')


# Onu view
# onu details showing view
@login_required(login_url='client-login')
@staff_roles
def onuShowing(request):
    # Isp details
    isp_info = Isp_info.objects.filter(id=1).first()
    onu = Onu.objects.all().order_by('-id')
    filters = OnuFilter(request.GET, queryset=onu)
    onu = filters.qs
    p = Paginator(onu, 50)
    n = request.GET.get('p')
    onu = p.get_page(n)
    total = Onu.objects.aggregate(Sum('price'))
    context = {
        'isp_info': isp_info,
        'onus': onu,
        'total': total,
        'filters': filters
    }
    return render(request, 'core/onu/onu_show.html', context)


# add new onu entry
@login_required(login_url='client-login')
@staff_roles
def onuAdding(request):
    # Isp details
    isp_info = Isp_info.objects.filter(id=1).first()
    form = OnuAdd()
    if request.method == 'POST':
        form = OnuAdd(request.POST)
        if form.is_valid():
            form.save()
            return redirect('onu-show')
    context = {'isp_info': isp_info, 'form': form}
    return render(request, 'core/onu/onu_add.html', context)


# Edit onu entry
@login_required(login_url='client-login')
@staff_roles
def onuEdit(request, pk):
    # Isp details
    isp_info = Isp_info.objects.filter(id=1).first()
    instance = Onu.objects.get(id=pk)
    form = OnuAdd(instance=instance)
    if request.method == 'POST':
        form = OnuAdd(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('onu-show')
    context = {'isp_info': isp_info, 'form': form}
    return render(request, 'core/onu/onu_edit.html', context)


# Delete onu entry
@login_required(login_url='client-login')
@staff_roles
def onuDelete(request, pk):
    onu = Onu.objects.get(id=pk)
    onu.delete()
    return redirect('onu-show')


# Switch view
# switch details showing view
@login_required(login_url='client-login')
@staff_roles
def switchShowing(request):
    # Isp details
    isp_info = Isp_info.objects.filter(id=1).first()
    switch = Switch.objects.all().order_by('-id')
    filters = SwitchFilter(request.GET, queryset=switch)
    switch = filters.qs
    p = Paginator(switch, 50)
    n = request.GET.get('p')
    switch = p.get_page(n)
    total = Switch.objects.aggregate(Sum('price'))
    context = {
        'isp_info': isp_info,
        'switchs': switch,
        'total': total,
        'filters': filters
    }
    return render(request, 'core/switch/switch_show.html', context)


# add new Switch entry
@login_required(login_url='client-login')
@staff_roles
def switchAdding(request):
    # Isp details
    isp_info = Isp_info.objects.filter(id=1).first()
    form = SwitchAdd()
    if request.method == 'POST':
        form = SwitchAdd(request.POST)
        if form.is_valid():
            form.save()
            return redirect('switch-show')
    context = {'isp_info': isp_info, 'form': form}
    return render(request, 'core/switch/switch_add.html', context)


# Edit Switch entry
@login_required(login_url='client-login')
@staff_roles
def switchEdit(request, pk):
    # Isp details
    isp_info = Isp_info.objects.filter(id=1).first()
    instance = Switch.objects.get(id=pk)
    form = SwitchAdd(instance=instance)
    if request.method == 'POST':
        form = SwitchAdd(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('switch-show')
    context = {'isp_info': isp_info, 'form': form}
    return render(request, 'core/switch/switch_edit.html', context)


# Delete Switch entry
@login_required(login_url='client-login')
@staff_roles
def switchDelete(request, pk):
    switch = Switch.objects.get(id=pk)
    switch.delete()
    return redirect('switch-show')


# Router view
# router details showing view
@login_required(login_url='client-login')
@staff_roles
def routerShowing(request):
    # Isp details
    isp_info = Isp_info.objects.filter(id=1).first()
    router = Router.objects.all().order_by('-id')
    filters = RouterFilter(request.GET, queryset=router)
    router = filters.qs
    p = Paginator(router, 50)
    n = request.GET.get('p')
    router = p.get_page(n)
    total = Router.objects.aggregate(Sum('price'))
    context = {
        'isp_info': isp_info,
        'routers': router,
        'total': total,
        'filters': filters
    }
    return render(request, 'core/router/router_show.html', context)


# add new router entry
@login_required(login_url='client-login')
@staff_roles
def routerAdding(request):
    # Isp details
    isp_info = Isp_info.objects.filter(id=1).first()
    form = RouterAdd()
    if request.method == 'POST':
        form = RouterAdd(request.POST)
        if form.is_valid():
            form.save()
            return redirect('router-show')
    context = {'isp_info': isp_info, 'form': form}
    return render(request, 'core/router/router_add.html', context)


# Edit router entry
@login_required(login_url='client-login')
@staff_roles
def routerEdit(request, pk):
    # Isp details
    isp_info = Isp_info.objects.filter(id=1).first()
    instance = Router.objects.get(id=pk)
    form = RouterAdd(instance=instance)
    if request.method == 'POST':
        form = RouterAdd(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('router-show')
    context = {'isp_info': isp_info, 'form': form}
    return render(request, 'core/router/router_edit.html', context)


# Delete router entry
@login_required(login_url='client-login')
@staff_roles
def routerDelete(request, pk):
    router = Router.objects.get(id=pk)
    router.delete()
    return redirect('router-show')


# Package view
# package details showing view
@login_required(login_url='client-login')
@staff_roles
def packageShowing(request):
    # Isp details
    isp_info = Isp_info.objects.filter(id=1).first()
    package = Package.objects.all().order_by('-id')
    total = Package.objects.aggregate(Sum('price'))
    context = {'isp_info': isp_info, 'packages': package, 'total': total}
    return render(request, 'core/package/package_show.html', context)


# add new package entry
@login_required(login_url='client-login')
@staff_roles
def packageAdding(request):
    # Isp details
    isp_info = Isp_info.objects.filter(id=1).first()
    form = PackageAdd()
    if request.method == 'POST':
        form = PackageAdd(request.POST)
        if form.is_valid():
            form.save()
            return redirect('package-show')
    context = {'isp_info': isp_info, 'form': form}
    return render(request, 'core/package/package_add.html', context)


# Edit package entry
@login_required(login_url='client-login')
@staff_roles
def packageEdit(request, pk):
    # Isp details
    isp_info = Isp_info.objects.filter(id=1).first()
    instance = Package.objects.get(id=pk)
    form = PackageAdd(instance=instance)
    if request.method == 'POST':
        form = PackageAdd(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('package-show')
    context = {'isp_info': isp_info, 'form': form}
    return render(request, 'core/package/package_edit.html', context)


# Delete package entry
@login_required(login_url='client-login')
@staff_roles
def packageDelete(request, pk):
    package = Package.objects.get(id=pk)
    package.delete()
    return redirect('package-show')


# update isp details
@staff_roles
def ispUpdate(request, pk):
    isp_info = Isp_info.objects.filter(id=1).first()
    form = IspUpdate(instance=isp_info)
    if request.method == 'POST':
        form = IspUpdate(request.POST, instance=isp_info)
        if form.is_valid():
            form.save()
            return redirect('inside')

    context = {'form': form, 'isp_info': isp_info}
    return render(request, 'core/isp_update.html', context)


# pop showing view
@login_required(login_url='client-login')
@staff_roles
def popShowing(request):
    # Isp details
    isp_info = Isp_info.objects.filter(id=1).first()
    pop = Pop.objects.all().order_by('id')
    totalpop = Pop.objects.all().count()
    filters = PopFilter(request.GET, queryset=pop)
    pop = filters.qs
    p = Paginator(pop, 50)
    n = request.GET.get('p')
    pop = p.get_page(n)
    context = {
        'isp_info': isp_info,
        'pop': pop,
        'totalpop': totalpop,
        'filters': filters
    }
    return render(request, 'core/pop/pop_show.html', context)


# add new pop entry
@login_required(login_url='client-login')
@staff_roles
def popAdding(request):
    # Isp details
    isp_info = Isp_info.objects.filter(id=1).first()
    form = PopForm()
    if request.method == 'POST':
        form = PopForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pop-show')
    context = {'isp_info': isp_info, 'form': form}
    return render(request, 'core/pop/pop_add.html', context)


# Edit package entry
@login_required(login_url='client-login')
@staff_roles
def popEdit(request, pk):
    # Isp details
    isp_info = Isp_info.objects.filter(id=1).first()
    instance = Pop.objects.get(id=pk)
    form = PopForm(instance=instance)
    if request.method == 'POST':
        form = PopForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('pop-show')
    context = {'isp_info': isp_info, 'form': form}
    return render(request, 'core/pop/pop_edit.html', context)


# delete pop entry
@login_required(login_url='client-login')
@staff_roles
def packageDelete(request, pk):
    pop = Pop.objects.get(id=pk)
    pop.delete()
    return redirect('pop-show')
