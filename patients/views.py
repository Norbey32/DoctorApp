from .serializers import PatientSerializer
from .models import Patient

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


# GET api/patients/ - Listar todos los pacientes
# POST api/patients/ - Crear un nuevo paciente
# GET api/patients/<pk> - Detalle
# PUT api/patients/<pk> - Modifiacion


@api_view(['GET', 'POST'])
def list_patients(request):
    if request.method == 'GET':
        patients = Patient.objects.all()
        serializer = PatientSerializer(patients, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = PatientSerializer(data=request.data)
        serializer.is_valid(raise_exeption=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT'])
def detail_patient(request, pk):
    if request.method == 'GET':
        try:
            patient = Patient.objects.get(id=pk)
        except Patient.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = PatientSerializer(patients)
        return Response(serializer.data)


        