# -*- coding: utf-8 -*-

from django.contrib import admin
from administrativo.models import EgresoAdministrativo, Ingreso


class Admin(admin.ModelAdmin):
    """

    """

admin.site.register(EgresoAdministrativo)
admin.site.register(Ingreso)