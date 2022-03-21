# imports
from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group
from .forms import UserAdminCreationForm, UserAdminChangeForm

# Register your models here.
from django.contrib.auth import get_user_model
User = get_user_model()

# unregister group model
admin.site.unregister(Group)


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm
    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ['user_id', 'admin']
    list_filter = ['user_id']
    fieldsets = (
        (None, {'fields': ('user_id', 'password')}),
        ('Permissions', {
         'fields': ('client', 'reseller', 'owner', 'worker', 'staff', 'admin')}),

    )

    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('user_id', 'password', 'password2', 'staff', 'admin')}
         ),
    )
    search_fields = ['user_id']
    ordering = ['user_id']
    filter_horizontal = ()

    class Meta:
        model = User
        fields = ['user_id']


# others models
admin.site.register(Owners)
admin.site.register(Staff_Id)
admin.site.register(Staffs)
admin.site.register(UserId)
