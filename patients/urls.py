"""
patients URL Configuration
"""

from django.conf.urls import url
from patients import api
from patients import views

urlpatterns = [
    url(r'^patient/list$', views.FilteredPatientListView.as_view(),
        name='patients-list'),
    url(r'^patient/add$', views.CreatePatientView.as_view(), name='patients-add'),
    url(r'^patient/delete/(?P<pk>\d+)$',
        views.DeletePatientView.as_view(), name='patients-delete'),
    url(r'^patient/update/(?P<pk>\d+)$',
        views.UpdatePatientView.as_view(), name='patients-update'),
    url(r'^patient/medicalrecord/(?P<pk>\d+)$',
        views.CreateMedicalHistoryView.as_view(), name='patients-medical-record'),
    url(r'^cie10/list$', views.FilteredCie10ListView.as_view(),
        name='cie10-list'),
    url(r'^cie10/add$', views.CreateCie10View.as_view(), name='cie10-add'),
    url(r'^cie10/update/(?P<pk>\d+)$',
        views.UpdateCie10View.as_view(), name='cie10-update'),
    url(r'^cie10/delete/(?P<pk>\d+)$',
        views.DeleteCie10View.as_view(), name='cie10-delete'),
    url(r'^cie10/search$',
        api.SearchInCIE10.as_view(), name='cie10-search'),
    url(r'^medicine/list$', views.FilteredMedicineListView.as_view(),
        name='medicines-list'),
    url(r'^medicine/add$', views.CreateMedicineView.as_view(), name='medicines-add'),
    url(r'^medicine/update/(?P<pk>\d+)$',
        views.UpdateMedicineView.as_view(), name='medicines-update'),
    url(r'^medicine/delete/(?P<pk>\d+)$',
        views.DeleteMedicineView.as_view(), name='medicines-delete'),
    url(r'^paraclinical/list$', views.FilteredParaclinicalListView.as_view(),
        name='paraclinicals-list'),
    url(r'^paraclinical/add$', views.CreateParaclinicalView.as_view(),
        name='paraclinicals-add'),
    url(r'^paraclinical/update/(?P<pk>\d+)$',
        views.UpdateParaclinicalView.as_view(), name='paraclinicals-update'),
    url(r'^paraclinical/delete/(?P<pk>\d+)$',
        views.DeleteParaclinicalView.as_view(), name='paraclinicals-delete'),
    url(r'^medical_record/list$', views.FilteredMedicalHistoryListView.as_view(),
        name='medical-record-list'),
    url(r'^medical_record/detail/(?P<pk>\d+)$',
        views.DetailMedicalHistoryView.as_view(), name='medical-record-detail'),
    url(r'^medical_record/pdf/(?P<pk>\d+)$',
        views.PDFDetailMedicalHistoryView.as_view(), name='medical-record-pdf'),
    url(r'^backup/list$', views.BackUpListView.as_view(), name='backups-list'),
    url(r'^backup/add$', views.BackUpAddView.as_view(), name='backups-add'),
    url(r'^backup/restore/(?P<file_name>.*)/$',
        views.BackUpRestoreView.as_view(), name='backups-restore'),
    url(r'^backup/delete/(?P<file_name>.*)/$',
        views.BackUpDeleteView.as_view(), name='backups-delete'),
    url(r'^backup/import$', views.BackupImport.as_view(), name='backups-import')
]
