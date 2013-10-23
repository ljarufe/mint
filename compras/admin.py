# -*- coding: utf-8 -*-

from django.contrib import admin
from compras.models import Tienda, Foto, Envio, Marca, TipoProducto, Producto


class Admin(admin.ModelAdmin):
    """

    """

admin.site.register(Foto)
admin.site.register(Tienda)
admin.site.register(Envio)
admin.site.register(Marca)
admin.site.register(TipoProducto)
admin.site.register(Producto)