# -*- coding: utf-8 -*-

from datetime import datetime
from django.db import models
from compras.models import Producto
from ventas.constants import TIPO_PAGO_CHOICES


class Cliente(models.Model):
    """
    Cliente de la tienda
    """
    nombre = models.CharField(max_length=150)
    telefono = models.CharField(u"teléfono", max_length=9, blank=True)
    direccion = models.CharField(u"dirección", max_length=200, blank=True)
    email = models.EmailField(blank=True)

    def __unicode__(self):
        return u"{obj.nombre}".format(obj=self)


class Vale(models.Model):
    """
    Vale de descuento
    """
    codigo = models.CharField(max_length=5)
    cliente = models.ForeignKey(Cliente)

    def __unicode__(self):
        return u"{obj.cliente}: {obj.codigo}".format(obj=self)



class Credito(models.Model):
    """
    Compra al crédito
    """
    capital_pactado = models.FloatField()
    saldo_capital = models.FloatField()
    numero_cuotas = models.IntegerField(verbose_name=u"número de cuotas")
    fecha_inicial = models.DateField()
    fecha_final = models.DateField()
    estado_credito = models.BooleanField()

    def __unicode__(self):
        return u""

    def get_capital_pagado(self):
        return self.capital_pactado - self.saldo_capital

    class Meta:
        verbose_name = u"crédito"
        verbose_name_plural = u"créditos"


class PlanPago(models.Model):
    """
    Plan de pago de un crédito
    """
    credito = models.ForeignKey(Credito, verbose_name=u"crédito")
    numero_cuota = models.IntegerField(u"número de cuota")
    estado_cuota = models.BooleanField(u"estado de cuota")
    capital_pactado = models.FloatField()
    capital_pagado = models.FloatField()
    fecha_vencimiento = models.DateField(u"fecha de vencimiento")

    def __unicode__(self):
        return u"%s - %s" % (self.fecha_vencimiento, self.numero_cuota)

    class Meta:
        verbose_name = u"plan de pago"
        verbose_name_plural = u"plan de pagos"


class Venta(models.Model):
    """
    Venta de un producto
    """
    productos = models.ManyToManyField(Producto)
    cliente = models.ForeignKey(Cliente)
    fecha = models.DateField(default=datetime.now)
    vale = models.ForeignKey(Vale, blank=True, null=True)
    descuento = models.FloatField(blank=True, null=True)
    total = models.FloatField()
    tipo_pago = models.CharField(u"Tipo de pago", max_length=2, default=u"Co",
                                 choices=TIPO_PAGO_CHOICES)
    credito = models.ForeignKey(Credito, null=True, blank=True,
                                verbose_name=u"crédito")

    def __unicode__(self):
        return u"{obj.cliente}: {obj.fecha}".format(obj=self)
