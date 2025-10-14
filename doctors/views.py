from .serializers import DoctorSerializer, DepartmentSerializer, DoctorAvailabilitySerializer, MedicalNoteSerializer
from .models import Doctor, Department, DoctorAvailability, MedicalNote

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView


# GET api/doctors/ - Listar todos los doctores
# POST api/doctors/ - Crear un nuevo doctor
# GET api/doctors/<pk>/ - Detalle
# PUT api/doctors/<pk>/ - Modifiacion
# DELETE api/doctors/<pk>/ - Borrar


class ListDoctorView(ListAPIView, CreateAPIView):
    allowed_methods = ['GET', 'POST']
    serializer_class = DoctorSerializer
    queryset = Doctor.objects.all()


class DetailDoctorView(RetrieveUpdateDestroyAPIView):
    allowed_methods = ['GET', 'PUT', 'DELETE']
    serializer_class = DoctorSerializer
    queryset = Doctor.objects.all()


# GET api/department/ - Listar todos los departamentos
# POST api/department/ - Crear un nuevo departamento
# GET api/department/<pk>/ - Detalle
# PUT api/department/<pk>/ - Modifiacion
# DELETE api/department/<pk>/ - Borrar


class ListDepartmentView(ListAPIView, CreateAPIView):
    allowed_methods = ['GET', 'POST']
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()


class DetailDepartmentView(RetrieveUpdateDestroyAPIView):
    allowed_methods = ['GET', 'PUT', 'DELETE']
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()


# GET api/doctor-availability/ - Listar todos los medicos
# POST api/doctor-availability/ - Crear una nueva disponibilidad de medicos
# GET api/doctor-availability/<pk>/ - Detalle
# PUT api/doctor-availability/<pk>/ - Modifiacion
# DELETE api/doctor-availability/<pk>/ - Borrar


class ListDoctorAvailabilityView(ListAPIView, CreateAPIView):
    allowed_methods = ['GET', 'POST']
    serializer_class = DoctorAvailabilitySerializer
    queryset = DoctorAvailability.objects.all()


class DetailDoctorAvailabilityView(RetrieveUpdateDestroyAPIView):
    allowed_methods = ['GET', 'PUT', 'DELETE']
    serializer_class = DoctorAvailabilitySerializer
    queryset = DoctorAvailability.objects.all()


# GET api/note-medical/ - Listar todas las notas medicas
# POST api/note-medical/ - Crear una nueva nota medica
# GET api/note-medical/<pk>/ - Detalle
# PUT api/note-medical/<pk>/ - Modifiacion
# DELETE api/note-medical/<pk>/ - Borrar


class ListMedicalNoteView(ListAPIView, CreateAPIView):
    allowed_methods = ['GET', 'POST']
    serializer_class = MedicalNoteSerializer
    queryset = MedicalNote.objects.all()


class DetailMedicalNoteView(RetrieveUpdateDestroyAPIView):
    allowed_methods = ['GET', 'PUT', 'DELETE']
    serializer_class = MedicalNoteSerializer
    queryset = MedicalNote.objects.all()
