#!/usr/bin/env python
# -*- coding: utf-8 

from django.db import models

# Create your models here.

class ProyectoPrivado(models.Model):
	nombre 			= models.CharField(max_length=200,verbose_name=u'Nombre')
	descripcion 	= models.CharField(max_length=200,verbose_name=u'Descripción')
	img_minatura 	= models.ImageField(upload_to = 'img_proyectos/',verbose_name=u'Imagen principal')
	img_principal 	= models.ImageField(upload_to = 'img_proyectos/',verbose_name=u'Imagen banner', null=True, blank=True)
	img1 			= models.FileField(upload_to='img_proyectos/',blank=True, null=True)
	img2 			= models.FileField(upload_to='img_proyectos/',blank=True, null=True)
	img3 			= models.FileField(upload_to='img_proyectos/',blank=True, null=True)
	img4 			= models.FileField(upload_to='img_proyectos/',blank=True, null=True)
	img5 			= models.FileField(upload_to='img_proyectos/',blank=True, null=True)
	img6 			= models.FileField(upload_to='img_proyectos/',blank=True, null=True)
	resaltar 		= models.BooleanField(default=False)
	plus_mensaje 	= models.CharField(max_length=20, blank=True, null=True)
	tipo_propiedad	= models.CharField(max_length=20, blank=True,null=True)
	area			= models.DecimalField(max_digits=5, decimal_places=2, blank=True,null=True,verbose_name=u'Area')
	ubicacion		= models.CharField(max_length=20, blank=True,null=True) 
	tipo_negocio	= models.CharField(max_length=20, blank=True,null=True)
	parqueadero		= models.BooleanField(default=False)
	parqueadero_visitantes	= models.BooleanField(default=False)
	year			= models.IntegerField(blank=True,null=True,verbose_name=u'Año')
	zonas_verdes	= models.BooleanField(default=False)


	def get_absolute_url(self):
		return "/pPrivado/%i/" % self.id


class ProyectoPublico(models.Model):
	id = models.AutoField(primary_key=True)
	nombre 			= models.CharField(max_length=200,verbose_name=u'Nombre')
	descripcion 	= models.CharField(max_length=200,verbose_name=u'Descripción')
	img_minatura 	= models.ImageField(upload_to = 'img_proyectos/',verbose_name=u'Imagen principal')
	img_principal 	= models.ImageField(upload_to = 'img_proyectos/',verbose_name=u'Imagen banner', null=True, blank=True)
	img1 		= models.FileField(upload_to='img_proyectos/',blank=True, null=True)
	img2 		= models.FileField(upload_to='img_proyectos/',blank=True, null=True)
	img3 		= models.FileField(upload_to='img_proyectos/',blank=True, null=True)
	img4 		= models.FileField(upload_to='img_proyectos/',blank=True, null=True)
	img5 		= models.FileField(upload_to='img_proyectos/',blank=True, null=True)
	img6 		= models.FileField(upload_to='img_proyectos/',blank=True, null=True)
	img7 		= models.FileField(upload_to='img_proyectos/',blank=True, null=True)
	def get_absolute_url(self):
		return "/pPublico/%i/" % self.id	