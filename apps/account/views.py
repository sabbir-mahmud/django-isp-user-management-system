# import
from django.shortcuts import render, redirect
from .models import Investment, Earning, Upsteam_deal, Month, Year, Daily_Invoice,  Daily_Earn, Monthly_Invoice, Monthly_Earn, Yearly_Earn, Yearly_Invoice
from apps.clients.models import Clients
from apps.users.models import Owners, Staffs
from apps.resellers.models import Resellers
from django.db.models import Sum
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from apps.clients.decorators import user_roles, admin_roles
from django.db.models import Q
from apps.core.models import Isp_info
from .forms import OwnerForm, ResellerForm, InvestmentAdd, EarningAdd, CommissionUpdate, DailyInvoiceAdd, DailyEarnAdd, MonthlyInvoiceAdd, MonthlyEarnAdd, YearlyEarnAdd, YearlyInvoiceAdd, MonthAdd, YearAdd


# Accounts Dashboard
@login_required(login_url='client-login')
@admin_roles
def account_dashboard(request):
    # Investment and profit details
    total_investment = Investment.objects.aggregate(Sum('invest_amount'))
    total_earning = Earning.objects.aggregate(Sum('earning_amount'))

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
    profit = total_profit(total_investment['invest_amount__sum'],
                          total_earning['earning_amount__sum'])
    loss = total_loss(total_investment['invest_amount__sum'],
                      total_earning['earning_amount__sum'])

    # Isp details
    isp_info = Isp_info.objects.filter(id=1).first()

    # billing details
    total_bill = Clients.objects.filter(status='Active').aggregate(
        Sum('package_details__price'))
    billprofit = Upsteam_deal.objects.get(id=1)
    billearn = (total_bill['package_details__price__sum'] *
                billprofit.upsteam_deal) / 100
    upsteamBill = total_bill['package_details__price__sum'] - billearn
    collectedBill = Clients.objects.filter(paid=True).aggregate(
        Sum('package_details__price'))
    pendingbill = total_bill['package_details__price__sum'] - collectedBill[
        'package_details__price__sum']

    # daily invoice amount
    total_daily_invoice = Daily_Invoice.objects.filter(
        Q(month__active=True) & Q(year__active=True)).aggregate(
        Sum('invoice_amount'))
    # daily earn amount
    total_daily_earn = Daily_Earn.objects.filter(
        Q(month__active=True) & Q(year__active=True)).aggregate(Sum('invoice_amount'))
    # monthly invoice amount
    total_monthly_invoice = Monthly_Invoice.objects.aggregate(
        Sum('invoice_amount'))
    # monthly earn amount
    total_monthly_earn = Monthly_Earn.objects.aggregate(Sum('invoice_amount'))
    # yearly invoice amount
    total_yearly_invoice = Yearly_Invoice.objects.aggregate(
        Sum('invoice_amount'))
    # yearly earn amount
    total_yearly_earn = Yearly_Earn.objects.aggregate(Sum('invoice_amount'))

    # total staff salary
    total_salary = Staffs.objects.filter(
        status='Active').aggregate(Sum('salary'))
    # isp info
    isp_info = Isp_info.objects.filter(id=1).first()
    # context
    context = {
        'isp_info': isp_info,
        'total_investment_price': total_investment,
        'total_earning': total_earning,
        'profit': profit,
        'loss': loss,
        'total_bill': total_bill,
        'billearn': billearn,
        'upsteamBill': upsteamBill,
        'collectedBill': collectedBill,
        'pendingbill': pendingbill,
        'total_salary': total_salary,
        'total_monthly_invoice': total_monthly_invoice,
        'total_monthly_earn': total_monthly_earn,
        'total_yearly_invoice': total_yearly_invoice,
        'total_yearly_earn': total_yearly_earn,
        'total_daily_invoice': total_daily_invoice,
        'total_daily_earn': total_daily_earn,

    }
    return render(request, 'core/account/account_dashboard.html', context)


# owner view
# owner details showing view
@login_required(login_url='client-login')
@admin_roles
def ownerShowing(request):
    # Isp details
    isp_info = Isp_info.objects.filter(id=1).first()
    owner = Owners.objects.all().order_by('-id')
    p = Paginator(owner, 50)
    n = request.GET.get('p')
    owners = p.get_page(n)
    context = {'isp_info': isp_info, 'owners': owners}
    return render(request, 'core/owner/owners.html', context)

