from django.shortcuts import render
from .models import Project
# Create your views here.

def add_project(request):
    if request.method == 'POST':
        