"""webDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from.import views
urlpatterns = [
    path('',views.saludo,name='saludos'),# 1 argumento nombre url, sgundo nombre de nuestra funcion, y el nombre que le damos   (funcion que almacena una lista)hacemos esto para vincular nuestra funcion con Fjango 
    # arriba vinculamos nuestra funcion con django 
    path('admin/', admin.site.urls),
]
