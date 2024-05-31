from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
def guide_view(request):
    return(render(request,"guides/guides.html"))

def mg_purchase_view(request):
    return(render(request,"guides/main_guide_purchase.html"))

def av1_purchase_view(request):
    return(render(request,"guides/av1_purchase.html"))

class CompBackgrounds(TemplateView):
    template_name = 'guides/Compendium_Backgrounds.html'

class CompMysItemsWeapons(TemplateView):
    template_name = 'guides/Compendium_MysItems-Weapons.html'

class CompRaces(TemplateView):
    template_name = 'guides/Compendium_Species.html'

class CompSpells(TemplateView):
    template_name = 'guides/Compendium_Spells.html'

class CompTonics(TemplateView):
    template_name = 'guides/Compendium_Tonics.html'

class CompUtilities(TemplateView):
    template_name = 'guides/Compendium_Utilities.html'

class CompWeapons(TemplateView):
    template_name = 'guides/Compendium_Weapons.html'

class CompClothingArmor(TemplateView):
    template_name = 'guides/Compendium_Clothing-Armor.html'