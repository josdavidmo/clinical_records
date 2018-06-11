# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.management import call_command
from django.db import models
from django.utils import timezone
from StringIO import StringIO


class Generic(models.Model):
    """
    Abstract generic
    """

    url_options = [{"name": "update", "ico": "fas fa-pencil-alt"},
                   {"name": "delete", "ico": "fas fa-trash-alt"}]

    class Meta:
        abstract = True
        ordering = ['pk']


class DocumentType(models.Model):
    """
    table for document_types.
    """

    name = models.CharField(max_length=20)

    def __unicode__(self):
        return "%s" % (self.name)


class Gender(models.Model):
    """
    table for gender.
    """

    name = models.CharField(max_length=20)

    def __unicode__(self):
        return "%s" % (self.name)


class Patient(Generic):
    """
    table for patient.
    """

    url_options = Generic.url_options + \
        [{"name": "medicalrecord", "ico": "far fa-clipboard"}]

    names = models.CharField(
        max_length=100, verbose_name="Nombres", default="")
    last_names = models.CharField(
        max_length=100, verbose_name="Apellidos", default="")
    gender = models.ForeignKey(Gender, verbose_name="Género")
    birth_date = models.DateField(verbose_name="Fecha de Nacimiento")
    birth_city = models.CharField(null=True, blank=True,
                                  max_length=70, verbose_name="Ciudad de Nacimiento")
    address = models.CharField(max_length=100, verbose_name="Dirección")
    phone = models.CharField(max_length=50, verbose_name="Teléfono")
    email = models.EmailField(null=True, blank=True,
                              verbose_name="Correo Electronico")
    scholarship = models.CharField(
        null=True, blank=True, max_length=100, verbose_name="Nivel de escolaridad")
    profesion = models.CharField(
        null=True, blank=True, max_length=50, verbose_name="Profesión/ocupación")
    civil_status = models.CharField(
        null=True, blank=True, max_length=50, verbose_name="Estado civil")
    origin = models.CharField(null=True, blank=True,
                              max_length=50, verbose_name="Procedencia")
    document = models.CharField(
        unique=True, db_index=True, max_length=20, verbose_name="Documento")
    document_type = models.ForeignKey(
        DocumentType, verbose_name="Tipo")

    def get_full_name(self):
        return "%s %s" % (self.names, self.last_names)

    def __unicode__(self):
        return "%s %s, con %s %s" % (self.names, self.last_names,
                                     self.document_type, self.document)


class MedicineType(models.Model):
    """
    table for type medicine.
    """

    name = models.CharField(max_length=50, verbose_name="Tipo Medicina")

    def __unicode__(self):
        return "%s" % (self.name)


class Medicine(Generic):
    """
    table for medicine.
    """

    name = models.CharField(max_length=50, verbose_name="Nombre")
    medicine_type = models.ForeignKey(
        MedicineType, verbose_name="Tipo Medicina", null=True, blank=True)

    def __unicode__(self):
        return "%s" % (self.name)


class CIE10(Generic):
    """
    table for CIE10.
    """

    code = models.CharField(max_length=20, db_index=True, verbose_name="Código")
    name = models.CharField(max_length=500, verbose_name="Nombre")

    def __unicode__(self):
        return "%s %s" % (self.code, self.name)


class ClinicalHistory(Generic):
    """
    table for clinical history.
    """

    pathological = models.TextField(
        null=True, blank=True, verbose_name="Patológicos")
    surgical = models.TextField(
        null=True, blank=True, verbose_name="Quirúrgicos")
    traumatic = models.TextField(
        null=True, blank=True, verbose_name="Traumáticos")
    poisoning = models.TextField(
        null=True, blank=True, verbose_name="Intoxicaciones")
    smoking = models.TextField(
        null=True, blank=True, verbose_name="Tabaquismo")
    liqueur = models.TextField(null=True, blank=True, verbose_name="Licor")
    psychoactive = models.TextField(
        null=True, blank=True, verbose_name="Psicoactivos")
    permanent_medication = models.TextField(
        null=True, blank=True, verbose_name="Medicamentos permanentes")
    allergic = models.TextField(
        null=True, blank=True, verbose_name="Alérgicos")
    immunological = models.TextField(
        null=True, blank=True, verbose_name="Inmunológicos")
    transfusions = models.TextField(
        null=True, blank=True, verbose_name="Transfusiones")
    obstetric = models.TextField(
        null=True, blank=True, verbose_name="Obstétricos")
    men = models.CharField(null=True, blank=True,
                           max_length=20, verbose_name="Men")
    Cic = models.CharField(null=True, blank=True,
                           max_length=20, verbose_name="Cic")
    FUM = models.CharField(null=True, blank=True,
                           max_length=20, verbose_name="FUM")
    G = models.CharField(null=True, blank=True,
                         max_length=20, verbose_name="G")
    P = models.CharField(null=True, blank=True,
                         max_length=20, verbose_name="P")
    A = models.CharField(null=True, blank=True,
                         max_length=20, verbose_name="A")
    C = models.CharField(null=True, blank=True,
                         max_length=20, verbose_name="C")
    FUP = models.CharField(null=True, blank=True,
                           max_length=20, verbose_name="FUP")
    Menop = models.CharField(null=True, blank=True,
                             max_length=20, verbose_name="Menop")
    relatives = models.TextField(
        null=True, blank=True, verbose_name="Familiares")

    def __unicode__(self):
        return "%s" % (self.id)


