# -*- coding: utf-8 -*-

from datetime import datetime
from django.contrib.auth.models import User
from django.db import models
from compras.constants import MONEDA_CHOICES


class EgresoAdministrativo(models.Model):
    """
    Egresos administrativos
    """
    detalle_general = models.CharField(max_length=250)
    fecha = models.DateField(default=datetime.now)
    tipo_moneda = models.CharField(u"tipo de moneda", max_length=1,
                                   choices=MONEDA_CHOICES, default="S")
    tipo_cambio = models.FloatField(u"tipo de cambio", null=True, blank=True)
    multiple = models.BooleanField(
        u"múltiple", default=False,
        help_text=u"Contiene varios items del mismo tipo")
    precio_unitario = models.FloatField(blank=True, null=True)
    cantidad = models.IntegerField(default=1)
    unidad = models.CharField(max_length=20, blank=True)
    precio_neto = models.FloatField()

    def __unicode__(self):
        return "{obj.detalle_general}".format(obj=self)

    def get_precio_neto(self):
        return u"%.2f %s" % (self.precio_neto, self.get_tipo_moneda_display())

    get_precio_neto.short_description = u"precio neto"

    class Meta:
        verbose_name = u"egreso administrativo"
        verbose_name_plural = u"egresos administrativo"
        ordering = ("fecha",)


class Ingreso(models.Model):
    """
    Ingreso al banco, depósitos, inversión
    """
    detalle_general = models.CharField(max_length=250)
    fecha = models.DateField(default=datetime.now)
    tipo_moneda = models.CharField(u"tipo de moneda", max_length=1,
                                   choices=MONEDA_CHOICES)
    tipo_cambio = models.FloatField(u"tipo de cambio", null=True, blank=True)
    monto = models.FloatField()

    def __unicode__(self):
        return u"{obj.detalle_general}".format(obj=self)

    def get_monto(self):
        return u"%.2f %s" % (self.monto, self.get_tipo_moneda_display())

    get_monto.short_description = u"precio neto"

    class Meta:
        ordering = ("fecha",)