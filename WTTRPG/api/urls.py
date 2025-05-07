from django.urls import path
from . import views
from .views import *

app_name = 'api'

urlpatterns = [
    path('character/weapons', views.fetchWeapons, name='fetchWeapons'),
    path('character/levelUp', views.levelUp, name='levelup'),
    path('fetchAllWeapons', views.fetchAllWeapons, name='fetchAllWeapons'),
    path('addWeapon', views.addWeapon, name="addWeapon")

]
