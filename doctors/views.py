from .serializers import DoctorSerializer
from .models import Doctor

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


# GET api/doctors/ - Listar todos los doctores
# POST api/doctors/ - Crear un nuevo doctor
# GET api/doctors/<pk>/ - Detalle
# PUT api/doctors/<pk>/ - Modifiacion
# DELETE api/doctors/<pk>/ - Borrar


@api_view(['GET', 'POST'])
def list_doctors(request):
    if request.method == 'GET':
        doctors = Doctor.objects.all()
        serializer =  DoctorSerializer(doctors, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer =  DoctorSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

