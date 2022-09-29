from django.urls import path
from . import views
app_name = 'unity'

urlpatterns = [
    path('leads/list', views.leads_listing, name='leads_list'),
]