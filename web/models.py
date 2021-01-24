#!/usr/bin/env python
# -*- coding: utf-8 

from django.db import models
import sys
sys.path.append("..") # Adds higher directory to python modules path.
from proyectos.models import ProyectoPrivado, ProyectoPublico

# Create your models here.

class configuracionInicio(models.Model):

	select = []
	ppublico = ProyectoPublico.objects.all()
	pprivado = ProyectoPrivado.objects.all()

	for x in ppublico:
		select.append((str(x.id)+" ProyectoPublico",u'ProyectoPublico: '+x.nombre))
	
	for y in pprivado:
		select.append((str(y.id)+" ProyectoPrivado",u'ProyectoPrivado: '+y.nombre))


	imgbanner1 =  models.CharField(max_length=1000,choices=select,verbose_name=u'Imagen de Banner 1')
	imgbanner2 =  models.CharField(max_length=1000,choices=select,verbose_name=u'Imagen de Banner 2')
	imgbanner3 =  models.CharField(max_length=1000,choices=select,verbose_name=u'Imagen de Banner 3')

	proyectoventa1 = models.CharField(max_length=1000,choices=select,verbose_name=u'Proyecto en venta 1')
	proyectoventa2 = models.CharField(max_length=1000,choices=select,verbose_name=u'Proyecto en venta 2')
	proyectoventa3 = models.CharField(max_length=1000,choices=select,verbose_name=u'Proyecto en venta 3')

	def __str__(self):
		return "img1: "



class Contacto(models.Model):
	nombre   = models.CharField(max_length=50,verbose_name=u'Nombre')
	telefono = models.IntegerField(verbose_name=u'Telefono')
	correo	 = models.EmailField(max_length=70,blank=True, null= True, unique= True)
	mensaje  = models.CharField(max_length=1000,verbose_name=u'Mensaje')

	def __str__(self):
		return self.correo
