from django import forms
from . import models


class CategoryForm(forms.ModelForm):

    class Meta:
        model = models.Category
        fields = ['name', 'description']  # Adicione os campos necessários do modelo Category
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),  # Aplicando classe CSS do bootstrap
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),  # Aplicando classe CSS  e numero de linhas
        }
        labels = {
            'name': 'Nome da Categoria',
            'description': 'Descrição da Categoria',
        }
