# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-08 02:26
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0012_auto_20180307_0122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicalhistory',
            name='created_day',
            field=models.IntegerField(default=8, verbose_name='D\xeda'),
        ),
        migrations.AlterField(
            model_name='medicalhistory',
            name='created_hour',
            field=models.TimeField(default=datetime.datetime(2018, 3, 8, 2, 26, 10, 340589, tzinfo=utc), verbose_name='Hora'),
        ),
        migrations.AlterField(
            model_name='medicalhistory',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patients.Patient', verbose_name='Paciente'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='civil_status',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Estado civil'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='document_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patients.DocumentType', verbose_name='Tipo'),
        ),
    ]
