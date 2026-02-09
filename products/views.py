from rest_framework import generics
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from app import metrics
from categories.models import Category
from products.models import Product
from . import models, forms, serializers


class ProductListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = models.Product
    template_name = 'product_list.html'
    context_object_name = 'products'  # nome do model no plural e minúsculo
    paginate_by = 10  # Número de items por página
    permission_required = 'products.view_product'

    def get_queryset(self):  # Sobrescreve o método get_queryset, que retorna todas os produtos
        queryset = super().get_queryset()
        title = self.request.GET.get('title')  # Pega o parâmetro 'title' da URL
        serie_number = self.request.GET.get('serie_number')  # Pega o parâmetro 'serie_number' da URL
        category = self.request.GET.get('category')  # Pega o parâmetro 'category' da URL
        brand = self.request.GET.get('brand')  # Pega o parâmetro 'brand' da URL

        if title:
            queryset = queryset.filter(title__icontains=title)  # Filtra os produtos pelo título, ignorando maiúsculas/minúsculas

        if serie_number:
            queryset = queryset.filter(serie_number__icontains=serie_number)  # Filtra os produtos pelo número de série, ignorando maiúsculas/minúsculas

        if category:
            queryset = queryset.filter(category_id=category)  # Filtra os produtos pela categoria

        if brand:
            queryset = queryset.filter(brand_id=brand)  # Filtra os produtos pela marca

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)  # pegamos o contexto padrão,
        context['product_metrics'] = metrics.get_product_metrics()
        context['categories'] = Category.objects.all()  # adicionamos todas as categorias ao contexto e
        context['brands'] = Product.objects.all()  # adicionamos todas as marcas ao contexto
        return context


class ProductCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = models.Product
    template_name = 'product_create.html'
    form_class = forms.ProductForm
    success_url = reverse_lazy('product_list')  # Redireciona para a lista de products após a criação
    permission_required = 'products.add_product'


class ProductDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = models.Product
    template_name = 'product_detail.html'
    context_object_name = 'object'
    permission_required = 'products.view_product'


class ProductUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = models.Product
    template_name = 'product_update.html'
    form_class = forms.ProductForm
    success_url = reverse_lazy('product_list')  # Redireciona para a lista de products após a criação
    permission_required = 'products.change_product'


class ProductDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = models.Product
    template_name = 'product_delete.html'
    success_url = reverse_lazy('product_list')  # Redireciona para a lista de products após a exclusão
    permission_required = 'products.delete_product'


class ProductCreateListAPIView(generics.ListCreateAPIView):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer


class ProductRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer
