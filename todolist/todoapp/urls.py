from django.contrib import admin
from django.urls import path
from todoapp.views import UserLogin

urlpatterns = [
    path("user/login",UserLogin.as_view()),
]