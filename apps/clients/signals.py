# imports
from django.shortcuts import redirect
from django.db.models.signals import post_save, pre_save
from django.contrib.auth import get_user_model
from .models import Clients, ClientId
from apps.users.models import UserId
User = get_user_model()
# create client with signals


def create_client(sender, instance, created, **kwargs):
    if created:
        old_cid = ClientId.objects.filter(id=1).first()
        update_cid = old_cid.client_id + 1
        old_cid.client_id = update_cid
        old_cid.save()
        Clients.objects.create(
            user=instance,
            client_id=update_cid,
        )


# def create_user(sender, instance, **kwargs):
#     print(instance.first_name)
#     print(instance.gender)

#     Clients.objects.create(
#         user=new_user,
#         first_name=instance.first_name,
#         last_name=instance.last_name,
#         gender=instance.gender,
#         email=instance.email,
#         phone=instance.phone,
#         nid=instance.nid,
#         client_id=new_user_id,
#         ip_username=instance.ip_username,
#         address=instance.address,
#         olt_details=instance.olt_details,
#         onu_details=instance.onu_details,
#         switch_details=instance.switch_details,
#         router_details=instance.router_details,
#         package_details=instance.package_details,
#         pop_details=instance.pop_details,
#         status=instance.status,
#         paid=instance.paid,
#         reseller=instance.reseller,

#     )
#     return redirect('/')


# pre_save.connect(create_user, sender=Clients)
# post_save.connect(create_client, sender=User)
