from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('projects/', views.projects, name='projects'),
    path('new_project/', views.new_project, name='new_project'),
    # path('edit_project/<int:project_id>/', views.edit_project, name='edit_project'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
