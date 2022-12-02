from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
# Create your views here.
from rest_framework.decorators import (api_view, permission_classes,
                                       authentication_classes)
from rest_framework.response import Response
# Create your views here.
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import (TokenAuthentication,
                                           SessionAuthentication,
                                           BasicAuthentication)
from rest_framework import status
import time
import pytz
import datetime
import requests
import json

@api_view(['GET'])
def obtener_objetos_aleatorios(request):
    elementos=[]
    bandera=False
    if request.method == 'GET':
        for i in range(1, 20):#colocar 26
            datos_api=consumir_api()
            datos_api=json.loads(datos_api)
            if (len(elementos)>0):
                for x in elementos:
                    if (x["id"]==datos_api["id"]):
                        bandera=True
                if not (bandera):
                    elementos.append(datos_api)
            else:
                elementos.append(datos_api)
        return Response({'valores': elementos})



def consumir_api():
    url = "https://api.chucknorris.io/jokes/random"

    headers = {
        'cache-control': "no-cache",
        'postman-token': "2a9f8edf-9d88-930b-8b00-a58b806e6bc0"
        }

    response = requests.request("GET", url, headers=headers)

    return response.text