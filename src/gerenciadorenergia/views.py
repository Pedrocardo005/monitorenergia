from django.core.handlers.wsgi import WSGIRequest
from django.views.decorators.csrf import csrf_exempt
from django.http.response import HttpResponse
from django.forms.models import model_to_dict
from django.shortcuts import render
from django.core.cache import cache
from django.http import JsonResponse
from django.utils import timezone
from datetime import timedelta
import json

from gerenciadorenergia.models import InfoConsumo
from gerenciadorenergia.utils import Utils

# Create your views here.

def index(request: WSGIRequest):
    return render(request, "index.html")

@csrf_exempt
def register(request: WSGIRequest):
    try:
        data = {}
        if request.method == 'POST':

            elemento = json.loads(request.body)
            nome_dispositivo=elemento['nome_dispositivo']
            consumo=float(elemento['consumo'])
            corrente=float(elemento['corrente'])

            new_info_consumo = InfoConsumo(
                nome_dispositivo=nome_dispositivo,
                consumo=consumo,
                corrente=corrente
            )

            new_info_consumo.save()

            cache.set("current_device", nome_dispositivo, timeout=180)

            data = model_to_dict(new_info_consumo)
        return JsonResponse(status=200, data=data)
    except Exception as error:
        print('Erro', error)
        return HttpResponse(request, status=500)
    
@csrf_exempt
def get_all(request: WSGIRequest):
    try:
        lista = []
        for info in InfoConsumo.objects.all():

            date_time = info.date_time.astimezone(timezone.get_current_timezone())
            lista.append({
                'nome_dispositivo': info.nome_dispositivo,
                'consumo': info.consumo,
                'corrente': info.corrente,
                'date_time': date_time.strftime("%d/%m/%Y %H:%M:%S")
            })
        return JsonResponse(status=200, data=lista, safe=False)
    except Exception as error:
        print('Erro', error)
        return JsonResponse(status=500, data={'error': 'Algum erro ocorreu'})
    
@csrf_exempt
def get_all_formated(request: WSGIRequest, formatacao: str):
    try:
        listing = {}

        if formatacao == 'minute':
            current_date_hour = timezone.now()
            start_minute = current_date_hour - timedelta(minutes=1)
            results = InfoConsumo.objects.filter(date_time__gte=start_minute)
            listing['items'] = []
            for result in results:
                listing['items'].append({
                    'nome': result.nome_dispositivo,
                    'consumo': result.consumo,
                    'tempo': result.date_time.strftime("%S")
                })

        if formatacao == 'hour':
            current_date_hour = timezone.now()
            start_hours = current_date_hour - timedelta(hours=1)
            results = InfoConsumo.objects.filter(date_time__gte=start_hours).order_by('date_time')
            listing = Utils.get_list_consumo(results, 10, "M")

        if formatacao == 'day':
            current_date_hour = timezone.now()
            start_hours = current_date_hour - timedelta(days=1)
            results = InfoConsumo.objects.filter(date_time__gte=start_hours).order_by('date_time')
            listing = Utils.get_list_consumo(results, 40, "H")

        if formatacao == 'week':
            current_date_hour = timezone.now()
            start_hours = current_date_hour - timedelta(weeks=1)
            results = InfoConsumo.objects.filter(date_time__gte=start_hours).order_by('date_time')
            listing = Utils.get_list_consumo(results, 100, "d")

        listing['current_device'] = cache.get("current_device")
        
        return JsonResponse(status=200, data=listing, safe=False)
    except Exception as error:
        print('Erro', error)
        return JsonResponse(status=500, data={'error': 'Algum erro ocorreu'})
    