# add owner view


@login_required(login_url='client-login')
@admin_roles
def addOwner(request):
    # Isp details
    isp_info = Isp_info.objects.filter(id=1).first()
    if request.method == 'POST':
        form = OwnerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('owner-list')
    else:
        form = OwnerForm()
    context = {'isp_info': isp_info, 'form': form}
    return render(request, 'core/owner/addowner.html', context)


# edit owner view
@login_required(login_url='client-login')
@admin_roles
def editOwner(request, pk):
    # Isp details
    isp_info = Isp_info.objects.filter(id=1).first()
    owner = Owners.objects.get(id=pk)
    if request.method == 'POST':
        form = OwnerForm(request.POST, instance=owner)
        if form.is_valid():
            form.save()
            return redirect('owner-list')
    else:
        form = OwnerForm(instance=owner)
    context = {'isp_info': isp_info, 'form': form}
    return render(request, 'core/owner/addowner.html', context)

# delete owner view


@login_required(login_url='client-login')
@admin_roles
def delOwner(request, pk):
    owner = Owners.objects.get(id=pk)
    owner.delete()
    return redirect('owner-list')


# reseller view
# reseller details showing view
@login_required(login_url='client-login')
@admin_roles
def resellerShowing(request):
    # Isp details
    isp_info = Isp_info.objects.filter(id=1).first()
    resellers = Resellers.objects.all().order_by('-id')
    p = Paginator(resellers, 50)
    n = request.GET.get('p')
    resellers = p.get_page(n)
    context = {'isp_info': isp_info, 'resellers': resellers}
    return render(request, 'core/reseller/resellers.html', context)

# add reseller view


@login_required(login_url='client-login')
@admin_roles
def addReseller(request):
    # Isp details
    isp_info = Isp_info.objects.filter(id=1).first()
    if request.method == 'POST':
        form = ResellerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reseller-list')
    else:
        form = ResellerForm()
    context = {'isp_info': isp_info, 'form': form}
    return render(request, 'core/reseller/addreseller.html', context)


# edit reseller view
@login_required(login_url='client-login')
@admin_roles
def editReseller(request, pk):
    # Isp details
    isp_info = Isp_info.objects.filter(id=1).first()
    reseller = Resellers.objects.get(id=pk)
    if request.method == 'POST':
        form = ResellerForm(request.POST, instance=reseller)
        if form.is_valid():
            form.save()
            return redirect('reseller-list')
    else:
        form = ResellerForm(instance=reseller)
    context = {'isp_info': isp_info, 'form': form}
    return render(request, 'core/reseller/addreseller.html', context)

# delete reseller view


@login_required(login_url='client-login')
@admin_roles
def delReseller(request, pk):
    reseller = Resellers.objects.get(id=pk)
    reseller.delete()
    return redirect('reseller-list')

# Investment view
# investment details showing view


@login_required(login_url='client-login')
@admin_roles
def investmentShowing(request):
    # Isp details
    isp_info = Isp_info.objects.filter(id=1).first()
    investment = Investment.objects.all().order_by('-id')
    p = Paginator(investment, 50)
    n = request.GET.get('p')
    investment = p.get_page(n)
    total = Investment.objects.aggregate(Sum('invest_amount'))
    context = {'isp_info': isp_info, 'investments': investment, 'total': total}
    return render(request, 'core/investment/investment_show.html', context)


# add new investment entry

@login_required(login_url='client-login')
@admin_roles
def investmentAdding(request):
    # Isp details
    isp_info = Isp_info.objects.filter(id=1).first()
    form = InvestmentAdd()
    if request.method == 'POST':
        form = InvestmentAdd(request.POST)
        if form.is_valid():
            form.save()
            return redirect('investment-show')
    context = {'isp_info': isp_info, 'form': form}
    return render(request, 'core/investment/investment_add.html', context)


# Edit investment entry

