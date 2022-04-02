# imports
from django.db import models
from apps.account.models import Month, Year
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.
# reseller id model


class ResellerId(models.Model):
    reseller_id = models.IntegerField(default=7100)

    def __str__(self):
        return str(self.reseller_id)

# reseller model


class Resellers(models.Model):
    choice_status = (('Active', 'Active'), ('Inactive', 'Inactive'))
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rid = models.OneToOneField(ResellerId, on_delete=models.CASCADE)
    address = models.CharField(max_length=245)
    commission = models.FloatField(default=0)
    status = models.CharField(max_length=245, choices=choice_status)

    def __str__(self):
        return str(self.rid)

# resellers commission model


class Resellers_Commission(models.Model):
    resellerName = models.ForeignKey(
        Resellers, on_delete=models.CASCADE, verbose_name='Reseller Name')
    date = models.DateTimeField(auto_now_add=True)
    month = models.ForeignKey(Month, on_delete=models.CASCADE)
    year = models.ForeignKey(Year, on_delete=models.CASCADE)
    commission_amount = models.FloatField(default=0.0)

    def __str__(self):
        return str(self.resellerName)
