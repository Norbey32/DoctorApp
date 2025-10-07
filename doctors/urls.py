from django.urls import path

from .views import list_doctors


urlpatterns = [
    path('doctors/', list_doctors),
    # path('doctors/', ),
]