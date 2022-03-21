# imports
from django.db import models
from django.contrib.auth import get_user_model
from apps.core.models import Olt, Onu, Switch, Router, Package, Pop
from apps.resellers.models import Resellers

# user register form
User = get_user_model()

# client id model


class ClientId(models.Model):
    client_id = models.IntegerField(default=117100)

    def __str__(self):
        return str(self.client_id)

# client model


class Clients(models.Model):
    genders = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Others', 'Others'),
    )
    choice_status = (('Active', 'Active'), ('Inactive', 'Inactive'))
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=245)
    last_name = models.CharField(max_length=245)
    gender = models.CharField(max_length=245, choices=genders)
    email = models.EmailField(max_length=245)
    phone = models.CharField(max_length=11)
    nid = models.CharField(max_length=13, unique=True)
    client_id = models.IntegerField(unique=True)
    ip_username = models.CharField(max_length=20,
                                   unique=True,
                                   null=True,
                                   blank=True,
                                   verbose_name='IP/Username')
    address = models.CharField(max_length=100)
    olt_details = models.OneToOneField(Olt,
                                       on_delete=models.CASCADE,
                                       null=True,
                                       blank=True)
    onu_details = models.OneToOneField(Onu,
                                       on_delete=models.CASCADE,
                                       null=True,
                                       blank=True)
    switch_details = models.OneToOneField(Switch,
                                          on_delete=models.CASCADE,
                                          null=True,
                                          blank=True)
    router_details = models.OneToOneField(Router,
                                          on_delete=models.CASCADE,
                                          null=True,
                                          blank=True)
    package_details = models.ForeignKey(Package,
                                        on_delete=models.CASCADE,
                                        null=True,
                                        blank=True)
    pop_details = models.ForeignKey(Pop,
                                    on_delete=models.CASCADE,
                                    null=True,
                                    blank=True)
    status = models.CharField(max_length=100,
                              default='Active',
                              choices=choice_status)
    paid = models.BooleanField(default=False)
    reseller = models.ForeignKey(
        Resellers, on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.client_id)
