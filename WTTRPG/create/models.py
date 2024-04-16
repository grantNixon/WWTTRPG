from django.db import models
from .create_settings import *


def get_races():
    return {i: i for i in Races.races}

def get_backgrounds():
    return {i: i for i in Backgrounds.backgrounds}

def get_pointbuys():
    return {i: i for i in PointBuy.pointbuys}

def get_skills():
    return {i: i for i in Skills.skillz}

# Create your models here.
class Character(models.Model):
    name = models.CharField(max_length = 30)
    race = models.CharField(max_length = 30, choices = get_races)
    background = models.CharField(max_length = 30, choices = get_backgrounds)
    majorskill1 = models.CharField(max_length = 30, choices = get_skills)
    majorskill2 = models.CharField(max_length = 30, choices = get_skills)
    majorskill3 = models.CharField(max_length = 30, choices = get_skills)
    minorskill1 = models.CharField(max_length = 30, choices = get_skills)
    minorskill2 = models.CharField(max_length = 30, choices = get_skills)
    minorskill3 = models.CharField(max_length = 30, choices = get_skills)
    minorskill4 = models.CharField(max_length = 30, choices = get_skills)
    minorskill5 = models.CharField(max_length = 30, choices = get_skills)
    strength = models.IntegerField(choices = get_pointbuys)
    agility = models.IntegerField(choices = get_pointbuys)
    intelligence = models.IntegerField(choices = get_pointbuys)
    gumption = models.IntegerField(choices = get_pointbuys)
    mysticism = models.IntegerField(choices = get_pointbuys)
    personality = models.IntegerField(choices = get_pointbuys)
    
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

class Skill(models.Model):
    skillName = models.CharField(max_length = 30)
    skillAttribute = models.CharField(max_length = 30)