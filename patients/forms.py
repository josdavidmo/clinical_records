from clinical_records import settings
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Div, Field, Layout, Submit
from django import forms
from django.forms import DateField
from django.forms import ModelForm
from patients.models import CIE10
from patients.models import ClinicalHistory
from patients.models import MedicalFormulas
from patients.models import MedicalHistory
from patients.models import PhysicalExam
from patients.models import SystemsReview
from patients.models import Patient


class PatientForm(ModelForm):
    birth_date = DateField(input_formats=settings.DATE_INPUT_FORMATS)
    helper = FormHelper()
    helper.form_class = 'form-inline'
    helper.form_tag = False
    helper.layout = Layout(
        Div(
            Div('names', css_class='column_two'),
            Div('last_names', css_class='column_two'),
            css_class='row'),
        Div(
            Div('document_type', css_class='column_two'),
            Div('document', css_class='column_two'),
            css_class='row'),
        Div(
            Div('birth_date', css_class='column_two'),
            Div('birth_city', css_class='column_two'),
            css_class='row'),
        Div(
            Div('address', css_class='column_two'),
            Div('phone', css_class='column_two'),
            css_class='row'),
        Div(
            Div('scholarship', css_class='column_two'),
            Div('profesion', css_class='column_two'),
            css_class='row'),
        Div(
            Div('gender', css_class='column_three'),
            Div('civil_status', css_class='column_three'),
            Div('origin', css_class='column_three'),
            css_class='row'),
    )

    class Meta(object):
        model = Patient
        fields = '__all__'
        widgets = {
            'birth_date': forms.DateInput(format=('%Y-%m-%d'), attrs={'type': 'date'})
        }


class MedicalFormulasForm(ModelForm):
    helper = FormHelper()
    helper.form_class = 'form-inline'
    helper.form_tag = False
    helper.layout = Layout(
        Div(
            Div('medicines', css_class='column_one'),
            css_class='row'),
        Div(
            Div('paraclinicals', css_class='column_one'),
            css_class='row'),
        Div(
            Div('remission', css_class='column_one'),
            css_class='row'),
        Div(
            Div('conduct', css_class='column_one'),
            css_class='row'),
    )

    class Meta(object):
        model = MedicalFormulas
        fields = '__all__'


class MedicalHistoryForm(ModelForm):
    helper = FormHelper()
    helper.form_class = 'form-inline'
    helper.layout = Layout(
        Div(
            Div('companion', css_class='column_two'),
            Div('phone_companion', css_class='column_two'),
            css_class='row'),
        Div(
            Div('referred_by', css_class='column_two'),
            Div('sgss', css_class='column_two'),
            css_class='row'),
        Div(
            Div('created_at_date', css_class='column_two'),
            Div('created_at_hour', css_class='column_two'),
            css_class='row'),
        Div(
            Div('reason_consultation', css_class='column_one'),
            css_class='row'),
        Div(
            Div('current_illness', css_class='column_one'),
            css_class='row')
    )

    class Meta(object):
        model = MedicalHistory
        fields = ['created_at_date', 'created_at_hour', 'companion',
                  'referred_by', 'phone_companion',
                  'reason_consultation', 'current_illness', 'sgss']


class ClinicalHistoryForm(ModelForm):
    helper = FormHelper()
    helper.form_class = 'form-inline'
    helper.form_tag = False
    helper.layout = Layout(
        Div(
            Div('pathological', css_class='column_one'),
            css_class='row'),
        Div(
            Div('surgical', css_class='column_one'),
            css_class='row'),
        Div(
            Div('traumatic', css_class='column_one'),
            css_class='row'),
        Div(
            Div('poisoning', css_class='column_one'),
            css_class='row'),
        Div(
            Div('smoking', css_class='column_one'),
            css_class='row'),
        Div(
            Div('liqueur', css_class='column_one'),
            css_class='row'),
        Div(
            Div('psychoactive', css_class='column_one'),
            css_class='row'),
        Div(
            Div('permanent_medication', css_class='column_one'),
            css_class='row'),
        Div(
            Div('allergic', css_class='column_one'),
            css_class='row'),
        Div(
            Div('immunological', css_class='column_one'),
            css_class='row'),
        Div(
            Div('transfusions', css_class='column_one'),
            css_class='row'),
        Div(
            Div('obstetric', css_class='hidden'),
            Div('men', css_class='column_ten'),
            Div('Cic', css_class='column_ten'),
            Div('FUM', css_class='column_ten'),
            Div('G', css_class='column_ten'),
            Div('P', css_class='column_ten'),
            Div('A', css_class='column_ten'),
            Div('C', css_class='column_ten'),
            Div('FUP', css_class='column_ten'),
            Div('Menop', css_class='column_ten'),
            css_class='row'),
        Div(
            Div('relatives', css_class='column_one'),
            css_class='row'),
    )

    class Meta(object):
        model = ClinicalHistory
        fields = '__all__'
        widgets = {
            'created_at_date': forms.DateInput(format=('%Y-%m-%d'), attrs={'type': 'date'})
        }


