from rest_framework import generics
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from . import models, forms, serializers


class CategoryListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = models.Category
    template_name = 'category_list.html'
    context_object_name = 'categories'  # nome do model no plural e minúsculo
    paginate_by = 10  # Número de items por página
    permission_required = 'categories.view_category'

    def get_queryset(self):  # Sobrescreve o método get_queryset, que retorna todas as categories
        queryset = super().get_queryset()
        name = self.request.GET.get('name')  # Pega o parâmetro 'name' da URL

        if name:
            queryset = queryset.filter(name__icontains=name)  # Filtra as categories pelo nome, ignorando maiúsculas/minúsculas

        return queryset


class CategoryCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = models.Category
    template_name = 'category_create.html'
    form_class = forms.CategoryForm
    success_url = reverse_lazy('category_list')  # Redireciona para a lista de categories após a criação
    permission_required = 'categories.add_category'


class CategoryDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = models.Category
    template_name = 'category_detail.html'
    context_object_name = 'object'
    permission_required = 'categories.view_category'


class CategoryUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = models.Category
    template_name = 'category_update.html'
    form_class = forms.CategoryForm
    success_url = reverse_lazy('category_list')  # Redireciona para a lista de categories após a criação
    permission_required = 'categories.change_category'


class CategoryDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = models.Category
    template_name = 'category_delete.html'
    success_url = reverse_lazy('category_list')  # Redireciona para a lista de categories após a exclusão
    permission_required = 'categories.change_category'


class CategoryCreateListAPIView(generics.ListCreateAPIView):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer


class CategoryRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer
