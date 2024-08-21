from django.shortcuts import render
from django.http import JsonResponse
import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt, csrf_protect
import requests
# from .models import Book

@csrf_exempt
def addNumber(request):
    #numbers = {"numbers":[1,2,3]}
    data1 = json.loads(request.body)
    add = data1.get('numbers')
    return JsonResponse({"The sum of the numbers is":sum(add)})

@csrf_exempt
def averageNumber(request):
    #numbers2 = {"numbers":[1,2,3]}
    data2 = json.loads(request.body)
    foraverage = data2.get('numbers')
    sum2 = sum(foraverage)
    length = len(foraverage)
    average = sum2/length
    return JsonResponse({"The average of the numbers is":average})

@csrf_exempt
def productNumber(request):
#    numbers2 = {"numbers":[8,3]}
    product = 1
    data3 = json.loads(request.body)
    forproduct = data3.get('numbers')
    for i in range(0,len(forproduct)):
        product = product * forproduct[i]
    return JsonResponse({"The average of the numbers is":product})

