from django import forms
from django.forms import ModelForm
from models import * 

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Clientes
        exclude = ('cli_id',)
        #fields = ('cli_cedula','cli_nombre','cli_apellido')     
		  