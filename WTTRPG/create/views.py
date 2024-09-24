from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import FormView, CreateView, DetailView
from create.models import Character
from .forms import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json


# Create your views here.
def create_view(request):
    return(render(request,"create/create_page.html"))

def homebrew_view(request):
    return(render(request,"create/homebrew.html"))

class QSCharCreator(LoginRequiredMixin,CreateView):
    model = Character
    success_url = '/home_page/'
    form_class = CharacterCreateForm

    def leveling_table(self,stat,table):
        i = 0
        keys = list(table.keys())
        while i < len(keys):
            if stat == keys[i]:
                return table.get(keys[i])
            if stat > keys[i]:
                if stat < keys[i + 1]:
                    return table.get(keys[i])
                else:
                    i = i + 1
                


    def compute_stats(self):
        gump_health = {5:15,10:20,20:25,30:35,40:40,50:55,60:65,70:75,80:90,90:115,100:130}
        str_move = {5:15,15:20,30:25,45:30,60:35,75:40,90:45,100:50}
        agi_ec = {5:11,10:12,20:13,30:14,40:15,50:16,60:17,70:18,80:19,90:20,100:23}
        level_ap = {1:4,3:6,8:7,15:8,20:9}
        hp = self.leveling_table(Character.gumption,gump_health)
        mb = self.leveling_table(Character.strength,agi_ec)
        ec = self.leveling_table(Character.agility,agi_ec)
        ap = self.leveling_table(Character.level,level_ap)
        stats = {"hp":hp,"mb":mb,"ec":ec,"ap":ap}
        return stats

    
    def form_valid(self, form):
        Character = form.save(commit=False)
        Character.user = self.request.user  # Set the user field
        Character.level = 1
        stats = self.compute_stats()
        Character.hp = stats.get("hp")
        Character.mb = stats.get("mb")
        Character.ec = stats.get("ec")
        Character.ap = stats.get("ap")
        Character.save()
        return redirect('/create/character_detail/' + str(Character.id))  # Redirect to a success page

def SignUpView(request):
    form = NewUserForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            user = User.objects.create_user(form.cleaned_data['email'], form.cleaned_data['email'], 
                                           form.cleaned_data['password'])
        else:
            errors = form.errors
            for field_name, error_list in errors.items():
                for error in error_list:
                    print(f"Error in field '{field_name}': {error}")
            return render(request,"registration/create_account.html", {'form':form})
    return render(request,"registration/create_account.html", {'form':form})

class CharacterSheet(DetailView):
    model = Character

@csrf_exempt
def update_skills(request):
    #request should contain primary key for character, skill to increment, value to increment
    if request.method == 'POST':
        primary_key = request.POST.get('id')
        skill_to_update = "sk_" + request.POST.get('skill')
        increment = request.POST.get('increment')
        if primary_key and skill_to_update and increment:
            obj = Character.objects.get(id=primary_key)
            current_sk_value = getattr(obj, skill_to_update)
            new_sk_value = current_sk_value + int(increment)
            setattr(obj, skill_to_update, new_sk_value)
            obj.save()
            return JsonResponse({'status': 'success'})
        else:
            return JsonResponse({'status': 'error', 'message': 'Failed to update skills'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'})
    
@csrf_exempt
def retrieve_skills(request):
    if request.method == 'GET':
       primary_key = request.GET.get('id')
       obj = Character.objects.get(id=primary_key)
       response_string = {
           'status':'success',
           'crushing':{'level': obj.sk_crushing, 'xp': 0},
           'shotguns':{'level': obj.sk_shotguns, 'xp': 0},
           'hand':{'level': obj.sk_hand, 'xp': 0},
           'athletics':{'level': obj.sk_athletics, 'xp': 0},
           'crafting':{'level': obj.sk_crafting, 'xp': 0},
           'slashingmelee':{'level': obj.sk_slashingmelee, 'xp': 0},
           'pistols':{'level': obj.sk_pistols, 'xp': 0},
           'archery':{'level': obj.sk_archery,'xp': 0},
           'ropework':{'level': obj.sk_ropework, 'xp': 0},
           'acrobatics':{'level': obj.sk_acrobatics, 'xp': 0},
           'sneak':{'level': obj.sk_sneak, 'xp': 0},
           'thievery':{'level':obj.sk_thievery, 'xp': 0},
           'intimidation':{'level':obj.sk_intimidation, 'xp': 0},
           'hunting':{'level':obj.sk_hunting, 'xp': 0},
           'animal':{'level':obj.sk_animalhandling, 'xp': 0 },
            'rifles': { 'level': obj.sk_rifles, 'xp': 0 },
            'intuition': { 'level': obj.sk_intuition , 'xp': 0 },
            'investigation': { 'level': obj.sk_investigation , 'xp': 0 },
            'gambit': { 'level':obj.sk_gambit, 'xp': 0 },
            'brewing': { 'level': obj.sk_brewing, 'xp': 0 },
            'galvanism': { 'level': obj.sk_galvanismmagic, 'xp': 0 },
            'religion': { 'level': obj.sk_religion, 'xp': 0 },
            'history': { 'level': obj.sk_history, 'xp': 0 },
            'medicine': { 'level': obj.sk_medicine, 'xp': 0 },
           'healing': { 'level': obj.sk_healingmagic, 'xp': 0 },
            'utility': { 'level': obj.sk_utilitymagic, 'xp': 0 },
            'absolution': { 'level': obj.sk_absolutionmagic, 'xp': 0 },
            'foolery': { 'level': obj.sk_foolery, 'xp': 0 },
            'persuasion': { 'level': obj.sk_persuasion, 'xp': 0 },
            'barter': { 'level': obj.sk_barter, 'xp': 0 },
            'performance': { 'level': obj.sk_performance, 'xp': 0 },
            'deception': { 'level': obj.sk_deceptionmagic, 'xp': 0 },
            'ritual': { 'level': obj.sk_ritualmagic, 'xp': 0 },
            'destruction': { 'level': obj.sk_destructionmagic, 'xp': 0 },
           
           }
       return JsonResponse(response_string)
    else:
        return JsonResponse({'status':'error'})
    