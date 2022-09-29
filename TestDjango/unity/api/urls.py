from django.urls import path
from . import views
app_name = 'unity'

urlpatterns = [
    path('leads/', views.LeadsListView.as_view(), name='leads_list'),
    path('leads/subscribe', views.LeadsSubscribe.as_view(), name='leads_subscribe'),
]