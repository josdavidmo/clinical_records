# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-17 13:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0019_auto_20180315_0729'),
    ]

    operations = [
        migrations.CreateModel(
            name='TypeMedicine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Tipo Medicina')),
            ],
        ),
        migrations.AddField(
            model_name='medicine',
            name='type_medicine',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='patients.TypeMedicine', verbose_name='Tipo Medicina'),
        ),
    ]
