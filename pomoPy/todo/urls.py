from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from .views import RegisterView, TodoList,TodoCreate, TodoDetail, TodoUpdate, TodoDelete

app_name = "todo"

urlpatterns = [
    path("", TodoList.as_view(), name="todolist_url"),
    path("login/", LoginView.as_view(template_name="todo/login.html"), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("register/", RegisterView.as_view(), name="register"),
    path("create/",TodoCreate.as_view(), name="create"),
    path("<int:pk>", TodoDetail.as_view(), name="detail"),
    path("update/<int:pk>/",TodoUpdate.as_view(), name ="update"),
    path("delete/<int:pk>", TodoDelete.as_view(), name= "delete"),
    
]