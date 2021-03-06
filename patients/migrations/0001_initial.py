# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-13 12:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClinicalHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pathological', models.TextField(null=True)),
                ('surgical', models.TextField(null=True)),
                ('traumatic', models.TextField(null=True)),
                ('poisoning', models.TextField(null=True)),
                ('smoking', models.TextField(null=True)),
                ('liqueur', models.TextField(null=True)),
                ('psychoactive', models.TextField(null=True)),
                ('permanent_medication', models.TextField(null=True)),
                ('allergic', models.TextField(null=True)),
                ('immunological', models.TextField(null=True)),
                ('transfusions', models.TextField(null=True)),
                ('obstetric', models.TextField(null=True)),
                ('relatives', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='DocumentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Patiente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('middle_name', models.CharField(max_length=50, null=True)),
                ('last_name', models.CharField(max_length=50)),
                ('maiden_name', models.CharField(max_length=50, null=True)),
                ('birth_date', models.DateTimeField()),
                ('address', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('document', models.CharField(db_index=True, max_length=20, unique=True)),
                ('document_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patients.DocumentType')),
                ('gender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patients.Gender')),
            ],
        ),
    ]
