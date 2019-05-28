"""定义device的URL模式"""

from django.urls import path, re_path

from . import views

app_name = 'device '

urlpatterns = [
    # 主页
    path('', views.index, name='index'),
    path('new_device', views.new_device, name='new_device'),
    re_path('edit_device/(?P<device_id>\d+)/', views.edit_device, name='edit_device'),
    re_path('return_device/(?P<device_id>\d+)/', views.return_device, name='return_device'),
]
