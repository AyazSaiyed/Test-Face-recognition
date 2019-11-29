# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-09-20 09:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0003_users_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(blank=True, upload_to=b'')),
            ],
        ),
        migrations.RemoveField(
            model_name='users',
            name='image',
        ),
    ]
