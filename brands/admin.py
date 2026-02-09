from django.contrib import admin
from . import models


class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)  # Sempre colocar vírgula no final de tuplas de um único elemento para evitar que seja interpretado como string


admin.site.register(models.Brand, BrandAdmin)
