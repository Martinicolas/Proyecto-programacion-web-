"""
URL configuration for ProjecNoticias project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from core import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name="home"),
    path('nosotros', views.nosotros, name="periodistass"),
    path('contacto', views.contacto, name="contacto"),
    path('sesion', views.sesion, name="sesion"),
    path('productos', views.productos, name="productos"),
    path('carrito', views.carrito, name="carrito"),
    path('periodistas', views.periodistas, name="periodistas"),
    path('eliminarPeriodista/<codigo>', views.eliminarPeriodista),
    path('editarPeriodista/<codigo>/', views.editarPeriodista),
    path('admin/', admin.site.urls),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
