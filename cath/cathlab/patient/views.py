from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import *


def get(request):
    patient=Patient.objects.get(id=5)
    for procedure in patient.procedure():
        {'procedure':procedure}
        operator=patient.operator
        {'operator':operator}

        context={}

    return render (request, "home.html", context)

def show_angio(request, sudo_id):
    sudo=Patient.objects.get(pk=sudo_id),
    return render(request, 'show_angio.html',
        {'sudo': sudo})
      
def list_venues(request):
    venue_list=Patient.objects.all()
    return render(request, 'angio.html',
        {'venue_list': venue_list})
         
def patient_detail_view(request):
    obj=Patient.objects.all()
    obj2=Procedure.objects.all()

    context={
        'object':obj,
        'object2':obj2
   
    
    }
    return render(request, "detail.html", context) 


    
