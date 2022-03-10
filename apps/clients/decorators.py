# imports
from django.shortcuts import redirect, HttpResponse


# authentication decorator
def logged(view_func):  # used for auto login

    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('inside')
        else:
            return view_func(request, *args, **kwargs)

    return wrapper_func


# user log redirect decorator
def user_roles(view_func):

    def wrapper_func(request, *args, **kwargs):
        if request.user.client == True:
            return redirect('user_dashboard')

        if request.user.worker == True:
            return redirect('client-show')

        if request.user.reseller == True:
            return redirect('reseller_dashboard')

        if request.user.owner == True:
            return view_func(request, *args, **kwargs)

        if request.user.admin == True:
            return view_func(request, *args, **kwargs)

    return wrapper_func


# admin/staff roles decorator
def admin_roles(view_func):

    def wrapper_func(request, *args, **kwargs):
        if request.user.admin == True:
            return view_func(request, *args, **kwargs)

        if request.user.owner == True:
            return view_func(request, *args, **kwargs)

        if request.user.worker == True:
            return redirect('client-show')

        if request.user.reseller == True:
            return redirect('reseller_dashboard')

        if request.user.client == True:
            return redirect('user_dashboard')

    return wrapper_func

# staff roles decorator


def staff_roles(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.admin == True:
            return view_func(request, *args, **kwargs)

        if request.user.owner == True:
            return view_func(request, *args, **kwargs)

        if request.user.worker == True:
            return view_func(request, *args, **kwargs)

        if request.user.reseller == True:
            return redirect('reseller_dashboard')

        if request.user.client == True:
            return redirect('user_dashboard')

    return wrapper_func
