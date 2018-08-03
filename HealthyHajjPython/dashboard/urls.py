from django.urls import path

from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    #//////////////////////////ALL//////////////////////////////////////////////
    path('', views.firstpage, name='first_page'),


    #//////////////////////////////MEDECIN///////////////////////////////////////////

    path('admin/bilan', views.bilan_generale, name='bilan_generale'),



    path('admin/cree_patient/', views.cree_patient, name='cree_patient'),
    path('admin/consulter_patient/', views.consulter_patient, name='consulter_patient'),

    path('admin/consulter_patient/<int:id_patient>', views.dossier, name='dossier'),

    path('admin/cree_patient/<int:id_patient>/bilan', views.bilan_generale, name='bilan_generale'),




]
