from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(label="Email")
    first_name = forms.CharField(label="first name")
    last_name = forms.CharField(label="last name")
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', "first_name", "last_name", 'email', )

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