from django.urls import path
from .views import home, eliminarPeriodista, periodistas
from . import views

urlpatterns = [
    path('', home, name='home'),
    path('eliminarPeriodista/<codigo>', views.eliminarPeriodista),
    path('periodistas', periodistas, name='periodistas')
    # path('registrarPeriodista',)
]
