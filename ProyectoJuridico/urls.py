"""ProyectoJuridico URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from mainApp import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth.views import LoginView, LogoutView

import mainApp


urlpatterns = [
    path('admin/', admin.site.urls),
    path('archivo/', views.archivo),
    path('redenciones/', views.redenciones),
    path('libertades/', views.libertades),
    path('72h/', views.A_72h),
    path('tutelas/', views.tutelas),
    path('asesor/', views.asesor),
    path('guardar_funci/', views.guardar_funci, name='guardar_funci'),
    path('guardar_area/', views.guardar_area, name='guardar_area'),
    path('seccion/', views.seccion, name ='seccion'),
    path('',LoginView.as_view(template_name='index.html'),name='login')
    

    
]

urlpatterns += staticfiles_urlpatterns()
