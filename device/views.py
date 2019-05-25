from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.

from .models import Device
from .forms import DeviceForm, ModifyForm

import django.utils.timezone as timezone


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


def edit_device(request, device_id):
    """编辑既有条目"""
    device = Device.objects.get(id=device_id)
    # device.actual_time = timezone.now().strftime("%Y-%m-%d")
    if request.method != 'POST':
        # 初次请求，使用当前条目填充表单
        form = ModifyForm(instance=device)
    else:
        # POST提交的数据，对数据进行处理
        form = ModifyForm(instance=device, data=request.POST)
        if form.is_valid():
            if device.remark == 'NO':
                device.actual_time = '未归还'
            if device.remark == 'YES':
                # device.actual_time = timezone.now().strftime("%m{m}%d{d} %H:%m").format(m='月', d='日')
                device.actual_time = timezone.now().strftime("%m-%d %H:%m")
            form.save()
            return HttpResponseRedirect(reverse('device:index'))
    context = {'device': device, 'form': form}
    return render(request, 'device/edit_device.html', context)

