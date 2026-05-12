from django.shortcuts import render

# Create your views here.

from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView

from api.models import Lead
from api.serializers import LeadSerializer

from rest_framework.views import APIView

from django.db.models import Count

from rest_framework.response import Response

from rest_framework.authtoken.views import Token
from rest_framework.authtoken.views import ObtainAuthToken

from rest_framework import authentication,permissions




class LeadListCreateView(ListCreateAPIView):

    authentication_classes =[authentication.TokenAuthentication]

    permission_classes =[permissions.IsAdminUser]

    queryset = Lead.objects.all()

    serializer_class = LeadSerializer


class LeadRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):

    authentication_classes =[authentication.TokenAuthentication]

    permission_classes =[permissions.IsAdminUser]

    queryset = Lead.objects.all()

    serializer_class = LeadSerializer


class LeadSummaryView(APIView):

    authentication_classes =[authentication.TokenAuthentication]

    permission_classes =[permissions.IsAdminUser]

    def get(self,request,*args,**kwargs):
        
        
        summary = Lead.objects.values("status").annotate(total =Count("status"))

        return Response(data=summary)



