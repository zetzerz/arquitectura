from django.urls import path
from . import views
from .views import *


urlpatterns = [
    path('', home.as_view() , name="home"),
    path('agregar/', AgregarView.as_view(), name="agregar"),
    path('editar/edit/<int:pk>', EditarView.as_view(), name="editar"),
    path('eliminar/delete/<int:pk>', EliminarView.as_view(), name="eliminar"),
    path('detalle/<int:pk>', DetalleView.as_view(), name="detalle"),
    path('pago/', PagoView.as_view(), name="pago"),
    path('estado_proyecto/', EstadoView.as_view(), name="estado_proyecto"),
    path('formato_lista', FormatoLista.as_view(), name="formato_lista"),
    path('archivo/', FormatoAgregarView.as_view(), name="archivo"),
    path('editar_formato/edit/<int:pk>', EditarFormato.as_view(), name="editar_formato"),
    path('eliminar_formato/delete/<int:pk>', EliminarFormato.as_view(), name="eliminar_formato"),
    path('detalle_archivos/', Detalle_Archivos.as_view(), name="detalle_archivos"),
    path('ver_archivos/<int:pk>', VerDetalleView.as_view(), name="ver_archivos"),

    path('certificado_lista/', CertificadoLista.as_view(), name="certificado_lista"),
    path('agregar_certificado/', AgregarCertificado.as_view(), name="agregar_certificado"),
    path('editar_certificado/edit/<int:pk>', EditarCertificado.as_view(), name="editar_certificado"),
    path('eliminar_certificado/delete/<int:pk>', EliminarCertificado.as_view(), name="eliminar_certificado"),


    path('agenda_contacto/', Agenda_contacto.as_view(), name="agenda_contacto"),
    path('agregar_contacto/', Agregar_agenda.as_view(), name="agregar_contacto"),
    path('editar_agenda/edit/<int:pk>', Editar_agenda.as_view(), name="editar_agenda"),
    path('eliminar_agenda/delete/<int:pk>', Eliminar_agenda.as_view(), name="eliminar_agenda"),
]