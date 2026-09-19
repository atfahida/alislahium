from django.urls import path
from . import views

urlpatterns = [
    path("", views.participant_list, name="participant_list"),
    path("register/", views.register_participant, name="register_participant"),
]