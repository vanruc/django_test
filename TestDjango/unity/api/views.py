from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from unity.models import Leads
from unity.api.serializers import LeadsSerializer


class LeadsListView(generics.ListAPIView):
    queryset = Leads.objects.all()
    serializer_class = LeadsSerializer


class LeadsSubscribe(APIView):
    def post(self, request):
        leads = Leads(email_id=request.data['email'])
        leads.save()
        return Response({
            'subscribed': True
        })
