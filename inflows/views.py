from rest_framework import generics
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView
from . import models, forms, serializers


class InflowListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = models.Inflow
    template_name = 'inflow_list.html'
    context_object_name = 'inflows'  # nome do model no plural e minúsculo
    paginate_by = 10  # Número de items por página
    permission_required = 'inflows.view_inflow'

    def get_queryset(self):  # Sobrescreve o método get_queryset, que retorna todas as inflows
        queryset = super().get_queryset()
        product = self.request.GET.get('product')  # Alteramos para product

        if product:
            queryset = queryset.filter(product__title__icontains=product)  # Filtra as inflows pelo produto

        return queryset


class InflowCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = models.Inflow
    template_name = 'inflow_create.html'
    form_class = forms.InflowForm
    success_url = reverse_lazy('inflow_list')  # Redireciona para a lista de inflows após a criação
    permission_required = 'inflows.add_inflow'


class InflowDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = models.Inflow
    template_name = 'inflow_detail.html'
    context_object_name = 'object'
    permission_required = 'inflows.view_inflow'


class InflowCreateListAPIView(generics.ListCreateAPIView):
    queryset = models.Inflow.objects.all()
    serializer_class = serializers.InflowSerializer


class InflowRetrieveAPIView(generics.RetrieveAPIView):
    queryset = models.Inflow.objects.all()
    serializer_class = serializers.InflowSerializer
