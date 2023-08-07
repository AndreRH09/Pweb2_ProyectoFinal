from django.shortcuts import render
from .models import comidas
from django.views.generic import ListView,View
from .utils import render_to_pdf
# Create your views here.

def home(request):

    comids = comidas.objects.all()

    return render(request, 'index.html', {'comids' : comids})

class listaProductos(ListView):

    model = comidas
    template_name = 'pdf/invoice.html'
    context_object_name= 'comidas'

class listaProductosPdf(View):

    def get(self, request, *args,**kwargs):
        com=  comidas.objects.all()
        data={
            'com': com
        }
        pdf = render_to_pdf('home/lista.html',data)
    
