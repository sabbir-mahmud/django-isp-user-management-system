# imports
from django.shortcuts import redirect
from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
from .models import Clients, ClientId
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


post_save.connect(create_client, sender=User)
