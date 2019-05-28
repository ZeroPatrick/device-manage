from django.contrib import admin
from device.models import Device


# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display = ('device_name', 'conference_room', 'remark')
    search_fields = ('conference_name', 'remark',)


admin.site.register(Device, ContactAdmin)
