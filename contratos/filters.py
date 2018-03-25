from .models import Contrato
import django_filters

class ContratosFilter(django_filters.FilterSet):
    objeto = django_filters.CharFilter(lookup_expr='icontains')
    valor_ejecutado_gt = django_filters.NumberFilter(name='valor_ejecutado', lookup_expr='gt')
    valor_ejecutado_lt = django_filters.NumberFilter(name='valor_ejecutado', lookup_expr='lt')
    fecha_terminacion_gt = django_filters.DateFilter(name='fecha_terminacion', lookup_expr='gt')
    fecha_terminacion_lt = django_filters.DateFilter(name='fecha_terminacion', lookup_expr='lt')

    class Meta:
        model = Contrato
        fields = {'numero', 'year', 'objeto','tipo_de_obra',
                  'departamento','municipio',}
