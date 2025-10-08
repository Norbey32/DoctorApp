from django.urls import path

from .views import list_doctors, detail_doctor, list_department, detal_department


urlpatterns = [
    path('doctors/', list_doctors),
    path('doctors/<int:pk>/', detail_doctor),
    path('department/', list_department),
    path('department/<pk>/', detal_department)
]