# -*- coding: utf-8 -*-

from django.contrib import admin
from administrativo.models import EgresoAdministrativo, Ingreso


class EgresoAdministrativoAdmin(admin.ModelAdmin):
    list_display = ("detalle_general", "fecha", "multiple", "cantidad",
                    "get_precio_neto")
    list_filter = ("multiple",)


class IngresoAdmin(admin.ModelAdmin):
    list_display = ("detalle_general", "fecha", "get_monto",)

admin.site.register(EgresoAdministrativo, EgresoAdministrativoAdmin)
admin.site.register(Ingreso, IngresoAdmin)