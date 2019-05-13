from django.shortcuts import render
# Create your views here.

from .models import Device


def index(request):
    """设备管理的主页"""
    objects = Device.objects.order_by('borrow_time')
    items = [obj.as_dict() for obj in objects]
    return render(request, 'device/index.html', {'items': items})