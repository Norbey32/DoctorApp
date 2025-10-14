from django.urls import path
from patients.views import (
    ListPatientsView, DetailPatientsView, 
    list_insurance, detail_insurance,
    list_medical_record, detail_medical_record
)

urlpatterns = [
    path('patients/', ListPatientsView.as_view()),
    path('patients/<int:pk>/', DetailPatientsView.as_view()),
    path('insurance/', list_insurance),
    path('insurance/<int:pk>/', detail_insurance),
    path('medical-record/', list_medical_record),
    path('medical-record/<int:pk>/', detail_medical_record),
]