# -*- coding: utf-8 -*-

from django.db import models


class EgresoAdministrativo(models.Model):
    """
    Egresos administrativos
    """
    detalle_general = models.CharField(max_length=250)