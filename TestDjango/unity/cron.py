from .models import Leads
from django.utils import timezone
def my_scheduled_job():
    # filter leads subscribed in current month of year
    current_month_leads = Leads.objects.filter(
        action_time__year=timezone.now().year,
        action_time__month=timezone.now().month
    ).count()

    print(f'number subscribed in this month: { current_month_leads }')