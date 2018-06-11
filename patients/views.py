# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from dbbackup.storage import Storage
from django.core.management import call_command
from django.core.urlresolvers import reverse
from django.forms.models import model_to_dict
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import ListView
from django.views.generic import UpdateView
from django.views.generic import DetailView
from django.views import View
from django_filters.views import FilterView
from django_tables2 import RequestConfig
from django_tables2.export.views import ExportMixin
from django_tables2.views import SingleTableMixin
from easy_pdf.views import PDFTemplateResponseMixin
from patients.filters import CIE10Filter
from patients.filters import ClinicalHistoryFilter
from patients.filters import MedicineFilter
from patients.filters import ParaclinicalFilter
from patients.filters import PatientFilter
from patients.forms import ClinicalHistoryForm
from patients.forms import MedicalFormulasForm
from patients.forms import MedicalHistoryForm
from patients.forms import PatientForm
from patients.forms import PhysicalExamForm
from patients.forms import SystemsReviewForm
from patients.models import CIE10
from patients.models import MedicalHistory
from patients.models import Medicine
from patients.models import Paraclinical
from patients.models import Patient
from patients.tables import CIE10Table
from patients.tables import ClinicalRecordTable
from patients.tables import MedicineTable
from patients.tables import ParaclinicalTable
from patients.tables import PatientTable


class FilteredPatientListView(ExportMixin, SingleTableMixin, FilterView):
    table_class = PatientTable
    model = Patient
    template_name = 'patients/patient_list.html'
    paginate_by = 5
    filterset_class = PatientFilter


class CreatePatientView(CreateView):

    model = Patient
    template_name = 'patients/patient_form.html'
    fields = '__all__'
    success_url = reverse_lazy('patients-list')


class DeletePatientView(DeleteView):

    model = Patient
    template_name = 'patients/patient_delete.html'
    success_url = reverse_lazy('patients-list')


class UpdatePatientView(UpdateView):

    model = Patient
    template_name = 'patients/patient_update.html'
    fields = '__all__'
    success_url = reverse_lazy('patients-list')


class FilteredMedicineListView(ExportMixin, SingleTableMixin, FilterView):
    table_class = MedicineTable
    model = Medicine
    template_name = 'patients/medicine_list.html'
    paginate_by = 10
    filterset_class = MedicineFilter
    export_formats = ('xls', 'csv')


class CreateMedicineView(CreateView):

    model = Medicine
    template_name = 'patients/medicine_form.html'
    fields = '__all__'
    success_url = reverse_lazy('medicines-list')


class DeleteMedicineView(DeleteView):

    model = Medicine
    template_name = 'patients/medicine_delete.html'
    success_url = reverse_lazy('medicines-list')


class UpdateMedicineView(UpdateView):

    model = Medicine
    template_name = 'patients/medicine_update.html'
    fields = '__all__'
    success_url = reverse_lazy('medicines-list')


class FilteredParaclinicalListView(ExportMixin, SingleTableMixin, FilterView):

    table_class = ParaclinicalTable
    model = Paraclinical
    template_name = 'patients/paraclinical_list.html'
    paginate_by = 10
    filterset_class = ParaclinicalFilter


class CreateParaclinicalView(CreateView):

    model = Paraclinical
    template_name = 'patients/paraclinical_form.html'
    fields = ['name']
    success_url = reverse_lazy('paraclinicals-list')


class UpdateParaclinicalView(UpdateView):

    model = Paraclinical
    template_name = 'patients/paraclinical_update.html'
    fields = ['name']
    success_url = reverse_lazy('paraclinicals-list')


class DeleteParaclinicalView(DeleteView):

    model = Paraclinical
    template_name = 'patients/paraclinical_delete.html'
    success_url = reverse_lazy('paraclinicals-list')


class FilteredCie10ListView(ExportMixin, SingleTableMixin, FilterView):
    table_class = CIE10Table
    model = CIE10
    template_name = 'patients/cie10_list.html'
    paginate_by = 5
    filterset_class = CIE10Filter


class CreateCie10View(CreateView):

    model = CIE10
    template_name = 'patients/cie10_form.html'
    fields = '__all__'
    success_url = reverse_lazy('cie10-list')


