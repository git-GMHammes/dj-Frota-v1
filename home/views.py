from django.http import response
from django.shortcuts import render

# Create your views here.

def principal(request):
    return render(request, 'home/index.html')