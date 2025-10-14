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
    allowed_methods = ['GET', 'POST']
    serializer_class = PatientSerializer
    queryset = Patient.objects.all()


class DetailPatientsView(RetrieveUpdateDestroyAPIView):
    allowed_methods = ['GET', 'PUT', 'DELETE']
    serializer_class = PatientSerializer
    queryset = Patient.objects.all()



# GET api/insurance/ - Listar todos los pacientes
# POST api/insurance/ - Crear un nuevo paciente
# GET api/insurance/<pk>/ - Detalle
# PUT api/insurance/<pk>/ - Modifiacion
# DELETE api/insurance/<pk>/ - Borrar


@api_view(['GET', 'POST'])
def list_insurance(request):
    if request.method == 'GET':
        insurances = Insurance.objects.all()
        serializer = InsuranceSerializer(insurances, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = InsuranceSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def detail_insurance(request, pk):
    try:
        insurance = Insurance.objects.get(id=pk)
    except Insurance.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = InsuranceSerializer(insurance)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = InsuranceSerializer(insurance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    if request.method == 'DELETE':
        insurance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# GET api/medical-record/ - Listar todos los pacientes
# POST api/medical-record/ - Crear un nuevo paciente
# GET api/medical-record/<pk>/ - Detalle
# PUT api/medical-record/<pk>/ - Modifiacion
# DELETE api/medical-record/<pk>/ - Borrar


@api_view(['GET', 'POST'])
def list_medical_record(request):
    if request.method == 'GET':
        medical_records = MedicalRecord.objects.all()
        serializer = MedicalRecordSerializer(medical_records, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = MedicalRecordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def detail_medical_record(request, pk):
    try:
        medical_record = MedicalRecord.objects.get(id=pk)
    except MedicalRecord.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = MedicalRecordSerializer(medical_record)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = MedicalRecordSerializer(medical_record, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    if request.method == 'DELETE':
        medical_record.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