class PhysicalExamForm(ModelForm):

    diagnostics_images_aux = forms.MultipleChoiceField(label='Diagnostico')

    helper = FormHelper()
    helper.form_class = 'form-inline'
    helper.form_tag = False

    helper.layout = Layout(
        Div(
            Div('weight', css_class='column_ten'),
            Div('tall', css_class='column_ten'),
            Div('IM', css_class='column_ten'),
            Div('TA', css_class='column_ten'),
            Div('Fc', css_class='column_ten'),
            Div('minfr', css_class='column_ten'),
            Div('mint', css_class='column_ten'),
            Div('so', css_class='column_ten'),
            Div('pe', css_class='column_ten'),
            Div('pa', css_class='column_ten'),
            css_class='row'),
        Div(
            Div('mental_sphere', css_class='column_one'),
            css_class='row'),
        Div(
            Div('head', css_class='column_one'),
            css_class='row'),
        Div(
            Div('orl', css_class='column_one'),
            css_class='row'),
        Div(
            Div('neck_thyroid', css_class='column_one'),
            css_class='row'),
        Div(
            Div('chest', css_class='column_one'),
            css_class='row'),
        Div(
            Div('cardiovascular', css_class='column_one'),
            css_class='row'),
        Div(
            Div('respiratory', css_class='column_one'),
            css_class='row'),
        Div(
            Div('digestive', css_class='column_one'),
            css_class='row'),
        Div(
            Div('mammary_gland', css_class='column_one'),
            css_class='row'),
        Div(
            Div('genitourinary', css_class='column_one'),
            css_class='row'),
        Div(
            Div('snc_peripheral', css_class='column_one'),
            css_class='row'),
        Div(
            Div('osteomuscular', css_class='column_one'),
            css_class='row'),
        Div(
            Div('skin_faneras', css_class='column_one'),
            css_class='row'),
        Div(
            Div('senses_organs', css_class='column_one'),
            css_class='row'),
        Div(
            Div('diagnostics_images_aux', css_class='column_one'),
            css_class='row'),
    )

    class Meta(object):
        model = PhysicalExam
        fields = ['weight', 'tall', 'IM', 'TA', 'Fc', 'minfr', 'mint', 'so',
                  'pe', 'pa', 'mental_sphere', 'head', 'orl', 'neck_thyroid',
                  'chest', 'cardiovascular', 'respiratory', 'digestive',
                  'mammary_gland', 'genitourinary', 'snc_peripheral',
                  'osteomuscular', 'skin_faneras', 'senses_organs']

    def clean_diagnostics_images(self):
        diagnostics = self.cleaned_data['diagnostics_images']
        return diagnostics


class SystemsReviewForm(ModelForm):
    helper = FormHelper()
    helper.form_class = 'form-inline'
    helper.form_tag = False
    helper.layout = Layout(
        Div(
            Div('skin_faneras', css_class='column_one'),
            css_class='row'),
        Div(
            Div('orl', css_class='column_one'),
            css_class='row'),
        Div(
            Div('respiratory', css_class='column_one'),
            css_class='row'),
        Div(
            Div('cardiovascular', css_class='column_one'),
            css_class='row'),
        Div(
            Div('digestive', css_class='column_one'),
            css_class='row'),
        Div(
            Div('genitourinary', css_class='column_one'),
            css_class='row'),
        Div(
            Div('snc_peripheral', css_class='column_one'),
            css_class='row'),
        Div(
            Div('endocrine', css_class='column_one'),
            css_class='row'),
        Div(
            Div('locomotor', css_class='column_one'),
            css_class='row'),
        Div(
            Div('hematic_lymphatic', css_class='column_one'),
            css_class='row'),
        Div(
            Div('senses_organs', css_class='column_one'),
            css_class='row')
    )

    class Meta(object):
        model = SystemsReview
        fields = '__all__'
