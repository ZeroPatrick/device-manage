# Generated by Django 2.2.1 on 2019-05-24 23:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('device', '0005_device_phone_number'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Room',
        ),
        migrations.AlterField(
            model_name='device',
            name='actual_time',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='保存日期'),
        ),
    ]