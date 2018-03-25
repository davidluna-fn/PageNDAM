#encoding:utf-8
from django.forms import ModelForm
from django import forms
from .models import Contacto

class ContactoForm(forms.Form):
	nombre  = forms.CharField(max_length=100,label='Nombre' )
	numero  = forms.IntegerField()
	correo  = forms.EmailField()
	mensaje = forms.CharField(max_length=1000, widget=forms.Textarea)