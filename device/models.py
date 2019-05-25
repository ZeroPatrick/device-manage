from django.db import models

import django.utils.timezone as timezone

# Create your models here.


class Device(models.Model):
    """设备名称"""
    device_name = models.CharField('设备名称', max_length=50)
    conference_room = models.CharField('使用地点', max_length=20)
    borrower = models.CharField('借用人', max_length=20)
    phone_number = models.CharField('联系电话', max_length=15)
    department = models.CharField('部门', max_length=20)
    borrow_time = models.DateTimeField('借用日期', auto_now_add=True)
    expected_time = models.CharField('预计归还日期', max_length=20)
    actual_time = models.CharField('实际归还时间', default='未归还', max_length=20, null=True, blank=True)
    # remark = models.CharField(max_length=100)
    DONOT = 'NO'
    RERUENED = 'YES'
    REMARK_CHOICES = [
        (DONOT, 'No'),
        (RERUENED, 'Yes'),
    ]
    remark = models.CharField(
        '备注',
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
