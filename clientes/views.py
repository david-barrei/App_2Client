from django.shortcuts import render
from .models import *
#from .forms import ClientesForm
from django.views.generic import TemplateView,CreateView,ListView,UpdateView,DeleteView
from django.urls import reverse_lazy, reverse

# Create your views here.

class inicio(TemplateView):
    template_name= 'paginas_base/inicio.html'

