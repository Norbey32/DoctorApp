from django.urls import path
from rest_framework.routers import DefaultRouter

from patients.viewsets import PatientsViewSets, InsuranceViewSets, MedicalRecordViewSets


router = DefaultRouter()
router.register('patients', PatientsViewSets)
router.register('insurance', InsuranceViewSets)
router.register('medical-record', MedicalRecordViewSets)

urlpatterns = router.urls