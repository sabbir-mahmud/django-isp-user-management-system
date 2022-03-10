# imports
from django.db.models.signals import post_save
from .models import Month, Year

# month active signal


def month_active(sender, instance, created, **kwargs):
    if created:
        new = Month.objects.get(pk=instance.id)
        olds = Month.objects.all().exclude(pk=instance.id)
        new.active = True
        new.save()
        for old in olds:
            old.active = False
            old.save()


post_save.connect(month_active, sender=Month)


# year active signal

def year_active(sender, instance, created, **kwargs):
    if created:
        new = Year.objects.get(pk=instance.id)
        olds = Year.objects.all().exclude(pk=instance.id)
        new.active = True
        new.save()
        for old in olds:
            old.active = False
            old.save()


post_save.connect(year_active, sender=Year)
