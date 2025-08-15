from django.urls import path
from . import views
from .views import *

app_name = 'api'

urlpatterns = [
    path('character/weapons', views.fetchWeapons, name='fetchWeapons'),
    path('character/tonics', views.fetchTonics, name='fetchTonics'),
    path('character/levelUp', views.levelUp, name='levelup'),
    path('fetchAllWeapons', views.fetchAllWeapons, name='fetchAllWeapons'),
    path('addWeapon', views.addWeapon, name="addWeapon"),
    path('removeWeapon', views.removeWeapon, name="removeWeapon"),
    path('fetchAllTonics', views.fetchAllTonics, name='fetchAllTonics'),
    path('addTonic', views.addTonic, name="addTonic"),
    path('removeTonic', views.removeTonic, name="removeTonic"),

]
