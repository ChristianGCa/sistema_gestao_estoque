from django.db import models


class Brand(models.Model):
    name = models.CharField(max_length=500)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)    # Salva a data na hora da criação e nunca muda
    updated_at = models.DateTimeField(auto_now=True)        # Ao editar, a data será atualizada

    # Ordenando
    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
