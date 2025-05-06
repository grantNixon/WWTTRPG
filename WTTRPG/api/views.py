from django.shortcuts import render
from create.models import *
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
@csrf_exempt
def fetchWeapons(request):
    #return all weapons in current characters inventory
    if request.method == 'POST':
       data = json.loads(request.body)
       primary_key = data.get('id')
       obj = Character.objects.get(id=primary_key)
       print(obj.inventory.weapons)
       jsonInv = json.dumps(obj.inventory.weapons)
       return JsonResponse(jsonInv, safe=False)
    else:
        return JsonResponse({'status':'error'})

def addWeapon():
    pass

def removeWeapon():
    pass

def levelUp(request):
    if request.method == 'POST':    
        data = json.loads(request.body)
        primary_key = data.get('id')
        majorInc = data.get('major')
        minorInc = data.get('minor')
        obj = Character.objects.get(id=primary_key)

        new_major_value = getattr(obj, majorInc) + 5
        new_minor_value = getattr(obj, minorInc) + 3

        obj.level += 1
        setattr(obj, majorInc, new_major_value)
        setattr(obj, minorInc, new_minor_value)

        obj.save()

        return JsonResponse({'status': 'success'})
    else:
         return JsonResponse({'status': 'error', 'message': 'Failed to update skills'})

    #need logic for major/minor skill increases 

