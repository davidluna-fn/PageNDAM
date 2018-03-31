from django.shortcuts import render, render_to_response, get_object_or_404
from .models import configuracionInicio
from .models import Contacto
from .forms import ContactoForm
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.core.mail import send_mail
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.





def sobreNosotros(request):
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
            return HttpResponseRedirect('/busqueda/')
    else:
        formulario = ContactoForm()
        form = AuthenticationForm()
        
    return render(request,'sobreNosotros.html',{'formulario':formulario,'form':form})


def contacto(request):
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
    return render(request,'contacto.html',{'formulario':formulario,'form':form})