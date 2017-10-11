# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-11 07:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inheritance', '0002_school'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='school',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='inheritance.School'),
        ),
        migrations.AddField(
            model_name='teacher',
            name='school',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='inheritance.School'),
        ),
    ]
