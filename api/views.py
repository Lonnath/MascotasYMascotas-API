from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Mascota
@csrf_exempt
def obtener_todos(request):
    parametro = ""
    if request.GET:
        if request.GET['parametro']:
            parametro = request.GET['parametro']
    mascota_all = Mascota.objects.all().values()
    list_out = [salida for salida in mascota_all]
    if mascota_all:
        return JsonResponse({'CODIGO':1, 'MENSAJE':'Información consultada con exito.', 'DATOS' : list_out, 'PARAMETRO_GET': parametro})
    else:
        return JsonResponse({'CODIGO':1, 'MENSAJE':'No existen registros.', 'DATOS': ''})
@csrf_exempt
def obtener_no_adoptadas(request):
    no_adoptada = Mascota.objects.filter(propietario__isnull=True).values()
    list_out = [salida for salida in no_adoptada]
    if no_adoptada:
        return JsonResponse({'CODIGO':1, 'MENSAJE':'Información consultada con exito.', 'DATOS' : list_out})
    else:
        return JsonResponse({'CODIGO':1, 'MENSAJE':'No existen registros.', 'DATOS': ''})