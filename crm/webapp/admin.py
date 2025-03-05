from django.contrib import admin
from .models import Client

class ClientAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone', 'address', 'city', 'zip_code', 'created_at')  # Corrected field name

admin.site.register(Client, ClientAdmin)
