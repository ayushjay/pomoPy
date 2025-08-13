
from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "pomodroApp"

urlpatterns = [
    path("<str:username>/50/",views.Pomo50, name="pomo50"),
    path("<str:username>/25/",views.Pomo25, name="pomo25"),

]
