from django.contrib import admin
from .models import Leads, Store

# Register Admin App's models
@admin.register(Leads)
class LeadsAdmin(admin.ModelAdmin):
    list_display = ['store', 'email_id', 'action_time', 'status']
    list_filter = ['store', 'status']

@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ['store_name', 'store_address']