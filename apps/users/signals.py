# imports
from django.db.models.signals import post_save
from .models import Staff_Id, Staffs
from apps.resellers.models import Resellers, ResellerId

# create staff id


def create_staff_id(sender, instance, created, *args, **kwargs):
    if created:
        ids = instance.staffs_Id
        Staff_Id.objects.create(staff_id=int(str(ids)) + 1)


post_save.connect(create_staff_id, sender=Staffs)


# create reseller id
def create_reseller_id(sender, instance, created, *args, **kwargs):
    if created:
        ids = instance.rid
        ResellerId.objects.create(reseller_id=int(str(ids)) + 1)


post_save.connect(create_reseller_id, sender=Resellers)
