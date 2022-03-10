from django.contrib import admin
from .models import Clients, ClientId

# Register your models here.
admin.site.register(ClientId)
admin.site.register(Clients)
