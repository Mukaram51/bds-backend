from django import forms
from .models import Project

# TODO: CREATE PROJECT FORM
class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'description', 'is_completed']

    name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': "Project Name",
        'class': 'p-2 w-30'
    }))

    description = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder': "Project Name",
        'class': 'p-1'
    }))