from django.shortcuts import render
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
    


