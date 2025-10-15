from rest_framework import viewsets

from .serializers import PatientSerializer, InsuranceSerializer, MedicalRecordSerializer
from .models import Patient, Insurance, MedicalRecord


class PatientsViewSets(viewsets.ModelViewSet):
    serializer_class = PatientSerializer
    queryset = queryset = Patient.objects.all()


class InsuranceViewSets(viewsets.ModelViewSet):
    serializer_class = InsuranceSerializer
    queryset = Insurance.objects.all()


class MedicalRecordViewSets(viewsets.ModelViewSet):
    serializer_class = MedicalRecordSerializer
    queryset = MedicalRecord.objects.all()