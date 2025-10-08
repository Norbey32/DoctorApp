from django.urls import path
from .views import list_bookings, detail_bookings, list_medical_note, detail_medical_note

urlpatterns = [
    path('bookings/', list_bookings),
    path('bookings/<int:pk>/', detail_bookings),
    path('medical-note/', list_medical_note),
    path('medical-note/<int:pk>/', detail_medical_note),

]