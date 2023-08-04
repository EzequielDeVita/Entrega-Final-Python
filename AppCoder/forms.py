from django import forms 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class FansFormulario(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    pais = forms.CharField()
    
class LideresFormulario(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()
    pais = forms.CharField()
    
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repita contraseña", widget=forms.PasswordInput)
    apellido = forms.CharField()
    nombre = forms.CharField()
    
    class Meta:
        model = User
        fields = ["username","email","password1","password2","apellido","nombre"]
        help_texts = {k:"" for k in fields}
        
class UserEditForm(UserCreationForm):
    #son las opciones para modificar el user
    email= forms.EmailField(label="Modificar E-mail")
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir la contraseña", widget = forms.PasswordInput)
    apellido = forms.CharField()
    nombre= forms.CharField()
    
    class Meta:
        model = User
        fields = ["email", "password1", "password2", "apellido", "nombre"]
        help_texts = {k:"" for k in fields}
        
