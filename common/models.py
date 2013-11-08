# -*- coding: utf-8 -*-

from django.db import models
from .utils import get_photo_path


class Foto(models.Model):
    """
    Foto genérica
    """
    nombre = models.CharField(max_length=50, blank=True)
    imagen = models.ImageField(upload_to=get_photo_path)

    def __unicode__(self):
        return u"{obj.nombre}".format(obj=self)

    class Meta:
        abstract = True