from django.shortcuts import render,redirect
from .models import dato_cliente,Archivos,Estado_Archivo,Certificados,Agenda
from .forms import agregar_form,ArchivoForm,CertificadoForm,AgendaForm
from django.urls import reverse_lazy
from django.views.generic import ListView,CreateView,DetailView,DeleteView,TemplateView,UpdateView,FormView
from django.db.models import Q
from .filters import AñoFilter,EstadoFilter,ArchivoFilter,AgendaFilter
from django.views import generic
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.template import context
from django.http import request



# Create your views here.


class home(ListView):
    model = dato_cliente
    template_name = 'miapp/home.html'
    queryset = dato_cliente.objects.all().order_by('-id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = AñoFilter(self.request.GET, queryset=self.get_queryset())
        return context



class AgregarView(CreateView):
    model = dato_cliente
    form_class = agregar_form
    template_name= 'miapp/agregar.html'

class EditarView(UpdateView):
    model = dato_cliente
    form_class = agregar_form
    template_name = 'miapp/editar.html'

class EliminarView(DeleteView):
    model= dato_cliente
    template_name = 'miapp/eliminar.html'
    success_url = reverse_lazy('home')

class DetalleView(DetailView):
    model = dato_cliente
    template_name = 'miapp/detalle.html'
    




class PagoView(ListView):
    template_name = 'miapp/pago.html'
    model= dato_cliente
    queryset = dato_cliente.objects.all().order_by('-id')
  
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = AñoFilter(self.request.GET, queryset=self.get_queryset())
        return context



class EstadoView(ListView):
    template_name = 'miapp/estado_proyecto.html'
    model = dato_cliente
    queryset = dato_cliente.objects.all().order_by('-id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = EstadoFilter(self.request.GET, queryset=self.get_queryset())
        return context




class FormatoLista(ListView):
    model = Archivos
    template_name = 'miapp/formato/formato_lista.html'


class FormatoAgregarView(CreateView):
    model = Archivos
    template_name= "miapp/formato/agregar_archivos.html"
    form_class = ArchivoForm

class EditarFormato(UpdateView):
    model = Archivos
    form_class = ArchivoForm
    template_name = 'miapp/formato/editar_formato.html'

class EliminarFormato(DeleteView):
    model= Archivos
    template_name = 'miapp/formato/eliminar_formato.html'
    success_url = reverse_lazy('formato_lista')



class Detalle_Archivos(ListView):
    model = dato_cliente
    template_name = 'miapp/archivos/detalle_archivos.html'
   
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = ArchivoFilter(self.request.GET, queryset=self.get_queryset())
        return context

class VerDetalleView(DetailView):
    model = dato_cliente
    template_name = 'miapp/archivos/ver_archivos.html'


class CertificadoLista(ListView):
    model = Certificados
    template_name = 'miapp/certificado/certificado_lista.html'

class AgregarCertificado(CreateView):
    model = Certificados
    form_class = CertificadoForm
    template_name = 'miapp/certificado/agregar_certificado.html'

class EditarCertificado(UpdateView):
    model = Certificados
    form_class = CertificadoForm
    template_name = 'miapp/certificado/editar_certificado.html'

class EliminarCertificado(DeleteView):
    model = Certificados
    template_name = 'miapp/certificado/eliminar_certificado.html'
    success_url = reverse_lazy('certificado_lista')


class Agenda_contacto(ListView):
    model = Agenda
    template_name = 'miapp/agenda/agenda_contacto.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = AgendaFilter(self.request.GET, queryset=self.get_queryset())
        return context

class Agregar_agenda(CreateView):
    model = Agenda
    form_class = AgendaForm
    template_name = 'miapp/agenda/agregar_contacto.html'

class Editar_agenda(UpdateView):
    model = Agenda
    form_class = AgendaForm
    template_name = 'miapp/agenda/editar_agenda.html'

class Eliminar_agenda(DeleteView):
    model = Agenda
    template_name = 'miapp/agenda/eliminar_agenda.html'
    success_url = reverse_lazy('agenda_contacto')
    
