from django.shortcuts import render
from django.http import JsonResponse
import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt, csrf_protect
import requests
from . import util
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
    return JsonResponse({"The Product of the numbers is":product})

'''@csrf_exempt
def executefile(request):
    data = json.loads(request.body)
    data2 = data.get('code')
    #data3 = exec(data2)
    data4 = util.send(data2)
    return JsonResponse({"Output":data4})'''

@csrf_exempt
def split_evenly(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        person = data.get('person',0)
        total = data.get('total',0)
        splitevenly = total/person
        return JsonResponse({'split':splitevenly})
    
@csrf_exempt
def split_unevenly(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        total = data.get('total',0)
        person = data.get('person',[])
        split = total/len(person)
        unevenlysplit = {}
        for people in person:
            unevenlysplit[people["name"]] = people["contribution"] - split
        return JsonResponse({'split':unevenlysplit})
    
@csrf_exempt
def split_including_tip_and_tax(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        total = data.get('total',0)
        totalperson = data.get('totalperson',0)
        tip = data.get('tip',0)
        tax = data.get('tax',0)
        new_tip = total * tip / 100
        new_tax = total * tax / 100
        total += new_tip + new_tax
        splitwithtipandtax = total/totalperson
        return JsonResponse({'split':splitwithtipandtax})

@csrf_exempt
def split_with_discount(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        total = data.get('total',0)
        totalpeople = data.get('totalpeople',0)
        discount = data.get('discount',0)
        new_discount = total * (100 - discount) / 100
        splitwithdiscount = new_discount / totalpeople
        return JsonResponse({'split with discount': splitwithdiscount})
    
@csrf_exempt
def split_with_shareditems(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        items = data.get('items',[])
        person = data.get('person',[])
        tip = data.get('tip',0)
        tax = data.get('tax',0)

        amount = 0
        numberofperson = 0

        for paise in items:
            amount += paise['price']

        for log in person:
            numberofperson = numberofperson + 1

        new_tip = amount * tip / 100
        new_tax = amount * tax / 100
        amount += new_tip + new_tax

        people = []
        count = 0
        split = {}
        for item in items:
            for persons in person:
                if item['buy'] == persons['item']:
                    total = item['price']
                    count = count + 1
                    people.append(persons)

            new_tip = total * tip / 100
            new_tax = total * tax / 100
            total += new_tip + new_tax
            new_total = total / count
            for persons2 in people:
                split[persons2['name']] = new_total - persons2['contribution']
            people = []
            total = 0    
            count = 0
        return JsonResponse({'Total_amount_after_adding_tip_and_tax_and_prices_of_all_items':amount,'split':split})

# For last function (split_with_shareditems) Please enter input in this form:
# {
#   "tip":5,
#   "tax":20,
#   "person": [
#     {
#       "name": "saad",
#       "contribution": 300,
#       "item": "pizza"
#     },
#     {
#       "name": "hammad",
#       "contribution": 850,
#       "item": "pizza"
#     },
#     {
#       "name": "ghafoor",
#       "contribution": 100,
#       "item": "pizza"
#     },
#     {
#       "name": "umar",
#       "contribution": 1400,
#       "item": "burger"
#     },
#     {
#       "name": "Ahmed",
#       "contribution": 1100,
#       "item": "burger"
#     }
#   ],
#   "items": [
#     {
#       "buy": "pizza",
#       "price": 1000
#     },
#     {
#       "buy": "burger",
#       "price": 2000
#     }
#   ]
# }