# -*- coding: utf-8 -*-

from django.contrib import admin
from ventas.models import Cliente, Vale, Venta, Credito, PlanPago


class Admin(admin.ModelAdmin):
    """

    """

admin.site.register(Cliente)
admin.site.register(Vale)
admin.site.register(Venta)
admin.site.register(Credito)
admin.site.register(PlanPago)