# Generated by Django 3.0.7 on 2020-06-29 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0003_auto_20200629_0856'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='img',
            new_name='cover_img',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='text',
        ),
        migrations.AlterField(
            model_name='blog',
            name='desc',
            field=models.CharField(max_length=1024),
        ),
    ]