from django.urls import path
from django.urls.resolvers import URLPattern
from .views import obtener_todos, obtener_no_adoptadas
urlpatterns = {
    path('mascotas', obtener_todos, name='lista_mascotas' ),
    path('mascotas_no_adoptadas', obtener_no_adoptadas, name='lista_no_adoptadas' ),
}