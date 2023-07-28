from django.shortcuts import render
from .models import comidas
# Create your views here.

def home(request):

    comids = comidas.objects.all()

    return render(request, 'index.html', {'comids' : comids})