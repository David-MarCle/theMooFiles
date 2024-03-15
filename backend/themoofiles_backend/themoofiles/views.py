from django.shortcuts import render
from rest_framework import generics
from themoofiles.models import Abductions
from themoofiles.serializers import AbductionSerializer
from rest_framework import viewsets

# Create your views here.
# class AbductionListAPIView(generics.ListAPIView):
#     queryset = Abductions.objects.all()
#     serializer_class = AbductionSerializer

class AbductionViewSet(viewsets.ModelViewSet):
     queryset = Abductions.objects.all()
     serializer_class = AbductionSerializer