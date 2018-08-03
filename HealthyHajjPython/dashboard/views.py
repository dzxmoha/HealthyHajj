import datetime
import smtplib

from django.core.mail import send_mail
from django.http import HttpResponse
from django.http import FileResponse
from django.utils import timezone
from datetime import date, timedelta

import xlwings as xw
from dashboard.models import *
from django.shortcuts import render,redirect
from .forms import *
from django.contrib.auth import views as auth_views, authenticate,get_user
from django.shortcuts import get_object_or_404
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase.pdfmetrics import stringWidth
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm

AGE_TAILE = (75, 85, 95, 100, 105, 110, 115, 120, 128, 132, 140, 145, 150, 155, 163, 168, 171, 175)
AGE_POID = (5,30,46,48,50,52,54,56,58,62,65,70,75,80,84,86,88,88)


def firstpage(request):
    return render(request,'dashboard/index.html')
def cree_patient(request):
    form=Hajj_Form(request.POST or None)
    envoi=False
    if form.is_valid():
        nom=form['nom'].value()
        prenom=form['prenom'].value()
        date_de_naissance = form['dat$wwe_dN'].value()
        sexe = form['sexe'].value()
        blodtype = form['boldType'].value()
        contry = form['contry'].value()
        p=hajj.objects.create(nom=nom,prenom=prenom,date_de_naissance=date_de_naissance,sexe=sexe,blodtype=blodtype,contry=contry)
        return redirect('bilan_generale',p.id)

    return render(request,"dashboard/medecin/cree_patient.html",locals())

def dossier(request,id_patient):
    p=hajj.objects.get(pk=id_patient)
    d=p.dossier
    return render(request,'dashboard/medecin/patient.html',locals())

def consulter_patient(request):
    patients=hajj.objects.all();
    return  render(request,"dashboard/medecin/consulter_patient.html",{'patients':patients,})





def bilan_generale(request,id_patient):
    p=hajj.objects.get(pk=id_patient)
    form = BilanForm(request.POST or None)
    if form.is_valid():
        daibete = form["diabete"].value()
        tesion = form["tension"].value()
        canser = form["canser"].value()
        cardiopathie = form["cardiopathie"].value()
        bronchite = form["bronchite"].value()
        allergie = form["allergie"].value()
        neurologie = form["neurologie"].value()


        autre = form["autre"].value()

        d=Dossier.objects.create(diabete=daibete,tesion=tesion,canser=canser,cardiopathie=cardiopathie,bronchite=bronchite,allergie=allergie,neurologie=neurologie,autre=autre)
        p.dossier=d
        p.save()
        return redirect('consulter_patient')


    return render(request, "dashboard/medecin/bilan_gene.html", locals(),)




