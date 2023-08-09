
from django import forms
from .models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'email', 'telefono']
        

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
    email = forms.EmailField()
    telefono = forms.IntegerField()
