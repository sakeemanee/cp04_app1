from django.core import validators
from django import forms
from django.forms import fields, widgets
from django.shortcuts import render 
from .models import User

class StudentRegistration(forms.ModelForm):
    class Meta:
        model = User
        fields = ['token_number','name','section_sem']
        widgets = {
            'token_name' : forms.TextInput(attrs={'class':'form-control'}),
            'name' : forms.TextInput(attrs={'class':'form-control'}),
            'section_sem' : forms.TextInput({'class':'form-control'}),
        } 
        
#'section_sem' : forms.TextInput("""render_value=True,""" attrs={'class':'form-control'}),        