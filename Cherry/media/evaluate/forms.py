from django import forms
from .models import Assignment

class UploadDoc(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = ['name', 'content']