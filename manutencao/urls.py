from django.urls import path
from . import views

urlpatterns = [
    path('', views.principal)   # nome da função do views.py
]
