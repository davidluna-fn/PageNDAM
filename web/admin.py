from django.contrib import admin
from .models import ImgInicio
# Register your models here.

class AdminImgInicio(admin.ModelAdmin):
	list_display = ['img1','img2']
	class Meta:
		model = ImgInicio


admin.site.register(ImgInicio,AdminImgInicio)
