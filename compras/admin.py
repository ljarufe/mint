# -*- coding: utf-8 -*-

from django.contrib import admin
from compras.models import Tienda, Envio, Marca, TipoProducto, Producto, FotoProducto


class TiendaAdmin(admin.ModelAdmin):
    list_display = ("nombre", "url", "observaciones",)


class ProductoInLine(admin.StackedInline):
    extra = 1
    model = Producto


class EnvioAdmin(admin.ModelAdmin):
    list_display = ("tienda", "fecha_envio", "get_costo_envio",
                    "get_extras_admin", "get_total_admin")
    inlines = [ProductoInLine]


class FotoProductoInLine(admin.TabularInline):
    extra = 1
    model = FotoProducto
    readonly_fields = ("orden",)


class TipooductoAdmin(admin.ModelAdmin):
    inlines = [FotoProductoInLine]

admin.site.register(Tienda, TiendaAdmin)
admin.site.register(Envio, EnvioAdmin)
admin.site.register(Marca)
admin.site.register(TipoProducto, TipooductoAdmin)
admin.site.register(Producto)