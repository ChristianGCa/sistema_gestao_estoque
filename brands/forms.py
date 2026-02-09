from django import forms
from . import models


class BrandForm(forms.ModelForm):

    class Meta:
        model = models.Brand
        fields = ['name', 'description']  # Adicione os campos necessários do modelo Brand
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),  # Aplicando classe CSS do bootstrap
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),  # Aplicando classe CSS  e numero de linhas
        }
        labels = {
            'name': 'Nome da Marca',
            'description': 'Descrição da Marca',
        }
