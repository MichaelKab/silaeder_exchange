'''
from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
class Edit_skills_Form(ModelForm):
    class Meta:
        model = CustomUser
        fields = ['due_back',]
'''