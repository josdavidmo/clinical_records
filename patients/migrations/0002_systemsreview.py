# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-13 19:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SystemsReview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skin_faneras', models.TextField(null=True)),
                ('orl', models.TextField(null=True)),
                ('respiratory', models.TextField(null=True)),
                ('cardiovascular', models.TextField(null=True)),
                ('digestive', models.TextField(null=True)),
                ('genitourinary', models.TextField(null=True)),
                ('snc_peripheral', models.TextField(null=True)),
                ('endocrine', models.TextField(null=True)),
                ('locomotor', models.TextField(null=True)),
                ('hematic_lymphatic', models.TextField(null=True)),
                ('senses_organs', models.TextField(null=True)),
            ],
        ),
    ]
