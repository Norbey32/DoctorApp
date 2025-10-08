from .serializers import AppointmentSerializer
from .models import Appointment

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

