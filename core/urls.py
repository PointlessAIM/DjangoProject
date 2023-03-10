"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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

from .views import HomeView

urlpatterns = [
    path("admin/", admin.site.urls),

    # Aquí se le indica a Django que cuando se haga una petición al servidor, se va a
    # ejecutar la función HomeView.as_view(), que es la que se encarga de manejar las
    # peticiones HTTP que llegan al servidor y devolver una respuesta HTTP.
    # Escribimos homeview.as_view() porque es una clase, y para que se ejecute como una
    # función, se le agrega el .as_view()    
    path("",HomeView.as_view(), name="home"),

    # La dirección blog/ se va a manejar con el archivo urls.py que se encuentra en la
    # carpeta blog, y se le va a agregar el namespace "blog" para que no haya conflictos
    # con las urls de otras aplicaciones.
    # El namespace es como un prefijo que se le agrega a las urls de la aplicación
    # La función include() se encarga de incluir las urls de otra aplicación
    path('blog/', include('blog.urls', namespace='blog'))
]
