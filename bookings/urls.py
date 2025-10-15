from django.urls import path
from rest_framework.routers import DefaultRouter
from .viewsets import BookingsViewSets, MedicalNoteViewSets


router = DefaultRouter()
router.register('bookings', BookingsViewSets)
router.register('medical-note', MedicalNoteViewSets)

urlpatterns = router.urls