from django import forms
from .models import dato_cliente,Archivos,Estado_Archivo,Certificados,Agenda
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User




class agregar_form(forms.ModelForm):
    class Meta:
        model = dato_cliente
        fields = ('nombre', 'numero_presupuesto', 'proyecto','direccion','honorario','honorario_dos','detalle','mes','año', 'pago_uno',
         'pago_dos','pago_tres','pago_cuatro','pago_quinto','pago_seis','estado','nombre_kardex','detalle_estado','proyecto_completado',
         'documento','documento_presupuesto',
         'complete',
         'file_uno',
         'file_dos',
         'file_tres',
         'file_cuatro',
         'file_cinco',
         'file_seis',
         'file_siete',
         'file_ocho',
         'file_nueve',
         'file_dies',
         'file_once',
         'file_doce',
         'file_trece',
         'file_catorce',
         'file_quince',)

    


class ArchivoForm(forms.ModelForm):
    class Meta:
        model = Archivos
        fields = '__all__'
        

class CertificadoForm(forms.ModelForm):
    class Meta:
        model = Certificados
        fields = '__all__'

class AgendaForm(forms.ModelForm):
    class Meta:
        model = Agenda
        fields = '__all__'






        

