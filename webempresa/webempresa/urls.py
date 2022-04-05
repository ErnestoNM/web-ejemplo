"""webempresa URL Configuration

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
from django.urls import path, include
from django.conf import settings #Cargar las configuraciones nuevas

urlpatterns = [
    #paths del core
    path('', include('core.urls')),
    #path de services
    path('services/', include('services.urls')),
    #path de blog
    path('blog/', include('blog.urls')),
    #paths del admin
    path('admin/', admin.site.urls),
]

"""
Por defecto Django no permite en fase de desarrollo cargar imágenes y otro tipo
de archivos, la siguiente configuración esque mientras el DEBUG está activado
permita este tipo de archivos.
"""

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
