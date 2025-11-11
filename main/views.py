from django.shortcuts import render, redirect
from .models import Project
from .forms import ProjectForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
# Create your views here.

# HOMEPAGE VIEW ENDPOINT
def index(request):
    projects = Project.objects.order_by('-id')[:4]
    return render(request, 'index.html', {'projects': projects})

# PROJECTS: list all available projects in the database
def all_projects(request):
    projects = Project.objects.order_by('-id')
    return render(request, 'projects.html', {'projects': projects})


# Individual project endpoint: route to indivual project to give full project detail
def project(request, pid):
    project = Project.objects.get(id=pid)
    return render(request, 'project.html', {'project':project})


def login_view(request):
    if request.method == 'POST':

        form = AuthenticationForm(request=request, data=request.POST)

        if form.is_valid():

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
    else:
        form = AuthenticationForm()
    
    return render(request, 'auth/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('index')



# NEW PROJECT ENDPOINT: Add new projects & validate form data
@login_required
def new_project(request):
    
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('projects')
        
    elif request.method == 'GET':
        form = ProjectForm()

    return render(request, 'new_project.html', {'form': form})


# TODO: EDIT PROJECT ENDPOINT
@login_required
def edit_project(request, pid):
    
    project = Project.objects.get(id=pid)

    if request.method == 'POST':
        form = ProjectForm(instance=project,data=request.POST)

        if form.is_valid():
            form.save()
            return redirect('projects')
        
    else:
        form = ProjectForm(instance=project)

    return render(request, 'edit_project.html', {'form':form, 'project':project})