from django import forms
from .models import Teacher
from django.forms import widgets


class TeacherCreationForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = '__all__'
