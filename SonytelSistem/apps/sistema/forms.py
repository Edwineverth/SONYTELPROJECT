from django import forms
from models import * 
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout
"""
class ClienteForm(forms.From):
    cedula = 
    nombre = forms.CharField(max_length=30,required=True)
    apellido=froms.CharField(max_length==30,required=True)
    telefono=forms.CharField(max_length=10,required=True)
    direccion
    email
    estado
    ciudad
"""

class TestForm(forms.ModelForm):
    class Meta:
        model = Clientes

    #name = forms.CharField(required=True)
    #email = forms.EmailField(required=True)
    #url = forms.URLField(required=False)
    #comment = forms.CharField(required=True, widget=forms.Textarea)

    @property
    def helper(self):
        helper = FormHelper()
        helper.form_tag = False # don't render form DOM element
        helper.render_unmentioned_fields = True # render all fields
        helper.label_class = 'col-md-2'
        helper.field_class = 'col-md-10'
        return helper

