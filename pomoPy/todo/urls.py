from django.contrib import admin
from django.urls import path, include

app_name = "todo"

urlpatterns = [
    path("", include("django.contrib.auth.urls")),
]
