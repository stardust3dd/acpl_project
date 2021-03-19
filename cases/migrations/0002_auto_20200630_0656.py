# Generated by Django 3.0.7 on 2020-06-30 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cases', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='categories',
            field=models.CharField(choices=[('dmarketing', 'Digital Marketing'), ('msolutions', 'Marketing Solutions'), ('ranalytics', 'Research & Analytics')], default='Digital Marketing', max_length=128),
        ),
    ]