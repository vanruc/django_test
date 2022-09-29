import django.core.exceptions
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

import unity.models
from unity.models import Leads, Store
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
        # get and validate email
        req_email = request.data['email']
        try:
            validate_email(req_email)
        except django.core.exceptions.ValidationError as e:
            return Response({
                'issue': e.message
            })

        # get and validate Store
        # note: store id was hard coded to test multiple store concept
        store_id = 1
        try:
            store_obj = Store.objects.get(id=store_id)
        except Exception as e:
            return Response({
                'issue': e.message
            })

        try:
            leads = Leads(store=store_obj, email_id=req_email)
            leads.save()
        except Exception as e:
            return Response({
                'issue': e.message
            })

        return Response({
            'subscribed': 'success'
        })
