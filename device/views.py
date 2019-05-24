from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.

from .models import Device
from .forms import DeviceForm


def index(request):
    """设备管理的主页"""
    objects = Device.objects.order_by('borrow_time')
    items = [obj.as_dict() for obj in objects]
    return render(request, 'device/index.html', {'items': items})


def new_device(request):
    if request.method != 'POST':
        # 未提交数据：创建一个新表单
        form = DeviceForm()
    else:
        # POST提交的数据，对数据进行处理
        form = DeviceForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('device:index'))
    context = {'form': form}
    return render(request, 'device/new_device.html', context)
