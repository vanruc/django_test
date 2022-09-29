from django.contrib import admin
from .models import Leads

# Register Admin App's models
@admin.register(Leads)
class LeadsAdmin(admin.ModelAdmin):
    list_display = ['email_id', 'action_time', 'status']
    list_filter = ['email_id', 'action_time', 'status']

