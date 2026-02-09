from django.db.models.signals import post_save
from django.dispatch import receiver
from outflows.models import Outflow


@receiver(post_save, sender=Outflow)  # Esse decorator faz a conexão do sinal com o modelo Outflow
def update_product_quantity(sender, instance, created, **kwargs):
    if created:
        if instance.quantity > 0:
            product = instance.product
            product.quantity -= instance.quantity
            product.save()

# Podemos fazer a conexão de outra forma
# post_save.connect(update_product_quantity, sender=Inflow)