class SystemsReview(models.Model):
    """
    table for systems review.
    """

    skin_faneras = models.TextField(
        null=True, blank=True, verbose_name="Piel y Faneras")
    orl = models.TextField(null=True, blank=True, verbose_name="O.R.L")
    respiratory = models.TextField(
        null=True, blank=True, verbose_name="Respiratorio")
    cardiovascular = models.TextField(
        null=True, blank=True, verbose_name="Cardio-vascular")
    digestive = models.TextField(
        null=True, blank=True, verbose_name="Digestivo")
    genitourinary = models.TextField(
        null=True, blank=True, verbose_name="Genito-urinario")
    snc_peripheral = models.TextField(
        null=True, blank=True, verbose_name="SNC y Periferico")
    endocrine = models.TextField(
        null=True, blank=True, verbose_name="Endocrino")
    locomotor = models.TextField(
        null=True, blank=True, verbose_name="Locomotor")
    hematic_lymphatic = models.TextField(
        null=True, blank=True, verbose_name="Hemático y Linfático")
    senses_organs = models.TextField(
        null=True, blank=True, verbose_name="Organos de los Sentidos")

    def __unicode__(self):
        return "%s" % (self.id)


class PhysicalExam(models.Model):
    """
    table for physical exam.
    """

    weight = models.TextField(null=True, blank=True, verbose_name="Peso")
    tall = models.CharField(null=True, blank=True,
                            max_length=50, verbose_name="Talla")
    IM = models.CharField(null=True, blank=True,
                          max_length=50, verbose_name="I.M.C")
    TA = models.CharField(null=True, blank=True,
                          max_length=50, verbose_name="TA")
    Fc = models.CharField(null=True, blank=True,
                          max_length=50, verbose_name="Fc")
    minfr = models.CharField(null=True, blank=True,
                             max_length=50, verbose_name="/min.Fr")
    mint = models.CharField(null=True, blank=True,
                            max_length=50, verbose_name="/min.T")
    so = models.CharField(null=True, blank=True,
                          max_length=50, verbose_name="SPO2")
    pe = models.CharField(null=True, blank=True,
                          max_length=50, verbose_name="PC")
    pa = models.CharField(null=True, blank=True,
                          max_length=50, verbose_name="PA")
    mental_sphere = models.TextField(
        null=True, blank=True, verbose_name="Esfera mental")
    head = models.TextField(null=True, blank=True, verbose_name="Cabeza")
    orl = models.TextField(null=True, blank=True, verbose_name="O.R.L")
    neck_thyroid = models.TextField(
        null=True, blank=True, verbose_name="Cuello - Tiroides")
    chest = models.TextField(null=True, blank=True, verbose_name="Tórax")
    cardiovascular = models.TextField(
        null=True, blank=True, verbose_name="Cardiovascular")
    respiratory = models.TextField(
        null=True, blank=True, verbose_name="Respiratorio")
    digestive = models.TextField(
        null=True, blank=True, verbose_name="Digestivo")
    mammary_gland = models.TextField(
        null=True, blank=True, verbose_name="Mamas")
    genitourinary = models.TextField(
        null=True, blank=True, verbose_name="Genito-urinario")
    snc_peripheral = models.TextField(
        null=True, blank=True, verbose_name="SNC y Periferico")
    osteomuscular = models.TextField(
        null=True, blank=True, verbose_name="Muscular y osteoarticular")
    skin_faneras = models.TextField(
        null=True, blank=True, verbose_name="Piel y Faneras")
    senses_organs = models.TextField(
        null=True, blank=True, verbose_name="Organos de los sentidos")
    diagnostics_images =  models.ManyToManyField(
        CIE10, verbose_name="Diagnóstico", blank=True)

    def __unicode__(self):
        return "%s" % (self.id)


class Paraclinical(Generic):
    """
    table for paraclinical.
    """

    name = models.CharField(max_length=50, verbose_name="Nombre")

    def __unicode__(self):
        return "%s" % (self.name)


class MedicalFormulas(models.Model):
    """
    table for medical formulas.
    """

    medicines = models.ManyToManyField(
        Medicine, verbose_name="Medicamentos", blank=True)
    paraclinicals = models.ManyToManyField(
        Paraclinical, verbose_name="Paraclínicos", blank=True)
    remission = models.TextField(
        null=True, blank=True, verbose_name="Remisión")
    conduct = models.TextField(null=True, blank=True, verbose_name="Conducta")


class MedicalHistory(Generic):
    """
    table for medical history.
    """

    url_options = [{"name": "detail", "ico": "fas fa-eye"},
                   {"name": "pdf", "ico": "fas fa-print"}]
    created_at_date = models.DateField(
        verbose_name="Fecha", default=timezone.now)
    created_at_hour = models.TimeField(
        verbose_name="Hora", default=timezone.now)
    patient = models.ForeignKey(Patient, verbose_name="Paciente")
    companion = models.CharField(
        null=True, blank=True, max_length=50, verbose_name="Acompañante")
    phone_companion = models.CharField(
        null=True, blank=True, max_length=50, verbose_name="Teléfono del acompañante")
    referred_by = models.CharField(
        null=True, blank=True, max_length=50, verbose_name="Referido por")
    reason_consultation = models.TextField(verbose_name="Motivo de consulta")
    current_illness = models.TextField(
        null=True, blank=True, verbose_name="Enfermedad actual")
    clinical_history = models.ForeignKey(ClinicalHistory, blank=True)
    systems_review = models.ForeignKey(SystemsReview, blank=True)
    physical_exam = models.ForeignKey(PhysicalExam, blank=True)
    formulas = models.ForeignKey(MedicalFormulas, blank=True, null=True)
    sgss = models.CharField(null=True, blank=True,
                            max_length=50, verbose_name="SGSS")

    def __unicode__(self):
        return "%s %s %s %s" % (self.id, self.created_at_date, self.created_at_hour, self.patient)

    def get_full_date(self):
        return "%s %s" % (self.created_at_date, self.created_at_hour)
