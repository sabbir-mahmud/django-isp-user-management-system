# imports
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from .models import Clients
from apps.users.models import Staffs, UserId
from .forms import StaffForm, ClientForm
from apps.core.models import Isp_info
from .decorators import admin_roles, staff_roles
from django.contrib.auth.decorators import login_required
from .filter import ClientFilter
from django.db.models import Sum, Q
from django.contrib.auth import get_user_model
User = get_user_model()

# matching user details and clients details


def user_match():
    user_id = UserId.objects.filter(id=1).first()
    client = Clients.objects.filter(client_id=user_id.user).first()
    if client is None:
        user = User.object.get(user_id=user_id.user)
        user.delete()
        user_id.user = user_id.user - 1
        user_id.save()


# staff view

@login_required(login_url='client-login')
@admin_roles
def staffShow(request):
    isp_info = Isp_info.objects.filter(id=1).first()
    staff = Staffs.objects.all().order_by('-id')
    salary = Staffs.objects.all().aggregate(Sum('salary'))
    p = Paginator(staff, 50)
    n = request.GET.get('p')
    staff = p.get_page(n)
    context = {'isp_info': isp_info, 'staff': staff, 'salary': salary}
    return render(request, 'staff/staff_show.html', context)


# staff adding view
@login_required(login_url='client-login')
@admin_roles
def staff_add(request):
    isp_info = Isp_info.objects.filter(id=1).first()
    if request.method == 'POST':
        form = StaffForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('staff-show')
    else:
        form = StaffForm()
    context = {'isp_info': isp_info, 'form': form}
    return render(request, 'staff/staff_add.html', context)


# staff details editing view
@login_required(login_url='client-login')
@admin_roles
def staff_edit(request, pk):
    isp_info = Isp_info.objects.filter(id=1).first()
    staff = Staffs.objects.filter(id=pk).first()
    if request.method == 'POST':
        form = StaffForm(request.POST, instance=staff)
        if form.is_valid():
            form.save()
            return redirect('staff-show')
    else:
        form = StaffForm(instance=staff)
    context = {'isp_info': isp_info, 'form': form}
    return render(request, 'staff/staff_add.html', context)


# delete staff view
@login_required(login_url='client-login')
@admin_roles
def staff_delete(request, pk):
    staff = Staffs.objects.filter(id=pk).first()
    staff.delete()
    return redirect('staff-show')


# client list view

@login_required(login_url='client-login')
@staff_roles
def client_list(request):
    # matching user details and clients details
    user_match()
    clients = Clients.objects.all().order_by('-id')
    filters = ClientFilter(request.GET, queryset=clients)
    clients = filters.qs
    p = Paginator(clients, 50)
    n = request.GET.get('p')
    clients = p.get_page(n)
    count = Clients.objects.all().count()
    active_count = Clients.objects.filter(status='Active').count()
    inactive_count = Clients.objects.filter(status='Inactive').count()
    paid_count = Clients.objects.filter(Q(paid=True)
                                        & Q(status='Active')).count()
    unpaid_count = Clients.objects.filter(Q(paid=False)
                                          & Q(status='Active')).count()
    isp_info = Isp_info.objects.filter(id=1).first()
    context = {
        'clients': clients,
        'count': count,
        'active': active_count,
        'inactive': inactive_count,
        'paid_count': paid_count,
        'unpaid_count': unpaid_count,
        'filters': filters,
        'isp_info': isp_info,
    }
    return render(request, 'clients/clients_list.html', context)

# paid client list view


@login_required(login_url='client-login')
@staff_roles
def paid_client_list(request):
    user_match()
    clients = Clients.objects.filter(Q(paid=True)
                                     & Q(status='Active')).order_by('-id')
    filters = ClientFilter(request.GET, queryset=clients)
    clients = filters.qs
    p = Paginator(clients, 50)
    n = request.GET.get('p')
    clients = p.get_page(n)
    count = Clients.objects.all().count()
    active_count = Clients.objects.filter(status='Active').count()
    inactive_count = Clients.objects.filter(status='Inactive').count()
    paid_count = Clients.objects.filter(Q(paid=True)
                                        & Q(status='Active')).count()
    unpaid_count = Clients.objects.filter(Q(paid=False)
                                          & Q(status='Active')).count()
    isp_info = Isp_info.objects.filter(id=1).first()
    context = {
        'clients': clients,
        'count': count,
        'active': active_count,
        'inactive': inactive_count,
        'paid_count': paid_count,
        'unpaid_count': unpaid_count,
        'filters': filters,
        'isp_info': isp_info,
    }
    return render(request, 'clients/clients_list.html', context)

# unpaid client list view


@login_required(login_url='client-login')
@staff_roles
def unpaid_client_list(request):
    # matching user details and clients details
    user_match()
    clients = Clients.objects.filter(Q(paid=False)
                                     & Q(status='Active')).order_by('-id')
    filters = ClientFilter(request.GET, queryset=clients)
    clients = filters.qs
    p = Paginator(clients, 50)
    n = request.GET.get('p')
    clients = p.get_page(n)
    count = Clients.objects.all().count()
    active_count = Clients.objects.filter(status='Active').count()
    inactive_count = Clients.objects.filter(status='Inactive').count()
    paid_count = Clients.objects.filter(Q(paid=True)
                                        & Q(status='Active')).count()
    unpaid_count = Clients.objects.filter(Q(paid=False)
                                          & Q(status='Active')).count()
    isp_info = Isp_info.objects.filter(id=1).first()
    context = {
        'clients': clients,
        'count': count,
        'active': active_count,
        'inactive': inactive_count,
        'paid_count': paid_count,
        'unpaid_count': unpaid_count,
        'filters': filters,
        'isp_info': isp_info,
    }
    return render(request, 'clients/clients_list.html', context)


# client edit view
@login_required(login_url='client-login')
@staff_roles
def client_edit(request, pk):
    client = Clients.objects.get(id=pk)
    form = ClientForm(instance=client)
    isp_info = Isp_info.objects.filter(id=1).first()
    print(client)
    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            print('Form is valid')
            return redirect('client-show')
    context = {
        'form': form,
        'isp_info': isp_info,
    }
    return render(request, 'clients/clients_edit.html', context)


# User/Client registration view
@login_required(login_url='client-login')
@staff_roles
def client_register(request):
    user_match()
    isp_info = Isp_info.objects.filter(id=1).first()
    user_id = UserId.objects.filter(id=1).first()
    new_user_id = user_id.user + 1
    user_id.user = new_user_id
    user_id.save()
    # creating new user:
    User.object.create_user(
        user_id=new_user_id,
        password='Knet121357'
    )
    new_user = User.object.get(user_id=new_user_id)

    # creating new client:
    form = ClientForm(initial={'user': new_user, 'client_id': new_user_id})
    if request.method == 'POST':
        form = ClientForm(request.POST, initial={
                          'user': new_user, 'client_id': new_user_id})
        if form.is_valid():
            form.save()
            return redirect('client-show')
    context = {
        'form': form,
        'isp_info': isp_info,
    }
    return render(request, 'clients/clients_add.html', context)


# user/client profile view

@login_required(login_url='client-login')
def client_profile(request):
    isp_info = Isp_info.objects.filter(id=1).first()
    context = {'isp_info': isp_info}
    return render(request, 'clients/clients_userpage.html', context)


# user/clients payments view
@login_required(login_url='client-login')
def clients_payment(request):
    isp_info = Isp_info.objects.filter(id=1).first()
    context = {'isp_info': isp_info}
    return render(request, 'clients/customer_payments.html', context)
