from django.shortcuts import render,get_object_or_404
from .models import Device,DeviceLog
from rest_framework import generics,permissions
from .serializers import DeviceSerializer,DeviceLogSerializer

# Create your views here.

""" DeviceList provides the list
and create operations"""

class DeviceList(generics.ListCreateAPIView):
    # queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        company = self.request.user.employee.company
        print('user=',self.request.user)
        queryset = Device.objects.filter(company=company)
        return queryset


"""
DeviceDetail provides the retrieve, 
update, and destroy operations.
"""

class DeviceDetail(generics.RetrieveUpdateDestroyAPIView):
    # queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_object(self):
        company = self.request.user.employee.company
        queryset = Device.objects.filter(company=company)
        obj = get_object_or_404(queryset, pk=self.kwargs['pk'])
        return obj


""" DeviceLogList provides the list
and create operations"""
class DeviceLogList(generics.ListCreateAPIView):
    # queryset = DeviceLog.objects.all()
    serializer_class = DeviceLogSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        company = self.request.user.employee.company
        queryset = DeviceLog.objects.filter(device__company=company)
        return queryset


"""
DeviceLogDetail provides the retrieve, 
update, and destroy operations.
"""
class DeviceLogDetail(generics.RetrieveUpdateDestroyAPIView):
    # queryset = DeviceLog.objects.all()
    serializer_class = DeviceLogSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        company = self.request.user.employee.company
        queryset = DeviceLog.objects.filter(device__company=company)
        obj = get_object_or_404(queryset,pk=self.kwargs['pk'])
        return obj




