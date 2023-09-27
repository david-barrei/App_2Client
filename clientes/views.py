from django.shortcuts import render
from .models import *
from .forms import ClientesForm
from django.views.generic import TemplateView,CreateView,ListView,UpdateView,DeleteView
from django.urls import reverse_lazy, reverse

# Create your views here.

class inicio(TemplateView):
    template_name= 'paginas_base/inicio.html'


class lista(ListView):
    template_name= 'Crud/listado.html'
    model= Cliente
    ordering = 'nom'
    queryset= Cliente.objects.all()
    context_object_name = 'clientes'

class crear(CreateView):
    template_name = 'Crud/crear.html'
    model = Cliente
    form_class = ClientesForm

    def get_success_url(self, **kwargs):
        return reverse('clientes_app:lista')
    

    