class DeleteCie10View(DeleteView):

    model = CIE10
    template_name = 'patients/cie10_delete.html'
    success_url = reverse_lazy('cie10-list')


class UpdateCie10View(UpdateView):

    model = CIE10
    template_name = 'patients/cie10_update.html'
    fields = '__all__'
    success_url = reverse_lazy('cie10-list')


class FilteredMedicalHistoryListView(SingleTableMixin, FilterView):
    table_class = ClinicalRecordTable
    model = MedicalHistory
    template_name = 'patients/clinical_history_list.html'
    paginate_by = 10
    filterset_class = ClinicalHistoryFilter

    def get(self, request):
        filterset_class = self.get_filterset_class()
        self.filterset = self.get_filterset(filterset_class)
        if 'diagnostic' in request.GET:
            form_filter = self.filterset.form
            id_cie10s = request.GET.getlist('diagnostic')
            cie10s = CIE10.objects.filter(pk__in=id_cie10s)
            cie10s = list(cie10s)
            form_filter.fields['diagnostic'].choices = [
                (cie10.pk, cie10.name) for cie10 in cie10s]
            form_filter.fields['diagnostic'].initial = [
                cie10.pk for cie10 in cie10s]
        self.object_list = self.filterset.qs

        context = self.get_context_data(filter=self.filterset,
                                        object_list=self.object_list)
        return self.render_to_response(context)


class CreateMedicalHistoryView(View):
    template_name = 'patients/clinical_history_form.html'

    def get(self, request, pk):
        patient = Patient.objects.get(pk=pk)
        current_history = MedicalHistory.objects.filter(patient_id=pk).last()
        if current_history == None:
            context = {
                'patient': PatientForm(initial=model_to_dict(patient)),
                'physical_exam': PhysicalExamForm(),
                'systems_review': SystemsReviewForm(),
                'clinical_history': ClinicalHistoryForm(),
                'medical_formulas': MedicalFormulasForm(),
                'general': MedicalHistoryForm()
            }
        else:
            cie10s = current_history.physical_exam.diagnostics_images.all()
            form_physical_exam = PhysicalExamForm(
                initial=model_to_dict(current_history.physical_exam))
            form_physical_exam.fields['diagnostics_images_aux'].choices = [
                (cie10.pk, cie10.name) for cie10 in cie10s]
            form_physical_exam.fields['diagnostics_images_aux'].initial = [
                cie10.pk for cie10 in cie10s]
            context = {
                'patient': PatientForm(initial=model_to_dict(patient)),
                'physical_exam': form_physical_exam,
                'systems_review': SystemsReviewForm(initial=model_to_dict(current_history.systems_review)),
                'clinical_history': ClinicalHistoryForm(initial=model_to_dict(current_history.clinical_history)),
                'medical_formulas': MedicalFormulasForm(initial=model_to_dict(current_history.formulas)),
                'general': MedicalHistoryForm(initial=model_to_dict(current_history))
            }
        return render(request, self.template_name, context)

    def post(self, request, pk):
        id_medicines = self.request.POST.getlist('medicines')
        medicines = Medicine.objects.filter(pk__in=id_medicines)
        medicines = list(medicines)

        id_paraclinicals = self.request.POST.getlist('paraclinicals')
        paraclinicals = Paraclinical.objects.filter(pk__in=id_paraclinicals)
        paraclinicals = list(paraclinicals)

        id_cie10s = self.request.POST.getlist('diagnostics_images_aux')
        cie10s = CIE10.objects.filter(pk__in=id_cie10s)
        cie10s = list(cie10s)

        form_physical_exam = PhysicalExamForm(self.request.POST)
        form_physical_exam.fields['diagnostics_images_aux'].choices = [
            (cie10.pk, cie10.name) for cie10 in cie10s]
        form_systems_review = SystemsReviewForm(self.request.POST)
        form_clinical_history = ClinicalHistoryForm(self.request.POST)
        form_medical_formulas = MedicalFormulasForm(self.request.POST)

        if (form_physical_exam.is_valid()
            and form_systems_review.is_valid()
                and form_clinical_history.is_valid()
                and form_medical_formulas.is_valid()):
            form_general = MedicalHistoryForm(self.request.POST)
            if form_general.is_valid():
                general = form_general.save(commit=False)
                general.patient = Patient.objects.get(pk=pk)
                general.physical_exam = form_physical_exam.save()
                general.systems_review = form_systems_review.save()
                general.clinical_history = form_clinical_history.save()
                general.formulas = form_medical_formulas.save()
                general.save()
                general.physical_exam.diagnostics_images.add(*cie10s)
                general.formulas.medicines.add(*medicines)
                general.formulas.paraclinicals.add(*paraclinicals)
        return HttpResponseRedirect(reverse('patients-list'))


