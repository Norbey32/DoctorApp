from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from patients.models import Patient
from .models import Doctor




class DoctorViewSetsTest(TestCase):

    def setUp(self):
        self.patient = Patient.objects.create(
            first_name='Luis',
            last_name='Arboleda',
            date_of_birth='1999-12-12',
            contact_number='2345676899',
            email='arboleda@example.com',
            address='no existe',
            medical_history='ninguna'
        )
        self.doctor = Doctor.objects.create(
            first_name='Luis',
            last_name='Gutierrez',
            qualification='profesional',
            contact_number='3214564677',
            email='example@example.com',
            address='no existe',
            biography='neurocirujano',
            is_on_vacations=False
        )
        self.client = APIClient()


    def test_list_should_return_200(self):
        url = reverse('doctor-appointments', kwargs={"pk": self.doctor.id})

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
