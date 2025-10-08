from .serializers import DoctorSerializer, DepartmentSerializer, DoctorAvailabilitySerializer, MedicalNoteSerializer
from .models import Doctor, Department, DoctorAvailability, MedicalNote

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


# GET api/doctor-availability/ - Listar todos los medicos
# POST api/doctor-availability/ - Crear una nueva disponibilidad de medicos
# GET api/doctor-availability/<pk>/ - Detalle
# PUT api/doctor-availability/<pk>/ - Modifiacion
# DELETE api/doctor-availability/<pk>/ - Borrar


@api_view(['GET', 'POST'])
def list_doctor_availability(request):
    if request.method == 'GET':
        doctor_availabilitys = DoctorAvailability.objects.all()
        serializer = DoctorAvailabilitySerializer(doctor_availabilitys, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = DoctorAvailabilitySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def detail_doctor_availability(request, pk):
    try:
        doctor_availability = DoctorAvailability.objects.get(id=pk)
    except DoctorAvailability.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DoctorAvailabilitySerializer(doctor_availability)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = DoctorAvailabilitySerializer(doctor_availability, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    if request.method == 'DELETE':
        doctor_availability.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# GET api/note-medical/ - Listar todas las notas medicas
# POST api/note-medical/ - Crear una nueva nota medica
# GET api/note-medical/<pk>/ - Detalle
# PUT api/note-medical/<pk>/ - Modifiacion
# DELETE api/note-medical/<pk>/ - Borrar


@api_view(['GET', 'POST'])
def list_medical_note(request):
    if request.method == 'GET':
        medical_notes = MedicalNote.objects.all()
        serializer = MedicalNoteSerializer(medical_notes, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = MedicalNoteSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def detail_medical_note(request, pk):
    try:
        medical_note = MedicalNote.objects.get(id=pk)
    except MedicalNote.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = MedicalNoteSerializer(medical_note)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = MedicalNoteSerializer(medical_note, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    if request.method == 'DELETE':
        medical_note.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)