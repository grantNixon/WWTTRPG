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
       jsonInv = json.dumps(obj.inventory.weapons)
       return JsonResponse(jsonInv, safe=False)
    else:
        return JsonResponse({'status':'error'})
    
@csrf_exempt    
def fetchAllWeapons(request):
    if request.method == 'POST':
        obj = list(Weapon.objects.values_list('WeaponName', flat=True))
        jsonObj = json.dumps({'name':obj})
        return JsonResponse(jsonObj, safe=False)
    else:
        return JsonResponse({'status':'error'})
@csrf_exempt
def addWeapon(request):
    if request.method == 'POST':
       data = json.loads(request.body)
       weaponToAdd = data.get('weapon_id')
       print(data)
       primary_key = data.get('char_id')
       obj = Character.objects.get(id=primary_key)
       obj.inventory.weapons.append({'name':weaponToAdd})
       obj.inventory.save()
       obj.save()
       return JsonResponse({'status': 'success'})
    
@csrf_exempt
def removeWeapon(request):
    if request.method == 'POST':
       data = json.loads(request.body)
       weaponToRemove = data.get('weapon_id')
       print(data)
       primary_key = data.get('char_id')
       obj = Character.objects.get(id=primary_key)
       obj.inventory.weapons.remove({'name':weaponToRemove})
       obj.inventory.save()
       obj.save()
       return JsonResponse({'status': 'success'})

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

@csrf_exempt
def fetchAllTonics(request):
    if request.method == 'POST':
        obj = list(Tonic.objects.values_list('TonicName', flat=True))
        jsonObj = json.dumps({'name':obj})
        return JsonResponse(jsonObj, safe=False)
    else:
        return JsonResponse({'status':'error'})
    
@csrf_exempt
def fetchTonics(request):
    #return all weapons in current characters inventory
    if request.method == 'POST':
       data = json.loads(request.body)
       primary_key = data.get('id')
       obj = Character.objects.get(id=primary_key)
       jsonInv = json.dumps(obj.inventory.tonics)
       return JsonResponse(jsonInv, safe=False)
    else:
        return JsonResponse({'status':'error'})
    
@csrf_exempt
def addTonic(request):
    if request.method == 'POST':
       data = json.loads(request.body)
       tonicToAdd = data.get('tonic_id')
       print(data)
       primary_key = data.get('char_id')
       obj = Character.objects.get(id=primary_key)
       obj.inventory.tonics.append({'name':tonicToAdd})
       obj.inventory.save()
       obj.save()
       return JsonResponse({'status': 'success'})
    
@csrf_exempt
def removeTonic(request):
    if request.method == 'POST':
       data = json.loads(request.body)
       tonicToRemove = data.get('tonic_id')
       print(data)
       primary_key = data.get('char_id')
       obj = Character.objects.get(id=primary_key)
       obj.inventory.tonics.remove({'name':tonicToRemove})
       obj.inventory.save()
       obj.save()
       return JsonResponse({'status': 'success'})


