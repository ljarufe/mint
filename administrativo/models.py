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
    tipo_cambio = models.FloatField(u"tipo de cambio", null=True, blank=True)
    tipo_moneda = models.CharField(u"tipo de moneda", max_length=1,
                                   choices=MONEDA_CHOICES)
    precio_unitario = models.FloatField()
    multiple = models.BooleanField(u"múltiple", default=True)
    cantidad = models.IntegerField(default=1)
    precio_neto = models.FloatField(blank=True)
    unidad = models.CharField(max_length=20)

    def __unicode__(self):
        return "{obj.detalle_general}".format(obj=self)

    class Meta:
        verbose_name = u"egreso administrativo"
        verbose_name_plural = u"egresos administrativo"


class Ingreso(models.Model):
    """
    Ingreso al banco, depósitos, inversión
    """
    detalle_general = models.CharField(max_length=250)
    administrador = models.ForeignKey(User)
    fecha = models.DateField(default=datetime.now)
    monto = models.FloatField()
    tipo_cambio = models.FloatField(u"tipo de cambio", null=True, blank=True)
    tipo_moneda = models.CharField(u"tipo de moneda", max_length=1,
                                   choices=MONEDA_CHOICES)

    def __unicode__(self):
        return "{obj.detalle_general}".format(obj=self)