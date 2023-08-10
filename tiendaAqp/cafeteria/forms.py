
from django import forms
from .models import Pedido

class RawClienteForm(forms.Form):
    nombre = forms.CharField(label='Nombre', 
        widget=forms.TextInput(
            attrs={
                'placeholder':'ingresa solo tu nombre',
                'id': 'nombre',
                'class': 'form-control',
                'data-rule': 'minlen:1',
            }
            
        )
    )
    
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'placeholder':'ingresa tu email',
                'id': 'email',
                'class': 'form-control',
                'data-rule': 'minlen:1',
            }
            
        )
    )
    
    telefono = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                'placeholder':'ingresa tu telefono',
                'id': 'telefono',
                'class': 'form-control',
                'data-rule': 'minlen:1',
            }
            
        )
    )

#para pedidos
class RawPedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['cliente', 'productos', 'estado']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['cliente'].widget = forms.HiddenInput()
        self.fields['productos'].widget = forms.HiddenInput()
        self.fields['estado'].widget = forms.HiddenInput()