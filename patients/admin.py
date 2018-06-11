# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from patients.models import DocumentType
from patients.models import Gender
from patients.models import MedicineType

admin.site.register(DocumentType)
admin.site.register(Gender)
admin.site.register(MedicineType)
