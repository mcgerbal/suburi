from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:exercice_id>/", views.detail, name="detail"),
    path("sessions/add", views.newSession, name="newsession"),
]