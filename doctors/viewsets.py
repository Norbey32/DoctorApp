from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from bookings.models import Appointment
from bookings.serializers import AppointmentSerializer
from .serializers import (
    DoctorSerializer, DepartmentSerializer,
    DoctorAvailabilitySerializer, MedicalNoteSerializer
)
from .models import Doctor, Department, DoctorAvailability, MedicalNote
from .permissions import IsDoctor
from rest_framework.permissions import IsAuthenticated


class DoctorViewSets(viewsets.ModelViewSet):
    serializer_class = DoctorSerializer
    queryset = Doctor.objects.all()
    permission_classes = [IsAuthenticated, IsDoctor]

    @action(["POST"], detail=True, url_path='set-on-vacations')
    def set_on_vacations(self, request, pk):
        doctor = self.get_object()
        doctor.is_on_vacations = True
        doctor.save()
        return Response({"status": "El doctor esta de vacaciones"})
    
    @action(["POST"], detail=True, url_path='set-off-vacations')
    def set_off_vacations(self, request, pk):
        doctor = self.get_object()
        doctor.is_on_vacations = False
        doctor.save()
        return Response({"status": "El doctor esta disponible"})

    @action(['POST', 'GET'], detail=True, serializer_class=AppointmentSerializer)
    def appointments(self, request, pk):
        doctor = self.get_object()
        data = request.data.copy()
        data['doctors'] = doctor.id

        if request.method == 'POST':
            data = request.data.copy()
            data['doctors'] = doctor.id
            serializer = AppointmentSerializer(data=data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return  Response(serializer.data, status=status.HTTP_201_CREATED)

        if request.method == 'GET':
            appointments = Appointment.objects.filter(doctor=doctor)
            serializer = AppointmentSerializer(appointments, many=True)
            return Response(serializer.data)

class DepartmentViewSets(viewsets.ModelViewSet):
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()


class DoctorAvailabilityViewSets(viewsets.ModelViewSet):
    serializer_class = DoctorAvailabilitySerializer
    queryset = DoctorAvailability.objects.all()


class MedicalNoteViewSets(viewsets.ModelViewSet):
    serializer_class = MedicalNoteSerializer
    queryset = MedicalNote.objects.all()