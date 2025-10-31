from django.shortcuts import render, redirect
from .models import Project
from .forms import ProjectForm
# Create your views here.

def index(request):
    return render(request, 'index.html')

def projects(request):
    projects = Project.objects.order_by('-id')
    return render(request, 'projects.html', {'projects': projects})

# TODO: NEW PROJECT ENDPOINT
def new_project(request):
    
    if request.method == 'POST':
        form = ProjectForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('projects')
        
    elif request.method == 'GET':
        form = ProjectForm()

    return render(request, 'new_project.html', {'form': form})


# TODO: EDIT PROJECT ENDPOINT
# def edit_project(request, project_id):
    
#     project = Project.objects.get(id=project_id)

#     if request.method == 'POST':
#         form = ProjectForm(instance=project,data=request.POST)

#         if form.is_valid():
#             form.save()
#             return redirect('projects')
        
#     else:
#         form = ProjectForm(instance=project)

#     return render(request, 'edit_project.html', {'form':form})