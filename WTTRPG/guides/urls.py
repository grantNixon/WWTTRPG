from django.urls import path
from . import views
from .views import *

app_name = 'guides'

urlpatterns = [
    path('', views.guide_view),
    path('mg_purchase/', views.mg_purchase_view),
    path('av1_purchase/',views.av1_purchase_view),
    path('comp_Clothing-Armor',CompClothingArmor.as_view(),name='comp_clothingarmor'),
    path('comp_backgrounds',CompBackgrounds.as_view(),name='comp_backgrounds'),
    path('comp_MysItems-Weapons',CompMysItemsWeapons.as_view(),name='comp_mysitemsweapons'),
    path('comp_races',CompRaces.as_view(),name='comp_races'),
    path('comp_spells',CompSpells.as_view(),name='comp_spells'),
    path('comp_tonics',CompTonics.as_view(),name='comp_tonics'),
    path('comp_utilities',CompUtilities.as_view(),name='comp_utilities'),
    path('comp_weapons',CompWeapons.as_view(),name='comp_weapons'),
]
