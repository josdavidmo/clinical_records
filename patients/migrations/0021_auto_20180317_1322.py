# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-17 13:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0020_auto_20180317_1310'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='TypeMedicine',
            new_name='MedicineType',
        ),
        migrations.RenameField(
            model_name='medicine',
            old_name='type_medicine',
            new_name='medicine_type',
        ),
    ]
