from django import forms
from .models import Project

# TODO: CREATE PROJECT FORM
class ProjectForm(forms.ModelForm):
    class Meta: Project
    fields = ['name', 'description', 'is_completed']