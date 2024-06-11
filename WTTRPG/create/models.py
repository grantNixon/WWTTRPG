from django.db import models
from .create_settings import *
from django.conf import *


def get_races():
    return {i: i for i in Races.races}

def get_backgrounds():
    return {i: i for i in Backgrounds.backgrounds}

def get_pointbuys():
    return {i: i for i in PointBuy.pointbuys}

def get_skills():
    return {i: i for i in Skills.skillz}

def get_weaponprofs():
    return {i: i for i in WeaponProfs.weaponprof}

# Create your models here.

class Language(models.Model):
    languageName = models.CharField(max_length = 30)
    languageDescription = models.CharField(max_length = 300)
    def __str__(self):
        return self.languageName
    class Meta:
        ordering = ["-languageName"] 

class Morals(models.Model):
    moralsName = models.CharField(max_length = 30)
    moralsDescription = models.CharField(max_length = 300)
    def __str__(self):
        return self.moralsName
    class Meta:
        ordering = ["-moralsName"] 


class Character(models.Model):
    name = models.CharField(max_length = 30)
    species = models.CharField(max_length = 30, choices = get_races)
    background = models.CharField(max_length = 30, choices = get_backgrounds)
    major_skill_1 = models.CharField(max_length = 30, choices = get_skills)
    major_skill_2 = models.CharField(max_length = 30, choices = get_skills)
    major_skill_3 = models.CharField(max_length = 30, choices = get_skills)
    minor_skill_1 = models.CharField(max_length = 30, choices = get_skills)
    minor_skill_2 = models.CharField(max_length = 30, choices = get_skills)
    minor_skill_3 = models.CharField(max_length = 30, choices = get_skills)
    minor_skill_4 = models.CharField(max_length = 30, choices = get_skills)
    minor_skill_5 = models.CharField(max_length = 30, choices = get_skills)
    strength = models.IntegerField(choices = get_pointbuys)
    agility = models.IntegerField(choices = get_pointbuys)
    intelligence = models.IntegerField(choices = get_pointbuys)
    gumption = models.IntegerField(choices = get_pointbuys)
    mysticism = models.IntegerField(choices = get_pointbuys)
    personality = models.IntegerField(choices = get_pointbuys)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    morals = models.ForeignKey(Morals, on_delete=models.CASCADE)
    weapon_proficiency = models.CharField(max_length=30, choices= get_weaponprofs)
    class_name = models.CharField(max_length=30)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    
class Species(models.Model):
    SpeciesName = models.CharField(max_length = 30)
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





