# Generated by Django 3.0.7 on 2020-06-30 01:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cases', '0002_auto_20200630_0656'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='case',
            name='refr',
        ),
    ]
