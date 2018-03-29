from django.shortcuts import render
from .models import ProyectoPrivado, ProyectoPublico
import sys
sys.path.append("..") # Adds higher directory to python modules path.
from web.models import configuracionInicio


# Create your views here.

def p_privado(request):
	objs = ProyectoPrivado.objects.all()
	context = {'pPrivado':objs}
	return render(request,'proyectosPrivados.html',context)

def p_publico(request):
	objs = ProyectoPublico.objects.all()
	context = {'pPublico':objs}
	return render(request,'proyectosPublicos.html',context)

def pPublico_detalles(request,pk):
    try:
        pPublico_id=ProyectoPublico.objects.get(pk=pk)
    except pPublico_id.DoesNotExist:
        raise Http404("Proyecto does not exist")    
    return render(request,'pPublico-detalles.html', context={'pPublico':pPublico_id,})

def pPrivado_detalles(request,pk):
    try:
        pPrivado_id=ProyectoPrivado.objects.get(pk=pk)
    except pPrivado_id.DoesNotExist:
        raise Http404("Proyecto does not exist")    
    print(pPrivado_id)
    return render(request,'pPrivado-detalles.html', context={'pPrivado':pPrivado_id,})

def index(request):
    pprivado = ProyectoPrivado.objects.all()
    ppublico = ProyectoPrivado.objects.all()
    config   = configuracionInicio.objects.all()[0]

    print(pprivado)
    banner   = []
    projects = []

    if config.imgbanner1.split()[1] == 'ProyectoPublico':
        banner.append(ppublico[int(config.imgbanner1.split()[0])-1])
    else:
        banner.append(pprivado[int(config.imgbanner1.split()[0])-1])

    if config.imgbanner2.split()[1] == 'ProyectoPublico':
        banner.append(ppublico[int(config.imgbanner2.split()[0])-1])
    else:
        banner.append(pprivado[int(config.imgbanner2.split()[0])-1])

    if config.imgbanner3.split()[1] == 'ProyectoPublico':
        banner.append(ppublico[int(config.imgbanner3.split()[0])-1])
    else:
        banner.append(pprivado[int(config.imgbanner3.split()[0])-1])

    if config.proyectoventa1.split()[1] == 'ProyectoPublico':
        projects.append(ppublico[int(config.proyectoventa1.split()[0])-1])
    else:
        projects.append(pprivado[int(config.proyectoventa1.split()[0])-1])

    if config.proyectoventa2.split()[1] == 'ProyectoPublico':
        projects.append(ppublico[int(config.proyectoventa2.split()[0])-1])
    else:
        projects.append(pprivado[int(config.proyectoventa2.split()[0])-1])

    if config.proyectoventa3.split()[1] == 'ProyectoPublico':
        projects.append(ppublico[int(config.proyectoventa3.split()[0])-1])
    else:
        projects.append(pprivado[int(config.proyectoventa3.split()[0])-1])

    context = {'banner':banner, 'projects':projects}
    return render(request,'home.html',context)
