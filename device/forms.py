from django import forms
from .models import Device


class DeviceForm(forms.ModelForm):
    class Meta:
        model = Device
        fields = ['device_name', 'conference_room', 'remark']
        # labels = { }