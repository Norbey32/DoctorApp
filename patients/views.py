from .serializers import PatientSerializer, InsuranceSerializer, MedicalRecordSerializer
from .models import Patient, Insurance, MedicalRecord

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView


# GET api/patients/ - Listar todos los pacientes
# POST api/patients/ - Crear un nuevo paciente
# GET api/patients/<pk>/ - Detalle
# PUT api/patients/<pk>/ - Modifiacion
# DELETE api/patients/<pk>/ - Borrar


class ListPatientsView(ListAPIView, CreateAPIView):
    """
    Endpoint para listar pacientes
    """
    allowed_methods = ['GET', 'POST']
    serializer_class = PatientSerializer
    queryset = Patient.objects.all()


class DetailPatientsView(RetrieveUpdateDestroyAPIView):
    allowed_methods = ['GET', 'PUT', 'DELETE']
    serializer_class = PatientSerializer
    queryset = Patient.objects.all()



# GET api/insurance/ - Listar todos seguros
# POST api/insurance/ - Crear un nuevo seguro
# GET api/insurance/<pk>/ - Detalle
# PUT api/insurance/<pk>/ - Modifiacion
# DELETE api/insurance/<pk>/ - Borrar


class ListInsuranceView(ListAPIView, CreateAPIView):
    allowed_methods = ['GET', 'POST']
    serializer_class = InsuranceSerializer
    queryset = Insurance.objects.all()


class DetailInsuranceView(RetrieveUpdateDestroyAPIView):
    allowed_methods = ['GET', 'PUT', 'DELETE']
    serializer_class = InsuranceSerializer
    queryset = Insurance.objects.all()



# GET api/medical-record/ - Listar todos las notas medicas
# POST api/medical-record/ - Crear una nueva nota
# GET api/medical-record/<pk>/ - Detalle
# PUT api/medical-record/<pk>/ - Modifiacion
# DELETE api/medical-record/<pk>/ - Borrar


class ListMedicalRecordView(ListAPIView, CreateAPIView):
    allowed_methods = ['GET', 'POST']
    serializer_class = MedicalRecordSerializer
    queryset = MedicalRecord.objects.all()


class DetailMedicalRecordView(RetrieveUpdateDestroyAPIView):
    allowed_methods = ['GET', 'PUT', 'DELETE']
    serializer_class = MedicalRecordSerializer
    queryset = MedicalRecord.objects.all()
