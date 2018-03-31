from django.shortcuts import render
from .models import ProyectoPrivado, ProyectoPublico
import sys
sys.path.append("..") # Adds higher directory to python modules path.
from web.models import configuracionInicio
from web.forms import ContactoForm
from django.core.mail import send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.

def p_privado(request):
    objs = ProyectoPrivado.objects.all()
    
    if request.method=='POST':
        formulario = ContactoForm(request.POST)
        form = AuthenticationForm(request, data=request.POST)

        if formulario.is_valid():
            titulo = 'Mensaje de contacto NDAM'
            contenido = 'La persona: ' + formulario.cleaned_data['nombre'] +' envia el siguiente mensaje: \n'
            contenido += formulario.cleaned_data['mensaje'] + '\n'
            contenido += 'Comunicarse al correo: ' + formulario.cleaned_data['correo'] + '\n'
            contenido += 'Telefono: '+ str(formulario.cleaned_data['numero']) + '\n'
            send_mail(titulo,contenido,'dflunan@gmail.com',['dflunan@gmail.com'],fail_silently=False,)
            return HttpResponseRedirect('/')

        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)


        if form.is_valid():
            login(request, user)
            return HttpResponseRedirect('busqueda/')

    else:
        formulario = ContactoForm()
        form = AuthenticationForm()

    context = {'pPrivado':objs,'formulario':formulario,'form':form}

    return render(request,'proyectosPrivados.html',context)

def p_publico(request):
    objs = ProyectoPublico.objects.all()

    if request.method=='POST':
        formulario = ContactoForm(request.POST)
        form = AuthenticationForm(request, data=request.POST)

        if formulario.is_valid():
            titulo = 'Mensaje de contacto NDAM'
            contenido = 'La persona: ' + formulario.cleaned_data['nombre'] +' envia el siguiente mensaje: \n'
            contenido += formulario.cleaned_data['mensaje'] + '\n'
            contenido += 'Comunicarse al correo: ' + formulario.cleaned_data['correo'] + '\n'
            contenido += 'Telefono: '+ str(formulario.cleaned_data['numero']) + '\n'
            send_mail(titulo,contenido,'dflunan@gmail.com',['dflunan@gmail.com'],fail_silently=False,)
            return HttpResponseRedirect('/')

        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)


        if form.is_valid():
            login(request, user)
            return HttpResponseRedirect('busqueda/')

    else:
        formulario = ContactoForm()
        form = AuthenticationForm()
    context = {'pPublico':objs,'formulario':formulario,'form':form}

    return render(request,'proyectosPublicos.html',context)

def pPublico_detalles(request,pk):
    try:
        pPublico_id=ProyectoPublico.objects.get(pk=pk)
    except pPublico_id.DoesNotExist:
        raise Http404("Proyecto does not exist") 

    if request.method=='POST':
        formulario = ContactoForm(request.POST)
        form = AuthenticationForm(request, data=request.POST)

        if formulario.is_valid():
            titulo = 'Mensaje de contacto NDAM'
            contenido = 'La persona: ' + formulario.cleaned_data['nombre'] +' envia el siguiente mensaje: \n'
            contenido += formulario.cleaned_data['mensaje'] + '\n'
            contenido += 'Comunicarse al correo: ' + formulario.cleaned_data['correo'] + '\n'
            contenido += 'Telefono: '+ str(formulario.cleaned_data['numero']) + '\n'
            send_mail(titulo,contenido,'dflunan@gmail.com',['dflunan@gmail.com'],fail_silently=False,)
            return HttpResponseRedirect('/')

        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)


        if form.is_valid():
            login(request, user)
            return HttpResponseRedirect('busqueda/')

    else:
        formulario = ContactoForm()
        form = AuthenticationForm()

    context ={'pPublico':pPublico_id,'formulario':formulario,'form':form}    
    return render(request,'pPublico-detalles.html', context)

def pPrivado_detalles(request,pk):
    try:
        pPrivado_id=ProyectoPrivado.objects.get(pk=pk)
    except pPrivado_id.DoesNotExist:
        raise Http404("Proyecto does not exist")
    if request.method=='POST':
        formulario = ContactoForm(request.POST)
        form = AuthenticationForm(request, data=request.POST)

        if formulario.is_valid():
            titulo = 'Mensaje de contacto NDAM'
            contenido = 'La persona: ' + formulario.cleaned_data['nombre'] +' envia el siguiente mensaje: \n'
            contenido += formulario.cleaned_data['mensaje'] + '\n'
            contenido += 'Comunicarse al correo: ' + formulario.cleaned_data['correo'] + '\n'
            contenido += 'Telefono: '+ str(formulario.cleaned_data['numero']) + '\n'
            send_mail(titulo,contenido,'dflunan@gmail.com',['dflunan@gmail.com'],fail_silently=False,)
            return HttpResponseRedirect('/')

        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)


        if form.is_valid():
            login(request, user)
            return HttpResponseRedirect('busqueda/')

    else:
        formulario = ContactoForm()
        form = AuthenticationForm()

    context ={'pPrivado':pPrivado_id,'formulario':formulario,'form':form}
    return render(request,'pPrivado-detalles.html', context)

def index(request):
    pprivado = ProyectoPrivado.objects.all()
    ppublico = ProyectoPublico.objects.all()
    config   = configuracionInicio.objects.all()[0]


    banner   = []
    projects = []

    if str(config.imgbanner1.split()[1]) == 'ProyectoPublico':
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


    if request.method=='POST':
        formulario = ContactoForm(request.POST)
        form = AuthenticationForm(request, data=request.POST)

        if formulario.is_valid():
            titulo = 'Mensaje de contacto NDAM'
            contenido = 'La persona: ' + formulario.cleaned_data['nombre'] +' envia el siguiente mensaje: \n'
            contenido += formulario.cleaned_data['mensaje'] + '\n'
            contenido += 'Comunicarse al correo: ' + formulario.cleaned_data['correo'] + '\n'
            contenido += 'Telefono: '+ str(formulario.cleaned_data['numero']) + '\n'
            send_mail(titulo,contenido,'dflunan@gmail.com',['dflunan@gmail.com'],fail_silently=False,)
            return HttpResponseRedirect('/')

        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)


        if form.is_valid():
            login(request, user)
            return HttpResponseRedirect('busqueda/')

    else:
        formulario = ContactoForm()
        form = AuthenticationForm()

    context = {'banner':banner, 'projects':projects,'formulario':formulario,'form':form}
    return render(request,'home.html',context)
