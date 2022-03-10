# imports
from django.db import models
from apps.users.models import Staffs


# Total Investment Model
class Investment(models.Model):
    invest_details = models.CharField(max_length=500)
    invest_amount = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.invest_details


# Earning Model
class Earning(models.Model):
    earning_details = models.CharField(max_length=500,
                                       verbose_name='Earning Details')
    earning_amount = models.IntegerField(verbose_name='Earning Amount')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.earning_details


# bill profit model
class Upsteam_deal(models.Model):
    upsteam_deal = models.FloatField(default=40)

    def __str__(self):
        return str(self.upsteam_deal)


# Month Model
class Month(models.Model):
    month_name = models.CharField(max_length=20)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.month_name


# Year Model
class Year(models.Model):
    year_name = models.CharField(max_length=20)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.year_name


# Daily invoice model
class Daily_Invoice(models.Model):
    Staffs_details = models.ForeignKey(Staffs, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    month = models.ForeignKey(Month, on_delete=models.CASCADE)
    year = models.ForeignKey(Year, on_delete=models.CASCADE)
    invoice_amount = models.IntegerField()
    invoice_details = models.CharField(max_length=500)

    def __str__(self):
        return self.invoice_details

# Daily Earn model


class Daily_Earn(models.Model):
    Staffs_details = models.ForeignKey(Staffs, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    month = models.ForeignKey(Month, on_delete=models.CASCADE)
    year = models.ForeignKey(Year, on_delete=models.CASCADE)
    invoice_amount = models.IntegerField()
    invoice_details = models.CharField(max_length=500)

    def __str__(self):
        return self.invoice_details


# Monthly invoice model
class Monthly_Invoice(models.Model):
    Staffs_details = models.ForeignKey(Staffs, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    month = models.ForeignKey(Month, on_delete=models.CASCADE)
    year = models.ForeignKey(Year, on_delete=models.CASCADE)
    invoice_amount = models.IntegerField()
    invoice_details = models.CharField(max_length=500)

    def __str__(self):
        return self.invoice_details


# Monthly Earn model
class Monthly_Earn(models.Model):
    Staffs_details = models.ForeignKey(Staffs, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    month = models.ForeignKey(Month, on_delete=models.CASCADE)
    year = models.ForeignKey(Year, on_delete=models.CASCADE)
    invoice_amount = models.IntegerField()
    invoice_details = models.CharField(max_length=500)

    def __str__(self):
        return self.invoice_details


# Yearly Invoice model
class Yearly_Invoice(models.Model):
    Staffs_details = models.ForeignKey(Staffs, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    month = models.ForeignKey(Month, on_delete=models.CASCADE)
    year = models.ForeignKey(Year, on_delete=models.CASCADE)
    invoice_amount = models.IntegerField()
    invoice_details = models.CharField(max_length=500)

    def __str__(self):
        return self.invoice_details


# Monthly Earn model
class Yearly_Earn(models.Model):
    Staffs_details = models.ForeignKey(Staffs, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    month = models.ForeignKey(Month, on_delete=models.CASCADE)
    year = models.ForeignKey(Year, on_delete=models.CASCADE)
    invoice_amount = models.IntegerField()
    invoice_details = models.CharField(max_length=500)

    def __str__(self):
        return self.invoice_details
