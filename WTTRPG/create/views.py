from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import FormView,CreateView
from create.models import Character
from .forms import *

# Create your views here.
def create_view(request):
    return(render(request,"create/create_page.html"))

def homebrew_view(request):
    return(render(request,"create/homebrew.html"))

class QSCharCreator(CreateView):
    model = Character
    success_url = '/home_page/'
    form_class = CharacterCreateForm
    
    def form_valid(self, form):
        Character = form.save(commit=False)
        Character.user = self.request.user  # Set the user field
        Character.save()
        return redirect('/home_page')  # Redirect to a success page


