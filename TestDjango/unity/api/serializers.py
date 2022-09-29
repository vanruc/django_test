from rest_framework import serializers
from unity.models import Leads


class LeadsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leads
        fields = ['email_id', 'action_time', 'status']