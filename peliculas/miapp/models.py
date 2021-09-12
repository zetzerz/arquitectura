from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

select_proyecto_complet = [
    ('APROBADO', 'APROBADO'),
    ('NO CONCRETADO', 'NO CONCRETADO'),
    ('INGRESADO', 'INGRESADO'),
    ('INGRESADO SAG', 'INGRESADO SAG'),
    ('INGRESADO DOM', 'INGRESADO DOM'),
    ('OBSERVADO', 'OBSERVADO'),
    ('EN PROCESO', 'EN PROCESO'),
]



select_estado = [
    ('PAGADO', 'PAGADO'),
    ('SIN PAGOS', 'SIN PAGOS'),
    ('ABONO', 'ABONO'),
]

select_meses = [
    ('ENERO', 'ENERO'),
    ('FEBRERO', 'FEBRERO'),
    ('MARZO', 'MARZO'),
    ('ABRIL', 'ABRIL'),
    ('MAYO', 'MAYO'),
    ('JUNIO', 'JUNIO'),
    ('JULIO', 'JULIO'),
    ('AGOSTO', 'AGOSTO'),
    ('SEPTIEMBRE', 'SEPTIEMBRE'),
    ('OCTUBRE', 'OCTUBRE'),
    ('NOVIEMBRE', 'NOVIEMBRE'),
    ('DICIEMBRE', 'DICIEMBRE'),
]

select_documentos = [
    ('COMPLETADOS', 'COMPLETADOS'),
    ('SIN DOCUMENTOS', 'SIN DOCUMENTOS'),
    ('ALGUNOS DOC', 'ALGUNOS DOC'),
]

select_detalle = [
    ('ARQUITECTURA', 'ARQUITECTURA'),
    ('INGENIERIA', 'INGENIERIA'),
    ('TOPOGRAFIA', 'TOPOGRAFIA'),
    ('ARQUITECTURA  INGENIERIA', 'ARQUITECTURA  INGENIERIA'),
    ('INGENIERIA  TOPOGRAFIA', 'INGENIERIA  TOPOGRAFIA'),
    ('ARQUITECTURA  TOPOGRAFIA', 'ARQUITECTURA  TOPOGRAFIA'),
]

class Año_ingreso(models.Model):
    año = models.CharField(max_length=20)

    def __str__(self):
        return self.año


