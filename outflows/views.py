from rest_framework import generics
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView
from app import metrics
from . import models, forms, serializers


class OutflowListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = models.Outflow
    template_name = 'outflow_list.html'
    context_object_name = 'outflows'  # nome do model no plural e minúsculo
    paginate_by = 10  # Número de items por página
    permission_required = 'outflows.view_outflow'

    def get_queryset(self):  # Sobrescreve o método get_queryset, que retorna todas as outflows
        queryset = super().get_queryset()
        product = self.request.GET.get('product')  # Alteramos para product

        if product:
            queryset = queryset.filter(product__title__icontains=product)  # Filtra as outflows pelo produto

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sales_metrics'] = metrics.get_sales_metrics()
        return context


class OutflowCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = models.Outflow
    template_name = 'outflow_create.html'
    form_class = forms.OutflowForm
    success_url = reverse_lazy('outflow_list')  # Redireciona para a lista de outflows após a criação
    permission_required = 'outflows.add_outflow'


class OutflowDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = models.Outflow
    template_name = 'outflow_detail.html'
    context_object_name = 'object'
    permission_required = 'outflows.view_outflow'


class OutflowCreateListAPIView(generics.ListCreateAPIView):
    queryset = models.Outflow.objects.all()
    serializer_class = serializers.OutflowSerializer


class OutflowRetrieveAPIView(generics.RetrieveAPIView):
    queryset = models.Outflow.objects.all()
    serializer_class = serializers.OutflowSerializer
