from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
    path('devices/',views.DeviceList.as_view(),name='device_list'),
    path('devices/<int:pk>/',views.DeviceDetail.as_view(),name='device_detail'),
    path('device_log/',views.DeviceLogList.as_view(),name='device_log'),
    path('device_log/<int:pk>/',views.DeviceLogDetail.as_view(),name='device_log_detail'),
]
