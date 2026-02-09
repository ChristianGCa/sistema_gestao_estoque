from django.db import models
from brands.models import Brand
from categories.models import Category


class Product(models.Model):
    title = models.CharField(max_length=500)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='products')
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name='products')
    description = models.TextField(blank=True, null=True)
    serie_number = models.CharField(max_length=200, null=True, blank=True)
    cost_price = models.DecimalField(max_digits=10, decimal_places=2)
    selling_price = models.DecimalField(max_digits=10, decimal_places=2)
    # Se não informar, considera 0 pois podemos cadastrar o produto antes de ter estoque
    quantity = models.IntegerField(default=0)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title
