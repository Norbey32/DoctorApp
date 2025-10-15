from .serializers import AppointmentSerializer, MedicalNoteSerializer
from .models import Appointment, MedicalNote

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView


# GET api/bookings/ - Listar todos las reservas
# POST api/bookings/ - Crear una nueva reserva
# GET api/bookings/<pk>/ - Detalle
# PUT api/bookings/<pk>/ - Modifiacion
# DELETE api/bookings/<pk>/ - Borrar


class ListBookingsView(ListAPIView, CreateAPIView):
    allowed_methods = ['GET', 'POST']
    serializer_class = AppointmentSerializer
    queryset = Appointment.objects.all()


class DetailBookimgsView(ListAPIView, CreateAPIView):
    allowed_methods = ['GET', 'PUT', 'DELETE']
    serializer_class = AppointmentSerializer
    queryset = Appointment.objects.all()


# GET api/medical-note/ - Listar todos las notas
# POST api/medical-note/ - Crear una nueva nota
# GET api/medical-note/<pk>/ - Detalle
# PUT api/medical-note/<pk>/ - Modifiacion
# DELETE api/medical-note/<pk>/ - Borrar


class ListMedicalNoteView(ListAPIView, CreateAPIView):
    allowed_methods = ['GET', 'POST']
    serializer_class = MedicalNoteSerializer
    queryset = MedicalNote.objects.all()


class DetailMedicalNoteView(ListAPIView, CreateAPIView):
    allowed_methods = ['GET', 'PUT', 'DELETE']
    serializer_class = MedicalNoteSerializer
    queryset = MedicalNote.objects.all()

