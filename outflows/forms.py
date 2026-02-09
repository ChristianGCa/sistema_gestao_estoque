from django import forms
from django.core.exceptions import ValidationError
from . import models


class OutflowForm(forms.ModelForm):

    class Meta:
        model = models.Outflow
        fields = ['product', 'quantity', 'description']
        widgets = {
            'product': forms.Select(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
        labels = {
            'product': 'Produto',
            'quantity': 'Quantidade',
            'description': 'Descrição',
        }

    # Validação personalizada para garantir que a quantidade a ser removida não exceda o estoque disponível
    def clean_quantity(self):
        quantity = self.cleaned_data.get('quantity')
        product = self.cleaned_data.get('product')

        # Se produto não foi selecionado, não faz validação extra (deixa o erro padrão do campo)
        if product is None or quantity is None:
            return quantity

        if quantity > product.quantity:
            raise ValidationError(f'A quantidade disponível em estoque do produto {product.title} é de {product.quantity} unidade(s).')
        return quantity
