from django.shortcuts import render
from produto.models import Deposito
from django.http import JsonResponse

def deposito(request):
    deposito = Deposito.objects.all()        # pylint: disable=no-member   
    return JsonResponse(deposito)
