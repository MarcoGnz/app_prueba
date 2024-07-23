from django import forms
from .models import articulo

class EjemploForm(forms.ModelForm):
    class Meta:
        model = articulo
        fields = ['nombre', 'descripcion',]