@login_required(login_url='client-login')
@admin_roles
def investmentEdit(request, pk):
    # Isp details
    isp_info = Isp_info.objects.filter(id=1).first()
    instance = Investment.objects.get(id=pk)
    form = InvestmentAdd(instance=instance)
    if request.method == 'POST':
        form = InvestmentAdd(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('investment-show')
    context = {'isp_info': isp_info, 'form': form}
    return render(request, 'core/investment/investment_edit.html', context)


# Delete investment entry
@login_required(login_url='client-login')
@admin_roles
def investmentDelete(request, pk):
    investment = Investment.objects.get(id=pk)
    investment.delete()
    return redirect('investment-show')


# Profit view
# profit details showing view
@login_required(login_url='client-login')
@admin_roles
def earningShowing(request):
    # Isp details
    isp_info = Isp_info.objects.filter(id=1).first()
    earning = Earning.objects.all().order_by('-id')
    p = Paginator(earning, 50)
    n = request.GET.get('p')
    earnings = p.get_page(n)
    total = Earning.objects.aggregate(Sum('earning_amount'))
    context = {'isp_info': isp_info, 'earning': earnings, 'total': total}
    return render(request, 'core/earning/profit_show.html', context)


# add new profit entry
@login_required(login_url='client-login')
@admin_roles
def profitAdding(request):
    # Isp details
    isp_info = Isp_info.objects.filter(id=1).first()
    form = EarningAdd()
    if request.method == 'POST':
        form = EarningAdd(request.POST)
        if form.is_valid():
            form.save()
            return redirect('earning-show')
    context = {'isp_info': isp_info, 'form': form}
    return render(request, 'core/earning/profit_add.html', context)


# Edit profit entry
@login_required(login_url='client-login')
@admin_roles
def profitEdit(request, pk):
    # Isp details
    isp_info = Isp_info.objects.filter(id=1).first()
    instance = Earning.objects.get(id=pk)
    form = EarningAdd(instance=instance)
    if request.method == 'POST':
        form = EarningAdd(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('earning-show')
    context = {'isp_info': isp_info, 'form': form}
    return render(request, 'core/earning/profit_edit.html', context)


# Delete profit entry
@login_required(login_url='client-login')
@admin_roles
def profitDelete(request, pk):
    earn = Earning.objects.get(id=pk)
    earn.delete()
    return redirect('earning-show')


# update commission details
@login_required(login_url='client-login')
@admin_roles
def commissionUpdate(request, pk):
    # Isp details
    isp_info = Isp_info.objects.filter(id=1).first()
    commission_info = Upsteam_deal.objects.filter(id=1).first()
    form = CommissionUpdate(instance=commission_info)
    if request.method == 'POST':
        form = CommissionUpdate(request.POST, instance=commission_info)
        if form.is_valid():
            form.save()
            return redirect('inside')

    context = {'form': form, 'isp_info': isp_info}
    return render(request, 'core/commission_update.html', context)


# daily invoice view
# daily invoice details showing view

def dailyInvoiceShowing(request):
    # Isp details
    isp_info = Isp_info.objects.filter(id=1).first()
    invoice = Daily_Invoice.objects.all().order_by('-id')
    p = Paginator(invoice, 50)
    n = request.GET.get('p')
    invoices = p.get_page(n)
    context = {'isp_info': isp_info, 'invoices': invoices}
    return render(request, 'core/invoice/dailyinvoices.html', context)

# daily invoice add


def dailyInvoiceAdd(request):
    # Isp details
    isp_info = Isp_info.objects.filter(id=1).first()
    staff_client = request.user.staffs
    month = Month.objects.filter(active=True).first()
    year = Year.objects.filter(active=True).first()
    form = DailyInvoiceAdd(
        initial={'Staffs_details': staff_client, 'month': month, 'year': year})
    if request.method == 'POST':
        form = DailyInvoiceAdd(request.POST)
        if form.is_valid():
            form.save()
            return redirect('daily-invoice')
    context = {'isp_info': isp_info, 'form': form}
    return render(request, 'core/invoice/invoice.html', context)


# daily invoice edit

def dailyInvoicEdit(request, pk):
    # Isp details
    isp_info = Isp_info.objects.filter(id=1).first()
    instance = Daily_Invoice.objects.get(id=pk)
    form = DailyInvoiceAdd(instance=instance)
    if request.method == 'POST':
        form = DailyInvoiceAdd(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('daily-invoice')
    context = {'isp_info': isp_info, 'form': form}
    return render(request, 'core/invoice/invoice.html', context)


# delete daily invoice
@login_required(login_url='client-login')
@admin_roles
def dailyInvoiceDelete(request, pk):
    invoice = Daily_Invoice.objects.get(id=pk)
    invoice.delete()
    return redirect('daily-invoice')


# daily earning view
# daily earning details showing view

#
def dailyEarningShowing(request):
    # Isp details
    isp_info = Isp_info.objects.filter(id=1).first()
    earning = Daily_Earn.objects.all().order_by('-id')
    p = Paginator(earning, 50)
    n = request.GET.get('p')
    earnings = p.get_page(n)
    context = {'isp_info': isp_info, 'earnings': earnings}
    return render(request, 'core/earnings/dailyearnings.html', context)

# daily earning add


def dailyEarningAdd(request):
    # Isp details
    isp_info = Isp_info.objects.filter(id=1).first()
    staff_client = request.user.staffs
    month = Month.objects.filter(active=True).first()
    year = Year.objects.filter(active=True).first()
    form = DailyEarnAdd(
        initial={'Staffs_details': staff_client, 'month': month, 'year': year})
    if request.method == 'POST':
        form = DailyEarnAdd(request.POST)
        if form.is_valid():
            form.save()
            return redirect('daily-earning')
    context = {'isp_info': isp_info, 'form': form}
    return render(request, 'core/invoice/invoice.html', context)


# daily Earning edit
def dailyEarningEdit(request, pk):
    # Isp details
    isp_info = Isp_info.objects.filter(id=1).first()
    instance = Daily_Earn.objects.get(id=pk)
    form = DailyEarnAdd(instance=instance)
    if request.method == 'POST':
        form = DailyEarnAdd(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('daily-earning')
    context = {'isp_info': isp_info, 'form': form}
    return render(request, 'core/invoice/invoice.html', context)


# delete daily earning
#
def dailyEarningDelete(request, pk):
    invoice = Daily_Earn.objects.get(id=pk)
    invoice.delete()
    return redirect('daily-earning')


# Monthly invoice view
# Monthly invoice details showing view
@login_required(login_url='client-login')
@admin_roles
def monthlyInvoiceShowing(request):
    # Isp details
    isp_info = Isp_info.objects.filter(id=1).first()
    invoice = Monthly_Invoice.objects.all().order_by('-id')
    p = Paginator(invoice, 50)
    n = request.GET.get('p')
    invoices = p.get_page(n)
    context = {'isp_info': isp_info, 'invoices': invoices}
    return render(request, 'core/invoice/monthlyinvoices.html', context)

# monthly invoice add


@login_required(login_url='client-login')
@admin_roles
def monthlyInvoiceAdd(request):
    # Isp details
    isp_info = Isp_info.objects.filter(id=1).first()
    staff_client = request.user.staffs
    month = Month.objects.filter(active=True).first()
    year = Year.objects.filter(active=True).first()
    form = MonthlyInvoiceAdd(
        initial={'Staffs_details': staff_client, 'month': month, 'year': year})
    if request.method == 'POST':
        form = MonthlyInvoiceAdd(request.POST)
        if form.is_valid():
            form.save()
            return redirect('monthly-invoice')
    context = {'isp_info': isp_info, 'form': form}
    return render(request, 'core/invoice/invoice.html', context)


# Monthly invoice edit
@login_required(login_url='client-login')
@admin_roles
def monthlyInvoicEdit(request, pk):
    # Isp details
    isp_info = Isp_info.objects.filter(id=1).first()
    instance = Monthly_Invoice.objects.get(id=pk)
    form = MonthlyInvoiceAdd(instance=instance)
    if request.method == 'POST':
        form = MonthlyInvoiceAdd(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('monthly-invoice')
    context = {'isp_info': isp_info, 'form': form}
    return render(request, 'core/invoice/invoice.html', context)


# delete monthly invoice
@login_required(login_url='client-login')
@admin_roles
def monthlyInvoiceDelete(request, pk):
    invoice = Monthly_Invoice.objects.get(id=pk)
    invoice.delete()
    return redirect('monthly-invoice')

# monthly earning view
# monthly earning details showing view


@login_required(login_url='client-login')
@admin_roles
def monthlyEarningShowing(request):
    # Isp details
    isp_info = Isp_info.objects.filter(id=1).first()
    earning = Monthly_Earn.objects.all().order_by('-id')
    p = Paginator(earning, 50)
    n = request.GET.get('p')
    earnings = p.get_page(n)
    context = {'isp_info': isp_info, 'earnings': earnings}
    return render(request, 'core/earnings/monthlyearnings.html', context)


# monthly earning add
@login_required(login_url='client-login')
@admin_roles
def monthlyEarningAdd(request):
    # Isp details
    isp_info = Isp_info.objects.filter(id=1).first()
    staff_client = request.user.staffs
    month = Month.objects.filter(active=True).first()
    year = Year.objects.filter(active=True).first()
    form = MonthlyEarnAdd(
        initial={'Staffs_details': staff_client, 'month': month, 'year': year})
    if request.method == 'POST':
        form = MonthlyEarnAdd(request.POST)
        if form.is_valid():
            form.save()
            return redirect('monthly-earning')
    context = {'isp_info': isp_info, 'form': form}
    return render(request, 'core/invoice/invoice.html', context)


# monthly Earning edit
@login_required(login_url='client-login')
@admin_roles
def monthlyEarningEdit(request, pk):
    # Isp details
    isp_info = Isp_info.objects.filter(id=1).first()
    instance = Monthly_Earn.objects.get(id=pk)
    form = MonthlyEarnAdd(instance=instance)
    if request.method == 'POST':
        form = MonthlyEarnAdd(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('monthly-earning')
    context = {'isp_info': isp_info, 'form': form}
    return render(request, 'core/invoice/invoice.html', context)


# delete monthly earning
@login_required(login_url='client-login')
@admin_roles
def monthlyEarningDelete(request, pk):
    invoice = Monthly_Earn.objects.get(id=pk)
    invoice.delete()
    return redirect('monthly-earning')


# yearly invoice view
# yearly invoice details showing view
@login_required(login_url='client-login')
@admin_roles
def yearlyInvoiceShowing(request):
    # Isp details
    isp_info = Isp_info.objects.filter(id=1).first()
    invoice = Yearly_Invoice.objects.all().order_by('-id')
    p = Paginator(invoice, 50)
    n = request.GET.get('p')
    invoices = p.get_page(n)
    context = {'isp_info': isp_info, 'invoices': invoices}
    return render(request, 'core/invoice/yearlyinvoice.html', context)


# yearly invoice add
@login_required(login_url='client-login')
@admin_roles
def yearlyInvoiceAdd(request):
    # Isp details
    isp_info = Isp_info.objects.filter(id=1).first()
    staff_client = request.user.staffs
    month = Month.objects.filter(active=True).first()
    year = Year.objects.filter(active=True).first()
    form = YearlyInvoiceAdd(
        initial={'Staffs_details': staff_client, 'month': month, 'year': year})
    if request.method == 'POST':
        form = YearlyInvoiceAdd(request.POST)
        if form.is_valid():
            form.save()
            return redirect('yearly-invoice')
    context = {'isp_info': isp_info, 'form': form}
    return render(request, 'core/invoice/invoice.html', context)


# yearly invoice edit
@login_required(login_url='client-login')
@admin_roles
def yearlyInvoicEdit(request, pk):
    # Isp details
    isp_info = Isp_info.objects.filter(id=1).first()
    instance = Yearly_Invoice.objects.get(id=pk)
    form = YearlyInvoiceAdd(instance=instance)
    if request.method == 'POST':
        form = YearlyInvoiceAdd(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('yearly-invoice')
    context = {'isp_info': isp_info, 'form': form}
    return render(request, 'core/invoice/invoice.html', context)


# delete yearly invoice
@login_required(login_url='client-login')
@admin_roles
def yearlyInvoiceDelete(request, pk):
    invoice = Yearly_Invoice.objects.get(id=pk)
    invoice.delete()
    return redirect('yearly-invoice')


# yearly earning view
# yearly earning details showing view
@login_required(login_url='client-login')
@admin_roles
def yearlyEarningShowing(request):
    # Isp details
    isp_info = Isp_info.objects.filter(id=1).first()
    earning = Yearly_Earn.objects.all().order_by('-id')
    p = Paginator(earning, 50)
    n = request.GET.get('p')
    earnings = p.get_page(n)
    context = {'isp_info': isp_info, 'earnings': earnings}
    return render(request, 'core/earnings/yearlyearning.html', context)

# yearly earning add


@login_required(login_url='client-login')
@admin_roles
def yearlyEarningAdd(request):
    # Isp details
    isp_info = Isp_info.objects.filter(id=1).first()
    staff_client = request.user.staffs
    month = Month.objects.filter(active=True).first()
    year = Year.objects.filter(active=True).first()
    form = YearlyEarnAdd(
        initial={'Staffs_details': staff_client, 'month': month, 'year': year})
    if request.method == 'POST':
        form = YearlyEarnAdd(request.POST)
        if form.is_valid():
            form.save()
            return redirect('yearly-earning')
    context = {'isp_info': isp_info, 'form': form}
    return render(request, 'core/invoice/invoice.html', context)


# yearly Earning edit
@login_required(login_url='client-login')
@admin_roles
def yearlyEarningEdit(request, pk):
    # Isp details
    isp_info = Isp_info.objects.filter(id=1).first()
    instance = Yearly_Earn.objects.get(id=pk)
    form = YearlyEarnAdd(instance=instance)
    if request.method == 'POST':
        form = YearlyEarnAdd(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('yearly-earning')
    context = {'isp_info': isp_info, 'form': form}
    return render(request, 'core/invoice/invoice.html', context)


# delete yearly earning
@login_required(login_url='client-login')
@admin_roles
def yearlyEarningDelete(request, pk):
    invoice = Yearly_Earn.objects.get(id=pk)
    invoice.delete()
    return redirect('yearly-earning')


# month add/show views
@login_required(login_url='client-login')
def months(request):
    # Isp details
    isp_info = Isp_info.objects.filter(id=1).first()
    months = Month.objects.all()
    if request.method == 'POST':
        form = MonthAdd(request.POST)
        if form.is_valid():
            form.save()
            return redirect('month-list')
    else:
        form = MonthAdd()
    context = {'isp_info': isp_info, 'form': form, 'months': months}
    return render(request, 'core/date/month.html', context)

# month edit view


@login_required(login_url='client-login')
def monthEdit(request, pk):
    # Isp details
    isp_info = Isp_info.objects.filter(id=1).first()
    months = Month.objects.all()
    instance = Month.objects.get(id=pk)
    if request.method == 'POST':
        form = MonthAdd(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('month-list')
    else:
        form = MonthAdd(instance=instance)
    context = {'isp_info': isp_info, 'form': form, 'months': months}
    return render(request, 'core/date/month.html', context)

# month active view


@login_required(login_url='client-login')
def monthActive(request, pk):
    # Isp details
    isp_info = Isp_info.objects.filter(id=1).first()
    months = Month.objects.all().exclude(id=pk)
    instance = Month.objects.get(id=pk)
    instance.active = True
    instance.save()
    for month in months:
        month.active = False
        month.save()
    return redirect('month-list')


# year add/show view
@login_required(login_url='client-login')
def years(request):
    # Isp details
    isp_info = Isp_info.objects.filter(id=1).first()
    months = Year.objects.all()
    if request.method == 'POST':
        form = YearAdd(request.POST)
        if form.is_valid():
            form.save()
            return redirect('year-list')
    else:
        form = YearAdd()
    context = {'isp_info': isp_info, 'form': form, 'months': months}
    return render(request, 'core/date/year.html', context)

# year edit view


@login_required(login_url='client-login')
def yearEdit(request, pk):
    # Isp details
    isp_info = Isp_info.objects.filter(id=1).first()
    months = Year.objects.all()
    instance = Year.objects.get(id=pk)
    if request.method == 'POST':
        form = YearAdd(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('year-list')
    else:
        form = YearAdd(instance=instance)
    context = {'isp_info': isp_info, 'form': form, 'months': months}
    return render(request, 'core/date/year.html', context)

# Year active view


@login_required(login_url='client-login')
def yearActive(request, pk):
    # Isp details
    isp_info = Isp_info.objects.filter(id=1).first()
    months = Year.objects.all().exclude(id=pk)
    instance = Year.objects.get(id=pk)
    instance.active = True
    instance.save()
    for month in months:
        month.active = False
        month.save()
    return redirect('year-list')
