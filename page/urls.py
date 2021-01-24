"""page URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from contratos import views
from web import views as wviews
from proyectos import views as pviews


urlpatterns = [
	#path('web/', include('web.urls')),
    path('admin/', admin.site.urls),
    path('busqueda/', views.search, name='busqueda_contratos'),
    path('sobreNosotros/busqueda/', views.search, name='busqueda_contratos'),
    path('proyectosPrivados/busqueda/', views.search, name='busqueda_contratos'),
    path('proyectosPublicos/busqueda/', views.search, name='busqueda_contratos'),
    path('',pviews.index,name='index'),
    url(r'^login/$', auth_views.LoginView.as_view(template_name= 'login.html'), name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(next_page= 'index'), name='logout'),
    url(r'^contrato/(?P<pk>\d+)/$', views.contrato_detail_view, name='contrato-detalles'),
    url(r'^contacto/$',wviews.contacto, name='contacto'),
    url(r'^sobreNosotros/$',wviews.sobreNosotros, name='sobreNosotros'),
    url(r'^proyectosPrivados/$',pviews.p_privado, name='proyectosPrivados'),
    url(r'^proyectosPublicos/$',pviews.p_publico, name='proyectosPublicos'),
    url(r'^pPublico/(?P<pk>\d+)/$', pviews.pPublico_detalles, name='pPublicos-detalles'),  
    url(r'^pPrivado/(?P<pk>\d+)/$', pviews.pPrivado_detalles, name='pPrivados-detalles'),  
    ]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL,  document_root = settings.MEDIA_ROOT)