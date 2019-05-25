from django.db import models

import django.utils.timezone as timezone

# Create your models here.


class Device(models.Model):
    """设备名称"""
    device_name = models.CharField(max_length=50)
    conference_room = models.CharField(max_length=20)
    borrower = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=10)
    department = models.CharField(max_length=20)
    borrow_time = models.DateTimeField(auto_now_add=True)
    expected_time = models.CharField(max_length=50)
    actual_time = models.DateTimeField('保存日期', default=timezone.now)
    #remark = models.CharField(max_length=100)
    DONOT = 'NO'
    RERUENED = 'YES'
    REMARK_CHOICES = [
        (DONOT, 'No'),
        (RERUENED, 'Yes'),
    ]
    remark = models.CharField(
        max_length=20,
        choices=REMARK_CHOICES,
        default=DONOT,
    )

    def as_dict(self):
        return {
            "device_name": self.device_name,
            "conference_name": self.conference_room,
            "borrower": self.borrower,
            "phone_number": self.phone_number,
            "department": self.department,
            "borrow_time": self.borrow_time,
            "expected_time": self.expected_time,
            "actual_time": self.actual_time,
            "remark": self.remark,
            "id": self.id,
        }

    def __str__(self):
        """返回内容"""
        return self.device_name
