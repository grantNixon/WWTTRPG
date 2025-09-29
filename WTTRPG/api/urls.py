from django.urls import path
from . import views
from .views import *

app_name = 'api'

urlpatterns = [
    path('character/weapons', views.fetchWeapons, name='fetchWeapons'),
    path('character/tonics', views.fetchTonics, name='fetchTonics'),
    path('character/clothing', views.fetchClothing, name='fetchClothing'),
    path('character/utilities', views.fetchUtility, name='fetchUtility'),
    path('character/mysticalWeapons', views.fetchMysticalWeapons, name='fetchMysticalWeapons'),
    path('character/levelUp', views.levelUp, name='levelup'),
    path('fetchAllWeapons', views.fetchAllWeapons, name='fetchAllWeapons'),
    path('addWeapon', views.addWeapon, name="addWeapon"),
    path('removeWeapon', views.removeWeapon, name="removeWeapon"),
    path('fetchAllTonics', views.fetchAllTonics, name='fetchAllTonics'),
    path('addTonic', views.addTonic, name="addTonic"),
    path('removeTonic', views.removeTonic, name="removeTonic"),
    path('fetchAllClothing', views.fetchAllClothing, name='fetchAllClothing'),
    path('addClothing', views.addClothing, name="addClothing"),
    path('removeClothing', views.removeClothing, name="removeClothing"),
    path('fetchAllUtility', views.fetchAllUtility, name='fetchAllUtility'),
    path('addUtility', views.addUtility, name="addUtility"),
    path('removeUtility', views.removeUtility, name="removeUtility"),
    path('fetchAllMysticalWeapons', views.fetchAllMysticalWeapons, name='fetchAllMysticalWeapons'),
    path('addMysticalWeapon', views.addMysticalWeapon, name="addMysticalWeapon"),
    path('removeMysticalWeapon', views.removeMysticalWeapon, name="removeMysticalWeapon"),
    path('showSpellSelection', views.showSpellSelection, name="showSpellSelection"),

]
