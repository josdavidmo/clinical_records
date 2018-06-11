# -*- coding: utf-8 -*-
from dateutil.relativedelta import relativedelta
from django.db.models import Q
from django.utils import timezone
from patients.models import CIE10
from patients.models import Patient
from patients.models import Paraclinical
from patients.models import MedicalHistory
from patients.models import Medicine
import datetime
import django_filters


class PatientFilter(django_filters.FilterSet):
    full_name_auto = django_filters.CharFilter(method='filter_full_name_auto',
                                               label='Nombre')
    age = django_filters.RangeFilter(method='filter_age',
                                     label='Edad')

    class Meta:
        model = Patient
        exclude = ('birth_date', 'phone', 'email', 'names', 'last_names',
                   'address', 'scholarship',
                   'profesion', 'civil_status', 'origin')

    def filter_age(self, queryset, name, value):
        current = datetime.datetime.now()
        if value.start < value.stop:
            min_date = datetime.date(
                current.year - value.start, current.month, current.day)
            max_date = datetime.date(
                current.year - (value.stop + 1), current.month, current.day + 1)
        else:
            min_date = datetime.date(
                current.year - (value.stop + 1), current.month, current.day + 1)
            max_date = datetime.date(
                current.year - value.start, current.month, current.day)
        return queryset.filter(birth_date__range=(max_date, min_date))

    def filter_full_name_auto(self, queryset, name, value):
        return queryset.filter(Q(names__contains=value) |
                               Q(last_names__contains=value))


class CIE10Filter(django_filters.FilterSet):
    class Meta:
        model = CIE10
        fields = {
            'code': ['contains'],
            'name': ['contains']
        }


class MedicineFilter(django_filters.FilterSet):
    class Meta:
        model = Medicine
        fields = {
            'name': ['contains'],
            'medicine_type': ['exact']
        }


class ParaclinicalFilter(django_filters.FilterSet):
    class Meta:
        model = Paraclinical
        fields = {
            'name': ['contains']
        }


class ClinicalHistoryFilter(django_filters.FilterSet):
    diagnostic = django_filters.MultipleChoiceFilter(
        method="filter_diagnostic",label="Diágnostico")

    def filter_diagnostic(self, queryset, name, value):
        return queryset.filter(physical_exam__diagnostics_images__id__in=value)

    class Meta:
        model = MedicalHistory
        fields = ['created_at_date', 'patient', 'diagnostic']
        exclude = ('clinical_history', 'physical_exam', 'systems_review',
                   'created_hour', 'city', 'phone_companion',
                   'referred_by', 'reason_consultation', 'sgss', 'companion',
                   'current_illness', 'formulas', 'created_at_hour')
