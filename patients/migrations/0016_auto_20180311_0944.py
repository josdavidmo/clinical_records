# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-11 09:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0015_auto_20180310_1334'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='maiden_name',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='middle_name',
        ),
        migrations.AddField(
            model_name='patient',
            name='last_names',
            field=models.CharField(default='', max_length=100, verbose_name='Apellidos'),
        ),
        migrations.AddField(
            model_name='patient',
            name='names',
            field=models.CharField(default='', max_length=100, verbose_name='Nombres'),
        ),
        migrations.AlterField(
            model_name='medicalhistory',
            name='medicines',
            field=models.ManyToManyField(to='patients.Medicine', verbose_name='Medicamentos'),
        ),
        migrations.AlterField(
            model_name='medicalhistory',
            name='paraclinicals',
            field=models.ManyToManyField(to='patients.Paraclinical', verbose_name='Paracl\xednicos'),
        ),
        migrations.AlterField(
            model_name='physicalexam',
            name='IM',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='I.M.C'),
        ),
        migrations.AlterField(
            model_name='physicalexam',
            name='osteomuscular',
            field=models.TextField(blank=True, null=True, verbose_name='Muscular y osteoarticular'),
        ),
        migrations.AlterField(
            model_name='physicalexam',
            name='so',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='SPO2'),
        ),
        migrations.AlterField(
            model_name='physicalexam',
            name='tall',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Talla'),
        ),
    ]
