from django.shortcuts import render
from .models import Device,DeviceLog
from rest_framework import generics
from .serializers import DeviceSerializer,DeviceLogSerializer

# Create your views here.

""" DeviceList provides the list
and create operations"""

class DeviceList(generics.ListCreateAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer


"""
DeviceDetail provides the retrieve, 
update, and destroy operations.
"""

class DeviceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer


class DeviceLogList(generics.ListCreateAPIView):
    queryset = DeviceLog.objects.all()
    serializer_class = DeviceLogSerializer

class DeviceLogDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = DeviceLog.objects.all()
    serializer_class = DeviceLogSerializer

