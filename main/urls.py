from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('projects/', views.projects, name='projects'),
    path('new_project/', views.new_project, name='new_project'),
    # path('edit_project/<int:project_id>/', views.edit_project, name='edit_project'),
]
