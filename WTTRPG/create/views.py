from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import FormView,CreateView
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
    
    def form_valid(self, form):
        Character = form.save(commit=False)
        Character.user = self.request.user  # Set the user field
        Character.save()
        return redirect('/home_page')  # Redirect to a success page

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
