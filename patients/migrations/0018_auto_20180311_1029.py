# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-11 10:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0017_auto_20180311_0956'),
    ]

    operations = [
        migrations.CreateModel(
            name='MedicalFormulas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('remission', models.TextField(blank=True, null=True, verbose_name='Remisi\xf3n')),
                ('conduct', models.TextField(blank=True, null=True, verbose_name='Conducta')),
                ('medicines', models.ManyToManyField(null=True, to='patients.Medicine', verbose_name='Medicamentos')),
                ('paraclinicals', models.ManyToManyField(null=True, to='patients.Paraclinical', verbose_name='Paracl\xednicos')),
            ],
        ),
        migrations.RemoveField(
            model_name='medicalhistory',
            name='medicines',
        ),
        migrations.RemoveField(
            model_name='medicalhistory',
            name='paraclinicals',
        ),
        migrations.RemoveField(
            model_name='medicalhistory',
            name='remission',
        ),
        migrations.AlterField(
            model_name='medicalhistory',
            name='reason_consultation',
            field=models.TextField(verbose_name='Motivo de consulta'),
        ),
        migrations.AddField(
            model_name='medicalhistory',
            name='formulas',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='patients.MedicalFormulas'),
        ),
    ]
