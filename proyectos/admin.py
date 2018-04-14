from django.contrib import admin
from .models import ProyectoPrivado, ProyectoPublico


# Register your models here.

class AdminProPriavado(admin.ModelAdmin):
	list_display = ['nombre','descripcion']
	fieldsets = [['Informacion del contrato',{'fields':[('nombre','descripcion')]}],
				 ['Imagenes principales',{'fields':[('img_minatura','img_principal')]}],
				 ['Imagenes galeria',{'fields':[('img1','img2'),('img3','img4'),('img5','img6')]}]]
	class Meta:
		model = ProyectoPrivado

class AdminProPublico(admin.ModelAdmin):
	list_display = ['nombre','descripcion']
	fieldsets = [['Informacion del contrato',{'fields':[('nombre','descripcion')]}],
				 ['Imagenes principales',{'fields':[('img_minatura','img_principal')]}],
				 ['Imagenes galeria',{'fields':[('img1','img2'),('img3','img4'),('img5','img6'),'img7']}]]



	class Meta:
		model = ProyectoPublico

admin.site.register(ProyectoPublico,AdminProPublico)
admin.site.register(ProyectoPrivado,AdminProPriavado)