class dato_cliente(models.Model):
    nombre = models.CharField(max_length=100)
    numero_presupuesto = models.CharField(max_length=4)
    proyecto = models.CharField(max_length=30)
    estado = models.CharField(max_length=30, null=False ,blank=False, choices=select_estado, default='DEBE PAGAR')
    año = models.ForeignKey(Año_ingreso, null=False,blank=False, on_delete=models.CASCADE)
    pago_uno  = models.CharField(max_length=20, null=True, blank=True,default=0)
    pago_dos = models.CharField(max_length=20, null=True,blank=True,default=0)
    pago_tres = models.CharField(max_length=20, null=True,blank=True,default=0)
    documento = models.FileField(null=True, blank=True,upload_to="documentos/", verbose_name="Excel DE PAGO")
    mes = models.CharField(max_length=30, null=True ,blank=True, choices=select_meses)
    detalle = models.CharField(max_length=100,null=True, blank=True, choices=select_detalle)
    honorario = models.CharField(max_length=20, null=False, blank=False,verbose_name="Honorario Arquitectura")
    direccion = models.CharField(max_length=100, null=True, blank=True)
    nombre_kardex = models.ForeignKey('kardex', on_delete=models.CASCADE, null=True,blank=True,)
    proyecto_completado = models.CharField(max_length=100, null=False ,blank=False, choices=select_proyecto_complet, default='EN PROCESO', verbose_name="")
    detalle_estado = models.CharField(max_length=100, null=True, blank=True,verbose_name="Informacion Adicional")
    documento_presupuesto = models.FileField(null=True, blank=True,upload_to="documentos/", verbose_name="DOC.PRESUPUESTO")
    file_uno = models.FileField(null=True, blank=True,upload_to="documentos/", verbose_name="Escritura")
    file_dos = models.FileField(null=True, blank=True,upload_to="documentos/", verbose_name="Fotocopia Carnet")
    file_tres = models.FileField(null=True, blank=True,upload_to="documentos/", verbose_name="Comprobante de Agua")
    file_cuatro = models.FileField(null=True, blank=True,upload_to="documentos/", verbose_name="Poder Simple")
    file_cinco = models.FileField(null=True, blank=True,upload_to="documentos/", verbose_name="Avaluo Detallado")
    file_seis = models.FileField(null=True, blank=True,upload_to="documentos/", verbose_name="Dominio Vigente")
    file_siete = models.FileField(null=True, blank=True,upload_to="documentos/", verbose_name="Certificado Informe Previo")
    file_ocho = models.FileField(null=True, blank=True,upload_to="documentos/", verbose_name="Utilidad Publica")
    file_nueve = models.FileField(null=True, blank=True,upload_to="documentos/", verbose_name="Conjunto Habitacional")
    file_dies = models.FileField(null=True, blank=True,upload_to="documentos/", verbose_name="Exp.Propiedad")
    file_once = models.FileField(null=True, blank=True,upload_to="documentos/", verbose_name="Informe Tecnico")
    file_doce = models.FileField(null=True, blank=True,upload_to="documentos/", verbose_name="Factibilidad")
    file_trece = models.FileField(null=True, blank=True,upload_to="documentos/", verbose_name="Solicitud")
    file_catorce = models.FileField(null=True, blank=True,upload_to="documentos/", verbose_name="I.N.E")
    file_quince = models.FileField(null=True, blank=True,upload_to="documentos/", verbose_name="Patente Profecional")
    complete = models.CharField(max_length=50, null=True ,blank=True, choices=select_documentos, verbose_name="Archivos Completos")
    pago_cuatro = models.CharField(max_length=20, null=True,blank=True,default=0)
    pago_quinto = models.CharField(max_length=100, null=True,blank=True,default=0, verbose_name="PAGO INGENIRIA O TOPOGRAFIA 1")
    honorario_dos = models.CharField(max_length=20, null=True, blank=True,verbose_name="honario Ing o topografia", default="0")
    pago_seis = models.CharField(max_length=100, null=True,blank=True,default=0, verbose_name="PAGO INGENIRIA O TOPOGRAFIA 2")



    def __str__(self):
        return self.nombre
    
    def get_absolute_url(self):
        return reverse('home')
        
    class Meta:
        ordering = ["-id"]

 
    


class kardex(models.Model):
    nombre_kardex = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_kardex



class Archivos(models.Model):
    formato = models.CharField(max_length=100)
    archivo_nuevo = models.FileField(null=True, blank=True,upload_to="archivos/")

    def __str__(self):
        return self.formato
        
    def get_absolute_url(self):
        return reverse('formato_lista')



class Estado_Archivo(models.Model):
    nombre = models.ManyToManyField('dato_cliente')
    estado_file = models.FileField(null=True, blank=True, upload_to="estado_archivo/")
    nombre_estado = models.CharField(max_length=100,null=False,blank=False)

    def __str__(self):
        return self.nombre_estado

    def get_absolute_url(self):
        return reverse('home')



class Certificados(models.Model):
    nombre_certificado = models.CharField(max_length=100,blank=False,null=False)
    link = models.URLField(max_length=300,null=False,blank=False)

    def __str__(self):
        return self.nombre_certificado

    def get_absolute_url(self):
        return reverse('certificado_lista')

class Agenda(models.Model):
    nombre_agenda = models.CharField(max_length=100,verbose_name="Nombre Contacto")
    proyecto_agenda= models.CharField(max_length=100,verbose_name="Descripcion")
    sitio = models.CharField(max_length=100)
    telefono = models.CharField(max_length=9)
    correo = models.EmailField(max_length=100)

    def __str__(self):
        return self.nombre_agenda
    
    class Meta:
        ordering = ["-id"]

    def get_absolute_url(self):
        return reverse('agenda_contacto')

    

