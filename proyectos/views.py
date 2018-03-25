from django.shortcuts import render
from .models import ProyectoPrivado, ProyectoPublico


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
    imgs = ProyectoPrivado.objects.all()
    obj = []
    for i in imgs:
        if i.mostrar_al_inicio == True:
            obj.append(i)
    context = {'img':obj}
    return render(request,'home.html',context)
