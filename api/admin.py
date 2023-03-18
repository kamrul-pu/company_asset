from django.contrib import admin
from .models import Company,Employee,Device,DeviceLog
# Register your models here.

class DeviceAdmin(admin.ModelAdmin):
    list_display = ['name','condition','company']

class DeviceLogAdmin(admin.ModelAdmin):
    list_display = ['device','employee','checked_out','checked_in','condition']

admin.site.register(Company)
admin.site.register(Employee)
admin.site.register(Device,DeviceAdmin)
admin.site.register(DeviceLog,DeviceLogAdmin)
