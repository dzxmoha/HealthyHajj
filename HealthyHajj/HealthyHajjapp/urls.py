from django.urls import path, include
from . import views
from django.contrib.auth.views import login, logout

appname = 'HealthyHajjapp'

urlpatterns = [

    path ('',views.index, name = 'index')
]