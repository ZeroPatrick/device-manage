from django.db import models


# Create your models here.


class Device(models.Model):
    """设备名称"""
    device_name = models.CharField(max_length=50)
    conference_room = models.CharField(max_length=20)
    department = models.CharField(max_length=20)
    borrower = models.CharField(max_length=20)
    borrow_time = models.DateTimeField(auto_now_add=True)
    expected_time = models.CharField(max_length=50)
    actual_time = models.CharField(max_length=50)
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
            "department": self.department,
            "borrow_time": self.borrow_time,
            "expected_time": self.expected_time,
            "remark": self.remark,
        }

    def __str__(self):
        """返回内容"""
        return self.device_name


class Room(models.Model):
    """设备名称"""
    device_name = models.CharField(max_length=50)
    conference_room = models.CharField(max_length=20)
    department = models.CharField(max_length=20)
    borrower = models.CharField(max_length=20)
    borrow_time = models.DateTimeField(auto_now_add=True)
    expected_time = models.CharField(max_length=50)
    actual_time = models.CharField(max_length=50)
    remark = models.CharField(max_length=100)

    def __str__(self):
        """返回内容"""
        return self.conference_room