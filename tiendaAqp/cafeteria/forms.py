
from django import forms
from .models import Cliente

class RawClienteForm(forms.Form):
    nombre = forms.CharField(label='Nombre', 
        widget=forms.TextInput(
            attrs={
                'placeholder':'ingresa solo tu nombre',
                'id': 'nombre',
                'class': 'special'
            }
            
        )
    )
    
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'placeholder':'ingresa tu email',
                'id': 'email',
                'class': 'special'
            }
            
        )
    )
    telefono = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                'placeholder':'ingresa tu telefono',
                'id': 'telefono',
                'class': 'special'
            }
            
        )
    )