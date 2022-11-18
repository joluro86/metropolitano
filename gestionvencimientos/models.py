from tkinter import CASCADE
from django.db import models

class Ans(models.Model):    
    Pedido = models.TextField(max_length=100, default=0, null=True)
    Subped = models.CharField(max_length=100, default=0, null=True)
    Soli = models.CharField(max_length=200, null=True, default=0)
    Producto_id = models.CharField(max_length=200, null=True, default=0)
    Tipo_Trabajo = models.CharField(max_length=200, null=True, default=0)
    Tipo_Elemento_ID = models.CharField(max_length=200, null=True, default=0)
    Fecha_Recibo = models.CharField(max_length=500, default=0)
    Fecha_Ingreso_Sol = models.CharField(max_length=500, default=0)
    Fecha_Concepto = models.CharField(max_length=500, default=0)
    Fecha_Inicio_ANS = models.CharField(max_length=500, default=0)
    Días_ANS = models.DecimalField(decimal_places=2, max_digits=100, default=0.00)
    Estado = models.CharField(max_length=500, null=True, default=0)
    Concepto = models.CharField(max_length=500, null=True, default=0)
    Nombre_concepto = models.CharField(max_length=500, null=True, default=0)
    ClienteID = models.CharField(max_length=500, null=True, default=0)
    Nombre_Cliente = models.CharField(max_length=500, null=True, default=0)
    Telefono = models.CharField(max_length=100, null=True, default=0)
    Correo = models.CharField(max_length=100, null=True, default=0)
    Direccion_Correspondencia = models.CharField(max_length=5000, null=True)
    Municipio_Correspondencia = models.CharField(max_length=5000, null=True)
    Telefono_Contacto = models.CharField(max_length=5000, null=True, default=0)
    Celular_Contacto = models.CharField(max_length=5000, null=True, default=0)
    Direccion = models.CharField(max_length=5000, null=True)
    Municipio = models.CharField(max_length=5000, null=True)
    Instalación = models.CharField(max_length=5000, null=True)
    Area_Operativa = models.CharField(max_length=5000, null=True)
    Subzona = models.CharField(max_length=5000, null=True)
    Area_Trabajo = models.CharField(max_length=5000, null=True)
    Ruta = models.CharField(max_length=5000, null=True)
    Coordenadax = models.CharField(max_length=5000, null=True)
    Coordenaday = models.CharField(max_length=5000, null=True)
    Actividad = models.CharField(max_length=5000, null=True)
    Equipo = models.CharField(max_length=5000, null=True)
    Nombre = models.CharField(max_length=5000, null=True)
    Fecha_Programación = models.CharField(max_length=5000, default=0)
    Num_Proyecto = models.CharField(max_length=500, null=True)
    Tipo_Dirección = models.CharField(max_length=10000, null=True)
    Observación = models.CharField(max_length=5000, null=True)
    Observación_Solicitud = models.CharField(max_length=5000, null=True)
    Pedido_CRM = models.CharField(max_length=5000, null=True, default=0)
    dias_vencimiento = models.IntegerField(verbose_name="Dias de vencimiento", default=0)
    dias_vencimiento_epm = models.IntegerField(verbose_name="Dias de vencimiento epm", default=0)
    fecha_vencimiento = models.CharField(max_length=30, verbose_name="Fecha vencimiento", default=0)
    encargado = models.CharField(max_length=100, null=True)
    estado_cierre = models.IntegerField(default=0, null=True, blank=True)
    fecha_cierre = models.CharField(max_length=100, null=True, default=0)
    fecha_vence_sin_hora= models.CharField(max_length=50, default=0)
    hora_vencimiento = models.CharField(max_length=50, default=0)
    fecha_vence_epm= models.CharField(max_length=50, default=0)

    class Meta:
        ordering = ["fecha_vencimiento"]
        verbose_name = "Programador"
        verbose_name_plural = "Programador"
        
    def __str__(self):
        return str(self.Pedido)

class Encargado(models.Model):
    nombre = models.CharField(max_length=50, null=True)

    class Meta:
        verbose_name = "Encargado"
        verbose_name_plural = "Encargados"

    def __str__(self):
        return self.nombre

class Actividad(models.Model):
    nombre = models.CharField(max_length=50, null=True)
    dias_urbano = models.CharField(max_length=50, null=True)
    dias_rural = models.CharField(max_length=50, null=True)
    encargado = models.ForeignKey(
        Encargado, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = "Actividad"
        verbose_name_plural = "Actividades"
        
class Actividad_epm(models.Model):
    nombre = models.CharField(max_length=50, null=True)
    dias_urbano = models.CharField(max_length=50, null=True)
    dias_rural = models.CharField(max_length=50, null=True)

    class Meta:
        verbose_name = "Actividad epm"
        verbose_name_plural = "Actividades epm"

class Vencido(models.Model):
    Pedido = models.TextField(max_length=100, default=0)
    Instalación = models.CharField(max_length=5000, null=True)
    Actividad = models.CharField(max_length=5000, null=True)
    Observación = models.CharField(max_length=5000, null=True)
    fecha_vencimiento = models.CharField(max_length=30, verbose_name="Fecha vencimiento", null=True, default="Sin registro")
    encargado = models.CharField(max_length=100, null=True)
    fecha_cierre = models.CharField(max_length=100, null=True)

    class Meta:
        verbose_name = "Vencido"
        verbose_name_plural = "Vencidos"

class Municipio(models.Model):
    nombre = models.CharField(max_length=100, null=True)

    class Meta:
        verbose_name = "Municipio"
        verbose_name_plural = "Municipios"

class NumeroActa(models.Model):
    numero= models.IntegerField()

    class Meta:
        verbose_name = 'Acta actual'
        verbose_name_plural = 'Acta actual'

    def __str__(self):
        return str('Acta # ' + str(self.numero))

class Guia(models.Model):
    nombre_perseo = models.CharField(verbose_name='Nombre Perseo', max_length=100)
    nombre_fenix = models.CharField(verbose_name='Nombre Fenix', max_length=100)
    
    class Meta:
        verbose_name = 'guia'
        verbose_name_plural = 'guias'

    def __str__(self):
        return str(self.nombre_perseo)
