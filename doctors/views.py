from .serializers import DoctorSerializer, DepartmentSerializer 
from .models import Doctor, Department, DoctorAvailability

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


@api_view(['GET', 'PUT', 'DELETE'])
def detail_doctor(request, pk):
    try:
        doctor = Doctor.objects.get(id=pk)
    except Doctor.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer =  DoctorSerializer(doctor)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer =  DoctorSerializer(doctor, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    if request.method == 'DELETE':
        doctor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# GET api/department/ - Listar todos los departamentos
# POST api/department/ - Crear un nuevo departamento
# GET api/department/<pk>/ - Detalle
# PUT api/department/<pk>/ - Modifiacion
# DELETE api/department/<pk>/ - Borrar


@api_view(['GET', 'POST'])
def list_department(request):
    if request.method == 'GET':
        departments = Department.objects.all()
        serializer = DepartmentSerializer(departments, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = DepartmentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def detal_department(request, pk):
    try:
        department = Department.objects.get(id=pk)
    except Department.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DepartmentSerializer(department)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = DepartmentSerializer(department, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    if request.method == 'DELETE':
        department.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# GET api/department/ - Listar todos los departamentos
# POST api/department/ - Crear un nuevo departamento
# GET api/department/<pk>/ - Detalle
# PUT api/department/<pk>/ - Modifiacion
# DELETE api/department/<pk>/ - Borrar