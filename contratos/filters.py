from .models import Contrato
import django_filters


rangos = ((0,"0 - 100'000.000"),
		  (1,"100'000.001  -  500'000.000"),
		  (2,"500'000.001  -  1000'000.000"),
		  (3,"Mayores  a 1000'000.000"))

class ContratosFilter(django_filters.FilterSet):
    objeto = django_filters.CharFilter(lookup_expr='icontains')
    valor_ejecutado_gt = django_filters.NumberFilter(name='valor_ejecutado', lookup_expr='gt')
    valor_ejecutado_lt = django_filters.NumberFilter(name='valor_ejecutado', lookup_expr='lt')
    fecha_terminacion_gt = django_filters.DateFilter(name='fecha_terminacion', lookup_expr='gt')
    fecha_terminacion_lt = django_filters.DateFilter(name='fecha_terminacion', lookup_expr='lt')
#    valor =  django_filters.ChoiceFilter(choices=rangos, method='filtro_rangos')

    def filtro_rangos(self, queryset, name,value):
    	print(name)

    class Meta:
        model = Contrato
        fields = {'numero', 'year', 'objeto','tipo_de_obra',
                  'departamento','municipio',}
