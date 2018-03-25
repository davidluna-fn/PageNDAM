from django.contrib import admin
from .models import ProyectoPrivado, ProyectoPublico


# Register your models here.

class AdminProPriavado(admin.ModelAdmin):
	list_display = ['nombre','descripcion']
	class Meta:
		model = ProyectoPrivado

class AdminProPublico(admin.ModelAdmin):
	list_display = ['nombre','descripcion']
	class Meta:
		model = ProyectoPublico

admin.site.register(ProyectoPublico,AdminProPublico)
admin.site.register(ProyectoPrivado,AdminProPriavado)
