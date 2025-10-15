from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

from .serializers import PatientSerializer, InsuranceSerializer, MedicalRecordSerializer
from .models import Patient, Insurance, MedicalRecord


class PatientsViewSets(viewsets.ModelViewSet):
    serializer_class = PatientSerializer
    queryset = queryset = Patient.objects.all()

    @action(['GET'], detail=True, url_path='medical-history')
    def medical_history(self, request, pk):
        patient = self.get_object()
        history_content = patient.medical_history
        report_data = {
            "patient_id": patient.pk,
            "full_name": f"{patient.first_name} {patient.last_name}",
            "medical_history_report": history_content
        }
        return Response(report_data, status=status.HTTP_200_OK)



class InsuranceViewSets(viewsets.ModelViewSet):
    serializer_class = InsuranceSerializer
    queryset = Insurance.objects.all()


class MedicalRecordViewSets(viewsets.ModelViewSet):
    serializer_class = MedicalRecordSerializer
    queryset = MedicalRecord.objects.all()