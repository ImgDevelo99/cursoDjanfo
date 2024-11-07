from django import forms
from .models import Producto

class ProductoForm(forms.ModelForm):# la clase hereda de forms.ModelForm = es una clase propia para creacion de formularios
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio', ' cantidad'] 