class DetailMedicalHistoryView(DetailView):
    model = MedicalHistory
    template_name = 'patients/clinical_history_detail.html'

    def get_context_data(self, **kwargs):
        medical_history = kwargs['object']
        context = super(DetailView, self).get_context_data(
            title="Historia clínica", **kwargs)

        cie10s = medical_history.physical_exam.diagnostics_images.all()
        form_physical_exam = PhysicalExamForm(
            initial=model_to_dict(medical_history.physical_exam))
        form_physical_exam.fields['diagnostics_images_aux'].choices = [
            (cie10.pk, cie10.name) for cie10 in cie10s]
        form_physical_exam.fields['diagnostics_images_aux'].initial = [
            cie10.pk for cie10 in cie10s]
        context['forms'] = {
            'patient': PatientForm(initial=model_to_dict(medical_history.patient)),
            'physical': form_physical_exam,
            'systems': SystemsReviewForm(initial=model_to_dict(medical_history.systems_review)),
            'clinical': ClinicalHistoryForm(initial=model_to_dict(medical_history.clinical_history)),
            'general': MedicalHistoryForm(initial=model_to_dict(medical_history)),
            'formulas': MedicalFormulasForm(initial=model_to_dict(medical_history.formulas))
        }
        return context


class PDFDetailMedicalHistoryView(PDFTemplateResponseMixin, DetailView):
    model = MedicalHistory
    template_name = 'patients/report.pdf'

    def get_context_data(self, **kwargs):
        medical_history = kwargs['object']
        context = super(DetailView, self).get_context_data(
            title="Historia clínica", **kwargs)
        context['forms'] = {
            'patient_pdf': model_to_dict(medical_history.patient),
            'general_pdf': model_to_dict(medical_history),
            'clinical_pdf': model_to_dict(medical_history.clinical_history),
            'systems_pdf': model_to_dict(medical_history.systems_review),
            'physical_pdf': model_to_dict(medical_history.physical_exam),
            'formulas_pdf': model_to_dict(medical_history.formulas)
        }
        return context


class BackUpListView(View):

    storage = Storage()
    template_name = 'patients/backup_list.html'

    def get(self, request):
        context = {'table': self.storage.list_backups()}
        return render(request, self.template_name, context)


class BackUpAddView(View):

    def get(self, request):
        call_command('dbbackup', '--compress')
        return HttpResponseRedirect(reverse('backups-list'))


class BackUpRestoreView(View):

    template_name = 'patients/backup_restore.html'

    def get(self, request, file_name):
        context = {'object': file_name}
        return render(request, self.template_name, context)

    def post(self, request, file_name):
        call_command('dbrestore', '--noinput', '--uncompress', i=file_name)
        return HttpResponseRedirect(reverse('backups-list'))


class BackUpDeleteView(View):

    storage = Storage()
    template_name = 'patients/backup_delete.html'

    def get(self, request, file_name):
        context = {'object': file_name}
        return render(request, self.template_name, context)

    def post(self, request, file_name):
        self.storage.delete_file(file_name)
        return HttpResponseRedirect(reverse('backups-list'))


class BackupImport(View):

    storage = Storage()
    template_name = 'patients/backup_import.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        backup_file = request.FILES['name']
        self.storage.write_file(backup_file, backup_file.name)
        return HttpResponseRedirect(reverse('backups-list'))


class Index(View):
    template_name = "index.html"

    def get(self, request):
        context = {}
        context["patients"] = Patient.objects.all().count()
        context["medicines"] = Medicine.objects.all().count()
        context["paraclinicals"] = Paraclinical.objects.all().count()
        context["clinical_histories"] = MedicalHistory.objects.all().count()
        context["cie10s"] = CIE10.objects.all().count()
        return render(request, self.template_name, context)
