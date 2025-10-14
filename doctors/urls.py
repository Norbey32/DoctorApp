from django.urls import path
from rest_framework.routers import DefaultRouter
from .viewsets import (
    DoctorViewSets, DepartmentViewSets,
    DoctorAvailabilityViewSets, MedicalNoteViewSets
)

router = DefaultRouter()
router.register('doctors', DoctorViewSets)
router.register('department', DepartmentViewSets)
router.register('doctor-availability', DoctorAvailabilityViewSets)
router.register('note-medical', MedicalNoteViewSets)

urlpatterns = router.urls