from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    # view, create & edit projects endpoints
    path('projects/', views.all_projects, name='projects'),
    path('project/<int:pid>/', views.project, name='project'),
    path('new_project/', views.new_project, name='new_project'),
    path('edit_project/<int:pid>/', views.edit_project, name='edit_project'),

    # Login & Logout endpoints
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
