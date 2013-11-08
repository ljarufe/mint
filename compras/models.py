# -*- coding: utf-8 -*-

from datetime import datetime
from django.db import models
from django.db.models import Sum
from common.models import Foto
from common.utils import get_photo_path
from .constants import MONEDA_CHOICES, ESTADO_PRODUCTO_CHOICES


class Tienda(models.Model):
    """
    Tienda donde se realizó una compra
    """
    nombre = models.CharField(max_length=100)
    url = models.URLField(blank=True)
    observaciones = models.TextField(blank=True)

    def __unicode__(self):
        return u"{obj.nombre}".format(obj=self)

    class Meta:
        ordering = ("nombre",)


class Envio(models.Model):
    """
    Envío de productos de alguna tienda
    """
    tienda = models.ForeignKey(Tienda)
    fecha_envio = models.DateField(u"fecha de envío", default=datetime.now)
    costo_envio = models.FloatField(u"costo de envío")
    tipo_moneda = models.CharField(u"tipo de moneda", max_length=1,
                                   choices=MONEDA_CHOICES, default="D")
    tipo_cambio = models.FloatField(u"tipo de cambio", null=True, blank=True)
    costo_aduana = models.FloatField(u"costo de aduana", default=0)
    costo_extra = models.FloatField(default=0)
    fecha_llegada = models.DateField(u"fecha de llegada", null=True, blank=True)

    def __unicode__(self):
        return u"{obj.tienda}: {obj.fecha_envio}".format(obj=self)

    def get_extras(self):
        return self.costo_aduana + self.costo_extra

    def get_total(self):
        """
        Devuelve el costo de todos los productos del envío y los costos extra
        """
        costo_productos = self.producto_set.aggregate(
            Sum("precio_compra"))["precio_compra__sum"]
        if not costo_productos:
            costo_productos = 0

        return self.get_extras() + costo_productos + self.costo_envio

    def get_costo_envio(self):
        return u"%.2f %s" % (self.costo_envio, self.get_tipo_moneda_display())

    get_costo_envio.short_description = u"costo de envío"

    def get_extras_admin(self):
        return u"%.2f %s" % (self.get_extras(), self.get_tipo_moneda_display())

    get_extras_admin.short_description = u"costos extras"

    def get_total_admin(self):
        return u"%.2f %s" % (self.get_total(), self.get_tipo_moneda_display())

    get_total_admin.short_description = u"costo total"

    class Meta:
        verbose_name = u"Envío"
        verbose_name_plural = u"Envíos"
        ordering = ("fecha_envio",)


class Marca(models.Model):
    """
    Marca de un producto
    """
    nombre = models.CharField(max_length=100)
    logo = models.ImageField(upload_to=get_photo_path, null=True, blank=True)
    url = models.URLField(blank=True)

    def __unicode__(self):
        return u"{obj.nombre}".format(obj=self.nombre)


class TipoProducto(models.Model):
    """
    Producto general
    """
    nombre = models.CharField(max_length=200)
    marca = models.ForeignKey(Marca)
    url = models.URLField(blank=True)
    foto_principal = models.ImageField(upload_to=get_photo_path, blank=True,
                                       null=True)

    def __unicode__(self):
        return u"{obj.nombre}".format(obj=self.nombre)

    class Meta:
        verbose_name = u"tipo de producto"
        verbose_name_plural = u"tipos de producto"


class FotoProducto(Foto):
    """
    Foto para los tipos de producto
    """
    tipo_producto = models.ForeignKey(TipoProducto,
                                      verbose_name=u"tipo de producto")
    orden = models.IntegerField()
    subir_facebook = models.BooleanField()


# TODO: Crear un método para clonar Productos
class Producto(models.Model):
    """
    Producto de la tienda
    """
    codigo = models.CharField(max_length=5, unique=True)
    tipo = models.ForeignKey(TipoProducto)
    talla = models.CharField(max_length=10)
    envio = models.ForeignKey(Envio)
    precio_compra = models.FloatField()
    costo_envio = models.FloatField(blank=True, null=True)
    costo_total = models.FloatField(blank=True, null=True)
    utilidad = models.FloatField(help_text=u"Factor de ganancia")
    precio_venta = models.FloatField()
    precio_final = models.FloatField(blank=True, null=True)
    estado = models.CharField(max_length=1, choices=ESTADO_PRODUCTO_CHOICES,
                              default="P")

    def __unicode__(self):
        return u"{obj.tipo: obj.talla [estado]}".\
            format(obj=self, estado=self.get_estado_display())
