from django import forms
from kkarmapp.models import*
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class contentform(forms.ModelForm):
    class Meta:
        fields='__all__'
        model=content 

class signupform(UserCreationForm):
    class Meta:
        fields=('first_name','last_name','username','email','password1','password2')
        model=User  

class Appointmentform(forms.ModelForm):
    class Meta:
        fields='__all__'
        model=Appoinment           

class Subcribeform(forms.ModelForm):
    class Meta:
        fields='__all__'
        model=Subcribe          

class Appointmentform(forms.ModelForm):
    class Meta:
        fields='__all__'
        model=Appoinment


           