# Generated by Django 3.0.7 on 2020-06-26 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('desc', models.CharField(blank=True, max_length=1024)),
                ('author', models.CharField(max_length=128)),
                ('text', models.TextField(default='')),
                ('date', models.DateField()),
                ('img', models.ImageField(upload_to='acpl/img/')),
                ('refr', models.CharField(blank=True, max_length=512)),
                ('categories', models.CharField(default='', max_length=128)),
                ('url', models.URLField(blank=True)),
            ],
        ),
    ]