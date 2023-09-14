from django.core import validators
from django import forms                #import forms
from .models import User                #User is model class

class StudentRegistration(forms.ModelForm): #creating model form class
    class Meta:
        model = User
        fields = ['name', 'email','password']     #this form field will be in same oredr
        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control'}),
            'email' : forms.EmailInput(attrs={'class':'form-control'}),
            'password' : forms.PasswordInput(render_value=True, attrs={'class':'form-control'}),
        }