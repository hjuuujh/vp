# Generated by Django 3.2.8 on 2021-10-21 08:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('localstatus', '0002_auto_20211021_0805'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productdetail',
            name='c_code',
        ),
    ]
