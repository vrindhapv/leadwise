from django.urls import path
from api.views import LeadListCreateView,LeadRetrieveUpdateDeleteView,LeadSummaryView
from rest_framework.authtoken.models import Token

from rest_framework.authtoken.views import ObtainAuthToken


urlpatterns=[

    path("leads/",LeadListCreateView.as_view()),

    path("leads/<int:pk>/",LeadRetrieveUpdateDeleteView.as_view()),

    path("leads/summary/",LeadSummaryView.as_view()),

    path("token/",ObtainAuthToken.as_view()),


]