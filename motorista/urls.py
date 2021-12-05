from django.urls import path
from . import views

urlpatterns = [
    path('', views.principal)   # função que será chamada na views.py
]
