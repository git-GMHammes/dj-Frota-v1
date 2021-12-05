from django.urls import path
from . import views

urlpatterns = [
    path('', views.principal)   # Função qus será chamada na views.py
]
