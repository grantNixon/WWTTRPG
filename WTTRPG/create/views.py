from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import FormView, CreateView, DetailView
from create.models import Character
from .forms import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

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