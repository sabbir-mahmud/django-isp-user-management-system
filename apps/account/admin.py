from django.contrib import admin
from .models import Investment, Earning, Upsteam_deal, Month, Year, Daily_Invoice, Monthly_Invoice, Daily_Earn, Monthly_Earn, Yearly_Earn, Yearly_Invoice

# Register your models here.
admin.site.register(Investment)
admin.site.register(Earning)
admin.site.register(Upsteam_deal)
admin.site.register(Month)
admin.site.register(Year)
admin.site.register(Daily_Invoice)
admin.site.register(Monthly_Invoice)
admin.site.register(Daily_Earn)
admin.site.register(Monthly_Earn)
admin.site.register(Yearly_Invoice)
admin.site.register(Yearly_Earn)
