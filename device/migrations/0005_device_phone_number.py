# Generated by Django 2.2.1 on 2019-05-24 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('device', '0004_auto_20190524_1600'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='phone_number',
            field=models.CharField(default=111111111, max_length=10),
            preserve_default=False,
        ),
    ]
