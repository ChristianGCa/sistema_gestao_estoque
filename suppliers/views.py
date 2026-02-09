from rest_framework import generics
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from . import models, forms, serializers


class SupplierListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = models.Supplier
    template_name = 'suppliers_list.html'
    context_object_name = 'suppliers'  # nome do model no plural e minúsculo
    paginate_by = 10  # Número de items por página
    permission_required = 'suppliers.view_supplier'

    def get_queryset(self):  # Sobrescreve o método get_queryset, que retorna todas as suppliers
        queryset = super().get_queryset()
        name = self.request.GET.get('name')  # Pega o parâmetro 'name' da URL

        if name:
            queryset = queryset.filter(name__icontains=name)  # Filtra as suppliers pelo nome, ignorando maiúsculas/minúsculas

        return queryset


class SupplierCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = models.Supplier
    template_name = 'suppliers_create.html'
    form_class = forms.SupplierForm
    success_url = reverse_lazy('supplier_list')  # Redireciona para a lista de suppliers após a criação
    permission_required = 'suppliers.add_supplier'


class SupplierDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = models.Supplier
    template_name = 'suppliers_detail.html'
    context_object_name = 'object'
    permission_required = 'suppliers.view_supplier'


class SupplierUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = models.Supplier
    template_name = 'suppliers_update.html'
    form_class = forms.SupplierForm
    success_url = reverse_lazy('supplier_list')  # Redireciona para a lista de suppliers após a criação
    permission_required = 'suppliers.change_supplier'


class SupplierDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = models.Supplier
    template_name = 'suppliers_delete.html'
    success_url = reverse_lazy('supplier_list')  # Redireciona para a lista de suppliers após a exclusão
    permission_required = 'suppliers.delete_supplier'


class SupplierCreateListAPIView(generics.ListCreateAPIView):
    queryset = models.Supplier.objects.all()
    serializer_class = serializers.SupplierSerializer


class SupplierRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Supplier.objects.all()
    serializer_class = serializers.SupplierSerializer
