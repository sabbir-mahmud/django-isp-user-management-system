# imports
from django.shortcuts import render, redirect
from apps.core.models import Isp_info
from django.contrib.auth import authenticate, login, logout
from apps.clients.decorators import logged
from apps.users.models import UserId
from apps.clients.models import Clients
from apps.clients.views import user_match
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your views here.


def home(request):
    # isp info
    isp_info = Isp_info.objects.filter(id=1).first()

    # context data
    context = {
        'isp_info': isp_info,
    }
    return render(request, 'home/home.html', context)


# user/client login view
@logged
def client_login(request):
    isp_info = Isp_info.objects.filter(id=1).first()
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('inside')

    context = {'isp_info': isp_info}
    return render(request, 'clients/clients_login.html', context)


# user/clients logout view
def client_logout(request):
    logout(request)
    return redirect('home-page')
