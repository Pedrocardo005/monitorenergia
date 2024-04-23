from django.core.handlers.wsgi import WSGIRequest
from django.views.decorators.csrf import csrf_exempt
from django.http.response import HttpResponse
from django.forms.models import model_to_dict
from django.shortcuts import render
from django.http import JsonResponse
import json

from gerenciadorenergia.models import InfoConsumo

# Create your views here.

def index(request: WSGIRequest):
    return render(request, "index.html")

@csrf_exempt
def register(request: WSGIRequest):
    try:
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
            
            data = model_to_dict(new_info_consumo)
        return JsonResponse(status=200, data=data)
    except Exception as error:
        print('Erro', error)
        return HttpResponse(request, status=500)
