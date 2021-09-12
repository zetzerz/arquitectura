from django.contrib import admin
from .models import dato_cliente,Año_ingreso,kardex,Archivos,Estado_Archivo,Certificados,Agenda

# Register your models here.

admin.site.register(dato_cliente)
admin.site.register(Año_ingreso)
admin.site.register(kardex)
admin.site.register(Archivos)
admin.site.register(Estado_Archivo)
admin.site.register(Certificados)
admin.site.register(Agenda)



