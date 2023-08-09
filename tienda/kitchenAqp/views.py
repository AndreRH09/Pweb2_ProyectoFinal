from django.shortcuts import render
from .models import comidas

from django.views.generic import ListView,View
from .utils import render_to_pdf
from django.http import HttpResponse
# Create your views here.

def home(request):

    comids = comidas.objects.all()

    return render(request, 'index.html', {'comids' : comids})


class VerMenuPdf(View):

    def get(self, request, *args,**kwargs):
        comida=  comidas.objects.all()
        data={
            'comidas': comida
        }
        pdf = render_to_pdf('pdf/menu.html',data)
        return HttpResponse(pdf,content_type='application/pdf')
    
class DescargarMenu(View):

    def get(self, request, *args,**kwargs):
        comida=  comidas.objects.all()
        data={
            'comidas': comida
        }
        pdf = render_to_pdf('pdf/menu.html',data)
        response = HttpResponse(pdf,content_type='application/pdf')
        filename= "Menu.pdf"
        content= "attachment; filename=%s" %(filename)
        response['Content-Disposition']= content
        return response