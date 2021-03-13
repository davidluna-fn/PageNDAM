from django.shortcuts import render
from django.http import HttpResponse
from .models import Contrato, ValorSM
from .filters import ContratosFilter
from django.views import generic


from contratos.utils import render_to_pdf
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.views.generic import View
from django.views import generic
from django.template.loader import get_template

from datetime import date

def SetMoneda(num, simbolo="US$", n_decimales=2):
    """Convierte el numero en un string en formato moneda
    SetMoneda(45924.457, 'RD$', 2) --> 'RD$ 45,924.46'     
    """
    #con abs, nos aseguramos que los dec. sea un positivo.
    n_decimales = abs(n_decimales)
    print(n_decimales,type(n_decimales))
    #se redondea a los decimales idicados.
    num = round(num, n_decimales)

    #se divide el entero del decimal y obtenemos los string
    num, dec = str(num).split(".")

    #si el num tiene menos decimales que los que se quieren mostrar,
    #se completan los faltantes con ceros.
    dec += "0" * (n_decimales - len(dec))
    
    #se invierte el num, para facilitar la adicion de comas.
    num = num[::-1]
    
    #se crea una lista con las cifras de miles como elementos.
    l = [num[pos:pos+3][::-1] for pos in range(0,50,3) if (num[pos:pos+3])]
    l.reverse()
    
    #se pasa la lista a string, uniendo sus elementos con comas.
    num = str.join(",", l)
    
    #si el numero es negativo, se quita una coma sobrante.
    try:
        if num[0:2] == "-,":
            num = "-%s" % num[2:]
    except IndexError:
        pass
    
    #si no se especifican decimales, se retorna un numero entero.
    if not n_decimales:
        return "%s %s" % (simbolo, num)
        
    return "%s %s.%s" % (simbolo, num, dec)

def search(request):
    contrato_list = Contrato.objects.all()
    SM = ValorSM.objects.all()

    vsm = {}
    vpesos = {}
    for i in range(len(SM)):
        vsm[str(SM[i].year)] = SM[i].valor


    contrato_filter = ContratosFilter(request.GET, queryset=contrato_list)
    context = {'filter':contrato_filter, 'date':date.today, 'user':request.user.username}

    page = request.GET.get('page', 1)

    paginator = Paginator(contrato_filter.qs, 10)
    try:
        cto_filter = paginator.get_page(page)
    except PageNotAnInteger:
        cto_filter = paginator.get_page(page(1))
    except EmptyPage:
        cto_filter = paginator.get_page(page(paginator.num_pages))

    for i in cto_filter:
        try:
            if i.fecha_terminacion.year < date.today().year:
                i.valor_ejecutado = round((i.valor_ejecutado/vsm[str(i.year)])*vsm[str(date.today().year)],2)
                i.valor_en_sm = round(i.valor_ejecutado /vsm[str(date.today().year)],2)
                i.valor_en_sm_participacion = i.valor_en_sm * i.porcentaje_participacion
                i.valor_ejecutado_participacion = round((i.valor_ejecutado * i.porcentaje_participacion),2)
            else:
                i.valor_en_sm = round(i.valor_ejecutado /vsm[str(i.year)],2)
                i.valor_en_sm_participacion = i.valor_en_sm * i.porcentaje_participacion
                i.valor_ejecutado_participacion = round((i.valor_ejecutado * i.porcentaje_participacion),2)

                i.valor_ejecutado = SetMoneda(i.valor_ejecutado,"$",2)
                i.valor_en_sm = SetMoneda(i.valor_en_sm,"",2)
                i.valor_en_sm_participacion = SetMoneda(i.valor_en_sm_participacion,"",2)
                i.valor_ejecutado_participacion = SetMoneda(i.valor_ejecutado_participacion,"$",2)
        except:
            continue





    if request.GET:
        if 'pdf' in request.GET:
            template = get_template('invoice.html')
            for i in context['filter'].qs:
                try:
                    i.valor_ejecutado = round((i.valor_ejecutado/vsm[str(i.year)])*vsm[str(date.today().year)],2)
                    i.valor_ejecutado_participacion = round((i.valor_ejecutado * i.porcentaje_participacion),2)
                    i.valor_ejecutado = SetMoneda(i.valor_ejecutado,"$",2)
                    i.valor_ejecutado_participacion = SetMoneda(i.valor_ejecutado_participacion,"$",2)
                    i.porcentaje_participacion = str(round(i.porcentaje_participacion*100,2))+'%'
                except:
                    continue
            
            html = template.render(context)
            pdf = render_to_pdf('invoice.html', context)
            if pdf:
                response = HttpResponse(pdf, content_type='application/pdf')
                filename = "Invoice_%s.pdf" %("12341231")
                content = "inline; filename='%s'" %(filename)
                download = request.GET.get("download")
                if download:
                    content = "attachment; filename='%s'" %(filename)
                response['Content-Disposition'] = content
                return response
            return HttpResponse("Not found")

    if request.user.is_authenticated:
        return render(request, 'busqueda_contratos.html', {'filter': cto_filter,'filterqs' : contrato_filter})
        #return render(request, 'busqueda_contratos.html', {'filter': contrato_filter,'filterqs' : contrato_filter})
    else:
        return HttpResponse('Debe iniciar sesion para poder buscar contratos')


def contrato_detail_view(request,pk):
    if request.user.is_authenticated:
        try:
            SM = ValorSM.objects.all()
            vsm = {}
            for i in range(len(SM)):
                vsm[str(SM[i].year)] = SM[i].valor

            contrato_id=Contrato.objects.get(pk=pk)
            contrato_id.valor_en_sm = SetMoneda(round(contrato_id.valor_ejecutado /vsm[str(date.today().year)],2),"",2)
            contrato_id.valor_ejecutado = SetMoneda(contrato_id.valor_ejecutado,"$",2)
            contrato_id.porcentaje_participacion = str(round(contrato_id.porcentaje_participacion*100,2))+"%"
            
        except Contrato.DoesNotExist:
            raise Http404("Contratos does not exist")
        return render(request,'Contrato_detail.html', context={'contrato':contrato_id,})
    else:
        return HttpResponse('Debe iniciar sesion para poder buscar contratos')



