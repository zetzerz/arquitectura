import django_filters
from .models import dato_cliente,Agenda


class AñoFilter(django_filters.FilterSet):
    class Meta:
        model = dato_cliente
        fields = ['año','estado','mes']


class EstadoFilter(django_filters.FilterSet):
    class Meta:
        model = dato_cliente
        fields = ['año','proyecto_completado','nombre_kardex']


class ArchivoFilter(django_filters.FilterSet):
    class Meta:
        model = dato_cliente
        fields = ['año','complete']

class AgendaFilter(django_filters.FilterSet):
    class Meta:
        model = Agenda
        fields = ['sitio','proyecto_agenda']


