from rest_framework import viewsets

from .serializers import (
    DoctorSerializer, DepartmentSerializer,
    DoctorAvailabilitySerializer, MedicalNoteSerializer
)
from .models import Doctor, Department, DoctorAvailability, MedicalNote


class DoctorViewSets(viewsets.ModelViewSet):
    serializer_class = DoctorSerializer
    queryset = Doctor.objects.all()


class DepartmentViewSets(viewsets.ModelViewSet):
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()


class DoctorAvailabilityViewSets(viewsets.ModelViewSet):
    serializer_class = DoctorAvailabilitySerializer
    queryset = DoctorAvailability.objects.all()


class MedicalNoteViewSets(viewsets.ModelViewSet):
    serializer_class = MedicalNoteSerializer
    queryset = MedicalNote.objects.all()