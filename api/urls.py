from django.urls import path
from api import views


urlpatterns = [
    path('ObtenerObjectosAleatorios/', views.obtener_objetos_aleatorios),
]