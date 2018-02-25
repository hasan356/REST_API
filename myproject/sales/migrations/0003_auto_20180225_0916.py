# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-02-25 09:16
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0002_auto_20180224_0548'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='itemlists', to=settings.AUTH_USER_MODEL),
        ),
    ]