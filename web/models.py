from django.db import models

# Create your models here.

class ImgInicio(models.Model):
	img1 = models.ImageField(upload_to = 'pic_folder/')
	img2 = models.ImageField(upload_to = 'pic_folder/')

	def __str__(self):
		return "img1: "+ str(self.img1) + "img2: " + str(self.img2)


class Contacto(models.Model):
	nombre   = models.CharField(max_length=50,verbose_name=u'Nombre')
	telefono = models.IntegerField(verbose_name=u'Telefono')
	correo	 = models.EmailField(max_length=70,blank=True, null= True, unique= True)
	mensaje  = models.CharField(max_length=1000,verbose_name=u'Mensaje')

	def __str__(self):
		return self.correo