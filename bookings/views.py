from .serializers import AppointmentSerializer, MedicalNoteSerializer
from .models import Appointment, MedicalNote

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


# GET api/bookings/ - Listar todos los pacientes
# POST api/bookings/ - Crear un nuevo paciente
# GET api/bookings/<pk>/ - Detalle
# PUT api/bookings/<pk>/ - Modifiacion
# DELETE api/bookings/<pk>/ - Borrar

@api_view(['GET', 'POST'])
def list_bookings(request):
    if request.method == 'GET':
        appointments = Appointment.objects.all()
        serializer = AppointmentSerializer(appointments, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = AppointmentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def detail_bookings(request, pk):
    try:
        appointment = Appointment.objects.get(id=pk)
    except Appointment.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AppointmentSerializer(appointment)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = AppointmentSerializer(appointment, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    if request.method == 'DELETE':
        appointment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# GET api/medical-note/ - Listar todos las notas
# POST api/medical-note/ - Crear una nueva nota
# GET api/medical-note/<pk>/ - Detalle
# PUT api/medical-note/<pk>/ - Modifiacion
# DELETE api/medical-note/<pk>/ - Borrar


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

