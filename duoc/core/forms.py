from core.models import Producto
from django.forms import ModelForm
from django import forms



class formAgregar (ModelForm):
    class Meta  :
        model = Producto
        fields = '__all__'
