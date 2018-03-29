#!/usr/bin/env python
# -*- coding: utf-8 

from django.db import models

# Create your models here.

class ProyectoPrivado(models.Model):
	nombre 			= models.CharField(max_length=200,verbose_name=u'Nombre')
	descripcion 	= models.CharField(max_length=200,verbose_name=u'Descripción')
	img_minatura 	= models.ImageField(upload_to = 'img_proyectos/')
	img_principal 	= models.ImageField(upload_to = 'img_proyectos/', null=True, blank=True)
	img1 		= models.FileField(upload_to='img_proyectos/',blank=True, null=True)
	img2 		= models.FileField(upload_to='img_proyectos/',blank=True, null=True)
	img3 		= models.FileField(upload_to='img_proyectos/',blank=True, null=True)
	img4 		= models.FileField(upload_to='img_proyectos/',blank=True, null=True)
	img5 		= models.FileField(upload_to='img_proyectos/',blank=True, null=True)
	img6 		= models.FileField(upload_to='img_proyectos/',blank=True, null=True)
	img7 		= models.FileField(upload_to='img_proyectos/',blank=True, null=True)
	img8 		= models.FileField(upload_to='img_proyectos/',blank=True, null=True)
	img9 		= models.FileField(upload_to='img_proyectos/',blank=True, null=True)
	img10 		= models.FileField(upload_to='img_proyectos/',blank=True, null=True)
	mostrar_al_inicio = models.BooleanField(default=False)
	def get_absolute_url(self):
		return "/pPrivado/%i/" % self.id


class ProyectoPublico(models.Model):
	nombre 			= models.CharField(max_length=200,verbose_name=u'Nombre')
	descripcion 	= models.CharField(max_length=200,verbose_name=u'Descripción')
	img_minatura 	= models.ImageField(upload_to = 'img_proyectos/')
	img_principal 	= models.ImageField(upload_to = 'img_proyectos/', null=True, blank=True)
	img1 		= models.FileField(upload_to='img_proyectos/',blank=True, null=True)
	img2 		= models.FileField(upload_to='img_proyectos/',blank=True, null=True)
	img3 		= models.FileField(upload_to='img_proyectos/',blank=True, null=True)
	img4 		= models.FileField(upload_to='img_proyectos/',blank=True, null=True)
	img5 		= models.FileField(upload_to='img_proyectos/',blank=True, null=True)
	img6 		= models.FileField(upload_to='img_proyectos/',blank=True, null=True)
	img7 		= models.FileField(upload_to='img_proyectos/',blank=True, null=True)
	img8 		= models.FileField(upload_to='img_proyectos/',blank=True, null=True)
	img9 		= models.FileField(upload_to='img_proyectos/',blank=True, null=True)
	img10 		= models.FileField(upload_to='img_proyectos/',blank=True, null=True)
	mostrar_al_inicio = models.BooleanField(default=False)
	def get_absolute_url(self):
		return "/pPublico/%i/" % self.id	