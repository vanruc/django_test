import django.core.exceptions
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from unity.models import Leads
from unity.api.serializers import LeadsSerializer
from django.core.validators import validate_email
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class LeadsListView(generics.ListAPIView):
    queryset = Leads.objects.all()
    serializer_class = LeadsSerializer


class LeadsSubscribe(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        ressult_str = {}
        req_email = request.data['email']
        try:
            validate_email(req_email)
            leads = Leads(email_id=request.data['email'])
            leads.save()
            ressult_str = {
                'subscribed': 'success'
            }
        except django.core.exceptions.ValidationError as e:
            ressult_str = {
                'issue': e.message
            }

        return Response(ressult_str)