from django.contrib import admin
from . import models


class InflowAdmin(admin.ModelAdmin):
    list_display = ('supplier', 'product', 'quantity', 'created_at', 'updated_at')
    search_fields = ('product__title', 'supplier__name')


admin.site.register(models.Inflow, InflowAdmin)
