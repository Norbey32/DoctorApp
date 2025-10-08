from django.urls import path
from .views import list_bookings, detail_bookings

urlpatterns = [
    path('bookings/', list_bookings),
    path('bookings/<int:pk>/', detail_bookings),
]