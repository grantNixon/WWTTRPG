from django.contrib import admin
from .models import *

# Register your models here

class CharacterAdmin(admin.ModelAdmin):
    filter_horizontal = ('perks',)  # Makes perks selection more user-friendly

admin.site.register(Character, CharacterAdmin)
admin.site.register(Morals)
admin.site.register(Language)
admin.site.register(Weapon)
admin.site.register(StartingEquipment)
admin.site.register(Spell)
admin.site.register(Utilities)
admin.site.register(Armor)
admin.site.register(Tonic)
admin.site.register(TestPacketFile)
admin.site.register(OneShotFile)
admin.site.register(Background)
admin.site.register(Inventory)
admin.site.register(Perk)