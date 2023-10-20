from rest_framework import generics

from django.shortcuts import render

from .models import SmartFarm
from .serializers import DoorListModelSerializer, FanListModelSerializer, InfoListModelSerializer, LedListModelSerializer, SmartFarmBaseModelSerializer, WarningListModelSerializer, WaterListModelSerializer

# Create your views here.
class InfoView(generics.ListAPIView):
    queryset = SmartFarm.objects.all()
    serializer_class = InfoListModelSerializer
    
class LedView(generics.ListAPIView):
    queryset = SmartFarm.objects.all()
    serializer_class = LedListModelSerializer
    
class WaterView(generics.ListAPIView):
    queryset = SmartFarm.objects.all()
    serializer_class = WaterListModelSerializer
    
class FanView(generics.ListAPIView):
    queryset = SmartFarm.objects.all()
    serializer_class = FanListModelSerializer
    
class DoorView(generics.ListAPIView):
    queryset = SmartFarm.objects.all()
    serializer_class = DoorListModelSerializer
    
class WarningView(generics.ListAPIView):
    queryset = SmartFarm.objects.all()
    serializer_class = WarningListModelSerializer