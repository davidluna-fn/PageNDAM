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



def search(request):
    contrato_list = Contrato.objects.all()
    SM = ValorSM.objects.all()

    vsm = {}
    for i in range(len(SM)):
        vsm[str(SM[i].year)] = SM[i].valor




    contrato_filter = ContratosFilter(request.GET, queryset=contrato_list)
    context = {'filter':contrato_filter, 'date':date.today, 'user':request.user.username}

    page = request.GET.get('page', 1)

    paginator = Paginator(contrato_filter.qs, 100)
    try:
        cto_filter = paginator.page(page)
    except PageNotAnInteger:
        cto_filter = paginator.page(1)
    except EmptyPage:
        cto_filter = paginator.page(paginator.num_pages)

    for i in cto_filter:
        i.valor_en_sm_participacion = round(i.valor_ejecutado /vsm[str(i.year)],2)


    if request.GET:
        if 'pdf' in request.GET:
            template = get_template('invoice.html')
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
            contrato_id=Contrato.objects.get(pk=pk)
        except Contrato.DoesNotExist:
            raise Http404("Contratos does not exist")
        return render(request,'Contrato_detail.html', context={'contrato':contrato_id,})
    else:
        return HttpResponse('Debe iniciar sesion para poder buscar contratos')