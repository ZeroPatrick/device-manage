from django import forms
from .models import Device


class DeviceForm(forms.ModelForm):
    class Meta:
        model = Device
        fields = ['device_name', 'conference_room', 'borrower', 'phone_number', 'department', 'expected_time']
        labels = {
            'device_name': '设备名称',
            'conference_room': '使用地点',
        }


class ModifyForm(forms.ModelForm):
    class Meta:
        model = Device
        fields = ['remark']
        #labels = {}