# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-16 12:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0004_auto_20180215_1208'),
    ]

    operations = [
        migrations.CreateModel(
            name='Laboratory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('middle_name', models.CharField(max_length=50, null=True)),
                ('last_name', models.CharField(max_length=50)),
                ('maiden_name', models.CharField(max_length=50, null=True)),
                ('birth_date', models.DateField()),
                ('address', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('document', models.CharField(db_index=True, max_length=20, unique=True)),
                ('document_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patients.DocumentType')),
                ('gender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patients.Gender')),
            ],
        ),
        migrations.RemoveField(
            model_name='patiente',
            name='document_type',
        ),
        migrations.RemoveField(
            model_name='patiente',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='medicalhistory',
            name='patiente',
        ),
        migrations.AddField(
            model_name='medicine',
            name='is_generic',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Patiente',
        ),
        migrations.AddField(
            model_name='medicalhistory',
            name='patient',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='patients.Patient'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='medicine',
            name='laboratory',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='patients.Laboratory'),
            preserve_default=False,
        ),
    ]
