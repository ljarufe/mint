# -*- coding: utf-8 -*-

from datetime import datetime
import os
import random
from django.db import models
from compras.constants import MONEDA_CHOICES, ESTADO_PRODUCTO_CHOICES


def get_photo_path(self, filename):
    """
    Devuelve un nombre aleatorio de archivo
    """
    univ = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    name = "".join([random.choice(univ) for i in xrange(20)])
    root, ext = os.path.splitext(filename)

    return u'photos/%s' % (name + ext)


class Foto(models.Model):
    """
    Foto genérica
    """
    nombre = models.CharField(max_length=50, blank=True)
    imagen = models.ImageField(upload_to=get_photo_path)

    def __unicode__(self):
        return u"{obj.nombre}".format(obj=self)


class Tienda(models.Model):
    """
    Tienda donde se realizó una compra
    """
    nombre = models.CharField(max_length=100)
    url = models.URLField(blank=True)
    observaciones = models.TextField(blank=True)

    def __unicode__(self):
        return u"{obj.nombre}".format(obj=self)


class Envio(models.Model):
    """
    Envío de productos de alguna tienda
    """
    tienda = models.ForeignKey(Tienda)
    costo_envio = models.FloatField(u"costo de envío")
    tipo_cambio = models.FloatField(u"tipo de cambio", null=True, blank=True)
    tipo_moneda = models.CharField(u"tipo de moneda", max_length=1,
                                   choices=MONEDA_CHOICES)
    costo_aduana = models.FloatField(u"costo de aduana", default=0)
    costo_extra = models.FloatField(default=0)
    fecha_envio = models.DateField(u"fecha de envío", default=datetime.now)
    fecha_llegada = models.DateField(u"fecha de llegada", null=True, blank=True)

    def __unicode__(self):
        return u"{obj.tienda el obj.fecha_envio}".format(obj=self)

    class Meta:
        verbose_name = u"Envío"
        verbose_name_plural = u"Envíos"


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
    fotos = models.ManyToManyField(Foto)

    def __unicode__(self):
        return u"{obj.nombre}".format(obj=self.nombre)

    class Meta:
        verbose_name = u"tipo de producto"
        verbose_name_plural = u"tipos de producto"


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
