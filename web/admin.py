from django.contrib import admin
from .models import configuracionInicio
# Register your models here.

class AdminConfiguracionInicio(admin.ModelAdmin):
	list_display = ['imgbanner1','imgbanner2','imgbanner3']
	class Meta:
		model = configuracionInicio


admin.site.register(configuracionInicio,AdminConfiguracionInicio)
