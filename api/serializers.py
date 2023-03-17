from rest_framework import serializers
from .models import Device, DeviceLog

class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = ['id', 'name', 'description', 'condition', 'company']

class DeviceLogSerializer(serializers.ModelSerializer):
    device = DeviceSerializer(read_only=True)
    employee = serializers.StringRelatedField()

    class Meta:
        model = DeviceLog
        fields = ['id', 'device', 'employee', 'checked_out', 'checked_in', 'condition']
