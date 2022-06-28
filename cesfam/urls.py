"""cesfam URL Configuration

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
from django.conf.urls import static
from django.conf import global_settings as configuracion
from django.urls import path, include

from cesfam.settings import STATIC_URL

urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuarios/', include('modulo.usuario.urls')),
    path('prescripcion/', include('modulo.prescripcion.urls')),
]

if configuracion.DEBUG == True:
    urlpatterns += static(configuracion.STATIC_URL, document_root= configuracion.STATIC_ROOT)
