from django.urls import path
from . import views
from .api import (
    DoctorListAPI, DoctorDetailAPI,
    PatientListAPI, PatientDetailAPI,
    MedicalRecordListAPI, MedicalRecordDetailAPI
)

app_name = 'myapp'

urlpatterns = [
    # URLs for doctors
    path('doctors/', views.DoctorList.as_view(), name='doctor_list'),
    path('doctors/<int:pk>/', views.DoctorDetail.as_view(), name='doctor_detail'),
    path('doctors/new/', views.DoctorCreate.as_view(), name='doctor_new'),
    path('doctors/<int:pk>/edit/', views.DoctorUpdate.as_view(), name='doctor_edit'),
    path('doctors/<int:pk>/delete/', views.DoctorDelete.as_view(), name='doctor_delete'),

    # URLs for patients
    path('patients/', views.PatientList.as_view(), name='patient_list'),
    path('patients/<int:pk>/', views.PatientDetail.as_view(), name='patient_detail'),
    path('patients/new/', views.PatientCreate.as_view(), name='patient_new'),
    path('patients/<int:pk>/edit/', views.PatientUpdate.as_view(), name='patient_edit'),
    path('patients/<int:pk>/delete/', views.PatientDelete.as_view(), name='patient_delete'),

    # URLs for medical records
    path('records/new/<int:patient_pk>/', views.MedicalRecordCreate.as_view(), name='medical_record_new'),
    path('records/<int:pk>/edit/', views.MedicalRecordUpdate.as_view(), name='medical_record_edit'),
    path('records/<int:pk>/delete/', views.MedicalRecordDelete.as_view(), name='medical_record_delete'),

    # API
    path('api/doctors/', DoctorListAPI.as_view(), name='doctor-list-api'),
    path('api/doctors/<int:pk>/', DoctorDetailAPI.as_view(), name='doctor-detail-api'),
    path('api/patients/', PatientListAPI.as_view(), name='patient-list-api'),
    path('api/patients/<int:pk>/', PatientDetailAPI.as_view(), name='patient-detail-api'),
    path('api/medical-records/', MedicalRecordListAPI.as_view(), name='medical-record-list-api'),
    path('api/medical-records/<int:pk>/', MedicalRecordDetailAPI.as_view(), name='medical-record-detail-api'),

]





