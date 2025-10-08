from django.urls import path

from .views import (
    list_doctors, detail_doctor, 
    list_department, detal_department, 
    list_doctor_availability, detail_doctor_availability,
    list_medical_note, detail_medical_note
)


urlpatterns = [
    path('doctors/', list_doctors),
    path('doctors/<int:pk>/', detail_doctor),
    path('department/', list_department),
    path('department/<int:pk>/', detal_department),
    path('doctor-availability/', list_doctor_availability),
    path('doctor-availability/<int:pk>/', detail_doctor_availability),
    path('note-medical/', list_medical_note),
    path('note-medical/<int:pk>', detail_medical_note),
]