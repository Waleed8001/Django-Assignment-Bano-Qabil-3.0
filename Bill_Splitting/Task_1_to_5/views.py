from django.shortcuts import render
from django.http import JsonResponse
import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt, csrf_protect

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

        # For calculate total amount with tip and tax.
        new_tip = amount * tip / 100
        new_tax = amount * tax / 100
        amount += new_tip + new_tax

        people = []
        count = 0
        split = {}

        # For checking what each person eat and how many price of that item and calculate how many person eat same thing.
        for item in items:
            for persons in person:
                if item['buy'] == persons['item']:
                    total = item['price']
                    count = count + 1
                    people.append(persons)

            # Calculate split for each person including tip and tax according to their item prices.
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

# Expected Output:

# {
#   "Total_amount_after_adding_tip_and_tax_and_prices_of_all_items": 3750.0,
#   "split": {
#     "saad": 216.66666666666669,
#     "hammad": -433.3333333333333,
#     "ghafoor": 316.6666666666667,
#     "umar": -150.0,
#     "Ahmed": 150.0
#   }
# }