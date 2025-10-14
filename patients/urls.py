from django.urls import path
from patients.views import (
    ListPatientsView, DetailPatientsView, 
    ListInsuranceView, DetailInsuranceView,
    ListMedicalRecordView, DetailMedicalRecordView
)

urlpatterns = [
    path('patients/', ListPatientsView.as_view()),
    path('patients/<int:pk>/', DetailPatientsView.as_view()),
    path('insurance/', ListInsuranceView.as_view()),
    path('insurance/<int:pk>/', DetailInsuranceView.as_view()),
    path('medical-record/', ListMedicalRecordView.as_view()),
    path('medical-record/<int:pk>/', DetailMedicalRecordView.as_view()),
]