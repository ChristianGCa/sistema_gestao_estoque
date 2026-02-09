from django import forms
from . import models


class SupplierForm(forms.ModelForm):

    class Meta:
        model = models.Supplier
        fields = ['name', 'description']  # Adicione os campos necessários do modelo Supplier
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),  # Aplicando classe CSS do bootstrap
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),  # Aplicando classe CSS  e numero de linhas
        }
        labels = {
            'name': 'Nome do Fornecedor',
            'description': 'Descrição do Fornecedor',
        }
