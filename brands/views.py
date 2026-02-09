from rest_framework import generics
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from . import models, forms, serializers


class BrandListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = models.Brand
    template_name = 'brand_list.html'
    context_object_name = 'brands'  # nome do model no plural e minúsculo
    paginate_by = 10  # Número de items por página
    permission_required = 'brands.view_brand'  # <nome_da_app>.<nome_da_acao>_<nome_do_model>

    def get_queryset(self):  # Sobrescreve o método get_queryset, que retorna todas as brands
        queryset = super().get_queryset()
        name = self.request.GET.get('name')  # Pega o parâmetro 'name' da URL

        if name:
            queryset = queryset.filter(name__icontains=name)  # Filtra as brands pelo nome, ignorando maiúsculas/minúsculas

        return queryset


class BrandCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = models.Brand
    template_name = 'brand_create.html'
    form_class = forms.BrandForm
    success_url = reverse_lazy('brand_list')  # Redireciona para a lista de brands após a criação
    permission_required = 'brands.add_brand'


class BrandDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = models.Brand
    template_name = 'brand_detail.html'
    permission_required = 'brands.view_brand'


class BrandUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = models.Brand
    template_name = 'brand_update.html'
    form_class = forms.BrandForm
    success_url = reverse_lazy('brand_list')  # Redireciona para a lista de brands após a criação
    permission_required = 'brands.change_brand'


class BrandDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = models.Brand
    template_name = 'brand_delete.html'
    success_url = reverse_lazy('brand_list')  # Redireciona para a lista de brands após a exclusão
    permission_required = 'brands.delete_brand'


class BrandCreateListAPIView(generics.ListCreateAPIView):
    queryset = models.Brand.objects.all()
    serializer_class = serializers.BrandSerializer


class BrandRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Brand.objects.all()
    serializer_class = serializers.BrandSerializer
