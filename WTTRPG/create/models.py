from django.db import models
from .create_settings import *

def get_races():
    return {i: i for i in Races.races}

def get_backgrounds():
    return {i: i for i in Backgrounds.backgrounds}

def get_pointbuys():
    return {i: i for i in PointBuy.pointbuys}

# Create your models here.
class Character(models.Model):
    name = models.CharField(max_length = 30)
    race = models.CharField(max_length = 30, choices = get_races)
    background = models.CharField(max_length = 30, choices = get_backgrounds)
    strength = models.IntegerField(choices = "")
    agility = models.IntegerField(choices = "")
    intelligence = models.IntegerField(choices = "")
    gumption = models.IntegerField(choices = "")
    mysticism = models.IntegerField(choices = "")
    personality = models.IntegerField(choices = "")
    
class Race(models.Model):
    RaceName = models.CharField(max_length = 30)
    description = models.TextField()

class Background(models.Model):
    BackgroundName = models.CharField(max_length = 30)
    StartingWeaponChoice = models.CharField(max_length = 100)
    StartingSupplies = models.CharField(max_length = 100)
    StartingBuff = models.CharField(max_length = 100)
    StartingDebuff = models.CharField(max_length = 100)

class Weapon(models.Model):
    WeaponName = models.CharField(max_length = 100)
    DamageType = models.CharField(max_length = 100)
    ActionCost = models.FloatField()
    Range = models.IntegerField()
    Damage = models.CharField(max_length = 100)

class Spell(models.Model):
    MagicSchool = models.CharField(max_length = 100)
    SpellType = models.CharField(max_length = 100)
    SpellDescription = models.TextField()

class Armor(models.Model):
    ArmorName = models.CharField(max_length = 100)
    ArmorDescription = models.TextField()

class Tonics(models.Model):
    TonicName = models.CharField(max_length = 100)
    TonicSize = models.CharField(max_length = 100)
    TonicDescription = models.TextField()

class Utilities(models.Model):
    UtilityName = models.CharField(max_length = 100)
    UtilityType = models.CharField(max_length = 100)
    ActionCost = models.FloatField()
    Range = models.IntegerField()
    Effect = models.TextField()