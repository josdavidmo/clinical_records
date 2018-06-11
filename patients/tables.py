import django_tables2 as tables
from patients.models import CIE10
from patients.models import Paraclinical
from patients.models import Patient
from patients.models import MedicalHistory
from patients.models import Medicine


class PatientTable(tables.Table):
    can_add = True
    full_name_column = tables.Column(accessor='get_full_name',
                                     verbose_name='Nombre Completo',
                                     order_by=('names', 'last_names'))

    class Meta:
        model = Patient
        fields = ['full_name_column', 'document_type', 'document', 'gender',
                  'birth_city', 'birth_date', 'phone']
        template_name = 'django_tables2/custom_table.html'


class ParaclinicalTable(tables.Table):
    can_add = True

    class Meta:
        model = Paraclinical
        fields = ['name']
        template_name = 'django_tables2/custom_table.html'


class CIE10Table(tables.Table):
    can_add = True

    class Meta:
        model = CIE10
        fields = ['code', 'name']
        template_name = 'django_tables2/custom_table.html'


class MedicineTable(tables.Table):
    can_add = True

    class Meta:
        model = Medicine
        fields = ['name', 'medicine_type']
        template_name = 'django_tables2/custom_table.html'


class ClinicalRecordTable(tables.Table):

    date_time = tables.Column(accessor='get_full_date',
                              verbose_name='Fecha',
                              order_by=('created_at_date',
                                        'created_at_hour'))
    can_add = False

    class Meta:
        model = MedicalHistory
        fields = ['date_time', 'patient', 'companion', 'reason_consultation',
                  'current_illness']
        template_name = 'django_tables2/custom_table.html'
