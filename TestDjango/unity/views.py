import math
from django.utils import timezone

from django.shortcuts import render
from .models import Leads
from django.core.paginator import Paginator


# Leads Listing page.
def leads_listing(request):
    leads_list = Leads.objects.all()

    # filter leads subscribed in current month of year
    current_month_leads = Leads.objects.filter(
        action_time__year = timezone.now().year,
        action_time__month = timezone.now().month
    ).count()

    # filter un-subscribed leads
    unsub_leads = Leads.objects.filter(
        status = 'UNS'
    ).count()

    #todo: apply pagination with 15 leads/page(temporary hardcoded)
    item_per_page = 15
    paginator = Paginator(leads_list, item_per_page)
    # get page number from request url, if there are no page parameter then get default = 1
    page_number = request.GET.get('page', 1)

    leads = paginator.get_page(page_number)
    context = {
        'total_leads': len(leads_list),
        'leads': leads,
        'current_month_leads_count': current_month_leads,
        'unsub_leads' : unsub_leads,
    }
    return render(request, 'unity/leads/list.html', context)