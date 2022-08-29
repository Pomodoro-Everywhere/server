from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("start_pomodoro", views.start_pomodoro, name="start pomodoro api call")
]
