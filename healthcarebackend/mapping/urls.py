from django.urls import path
from .views import PatientDoctorMappingListCreate, PatientDoctorMappingDetail, PatientDoctorMappingByPatient

urlpatterns = [
    path('mappings/', PatientDoctorMappingListCreate.as_view(), name='mapping-list-create'),
    path('mappings/<int:pk>/', PatientDoctorMappingDetail.as_view(), name='mapping-detail'),
    path('mappings/patient/<int:patient_id>/', PatientDoctorMappingByPatient.as_view(), name='mappings-by-patient'),
]
