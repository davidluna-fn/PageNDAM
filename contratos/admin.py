from django.contrib import admin
from .models import Contrato, ValorSM

# Register your models here.

class AdminContrato(admin.ModelAdmin):
	fieldsets = [['Identidicadores', {'fields': [('numero','year'),
												'numero_en_proponente',
												('departamento','municipio')]}],
				 [u'Descripción',{'fields':['entidad_contratante',
				 										 'tipo_de_obra','objeto',
				 										 ('plazo_en_dias','fecha_terminacion')]}],
				 [u'Infomración economica',{'fields':[('valor_ejecutado'),
				 									  ('porcentaje_participacion',
				 									  	'valor_en_sm_participacion')]}],
				 [u'Archivos', {'fields':[('contrato','acuerdo_consorcial'),
				 						  ('adicional1','adicional2'),
				 						  ('acta_recibo_final','acta_liquidacion'),
				 						  ('certificacion_de_obra','certificacion_director')]}]
				]


	list_display  		= ['numero','year','departamento','municipio','objeto']
	list_filter   		= ['year','departamento','municipio','valor_ejecutado','tipo_de_obra']
	list_display_links 	= ['objeto'] 
	#list_editable = ['objeto']
	search_fields = ['year','departamento','municipio','objeto']


	class Meta:
		model = Contrato

class AdminValorSM(admin.ModelAdmin):
	list_display = ['year','valor']
	list_filter  = ['year']
	class Meta:
		model = ValorSM


admin.site.register(Contrato,AdminContrato)
admin.site.register(ValorSM,AdminValorSM)

