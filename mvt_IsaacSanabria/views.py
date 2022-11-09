from django.http import HttpResponse
from django.template import Template, Context, loader
from desafio_mvt.models import List
from datetime import datetime

def family(request):
    list= List.objects.all()
    list_fam={"list":list}
    mihtml= open(r".\mvt_IsaacSanabria\templates\family_list.html")
    plantilla=Template(mihtml.read())
    mihtml.close()
    micontext= Context(list_fam)
    documento= plantilla.render(micontext)
    
    return HttpResponse(documento)