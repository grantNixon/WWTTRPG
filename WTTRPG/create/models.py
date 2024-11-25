from django.db import models
from create.create_settings import *
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

class Weapon(models.Model):
    WeaponName = models.CharField(max_length = 100)
    DamageType = models.CharField(max_length = 100)
    ActionCost = models.FloatField()
    Range = models.CharField(max_length=30)
    Damage = models.CharField(max_length = 100)

    def __str__(self):
        return self.WeaponName    

class StartingEquipment(models.Model):
    name = models.CharField(max_length=30)
    itemList = models.CharField(max_length=1000)


    def __str__(self):
        return self.name

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
    starting_weapon = models.ForeignKey(Weapon, on_delete=models.CASCADE)
    starting_equipment = models.ForeignKey(StartingEquipment, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    level = models.IntegerField()
    hp = models.IntegerField()
    mb = models.IntegerField()
    ec = models.IntegerField()
    ap = models.IntegerField()
    initiative = models.IntegerField(default=2)
    sk_crushing = models.IntegerField(default = 5)
    sk_shotguns = models.IntegerField(default = 5)
    sk_hand = models.IntegerField(default = 5)
    sk_athletics = models.IntegerField(default = 5)
    sk_crafting = models.IntegerField(default = 5)
    sk_slashingmelee= models.IntegerField(default = 5)
    sk_pistols = models.IntegerField(default = 5)
    sk_archery = models.IntegerField(default = 5)
    sk_ropework = models.IntegerField(default = 5)
    sk_acrobatics = models.IntegerField(default = 5)
    sk_sneak = models.IntegerField(default = 5)
    sk_thievery = models.IntegerField(default = 5)
    sk_intimidation = models.IntegerField(default = 5)
    sk_hunting = models.IntegerField(default = 5)
    sk_cooking = models.IntegerField(default = 5)
    sk_foraging = models.IntegerField(default = 5)
    sk_animalhandling = models.IntegerField(default = 5)
    sk_rifles = models.IntegerField(default = 5)
    sk_intuition = models.IntegerField(default = 5)
    sk_investigation = models.IntegerField(default = 5)
    sk_gambit = models.IntegerField(default = 5)
    sk_brewing = models.IntegerField(default = 5)
    sk_galvanismmagic = models.IntegerField(default = 5)
    sk_religion = models.IntegerField(default = 5)
    sk_medicine = models.IntegerField(default = 5)
    sk_history = models.IntegerField(default = 5)
    sk_healingmagic = models.IntegerField(default = 5)
    sk_utilitymagic = models.IntegerField(default = 5)
    sk_absolutionmagic = models.IntegerField(default = 5)
    sk_foolery = models.IntegerField(default = 5)
    sk_persuasion = models.IntegerField(default = 5)
    sk_barter = models.IntegerField(default = 5)
    sk_deceptionmagic = models.IntegerField(default = 5)
    sk_ritualmagic = models.IntegerField(default = 5)
    sk_destructionmagic = models.IntegerField(default = 5)
    sk_performance = models.IntegerField(default = 5)
    
    
    
class Species(models.Model):
    SpeciesName = models.CharField(max_length = 30)
    description = models.TextField()

class Background(models.Model):
    BackgroundName = models.CharField(max_length = 30)
    StartingWeaponChoice = models.CharField(max_length = 100)
    StartingSupplies = models.CharField(max_length = 100)
    StartingBuff = models.CharField(max_length = 100)
    StartingDebuff = models.CharField(max_length = 100)

class Spell(models.Model):
    MagicSchool = models.CharField(max_length = 100)
    SpellDescription = models.TextField()
    SpellName = models.CharField(max_length = 100)
    ActionCost = models.CharField(max_length=100)
    Range = models.CharField(max_length=100)
    SpellEffect =models.CharField(max_length=100)

    def __str__(self):
        return self.SpellName  

class Armor(models.Model):
    ArmorName = models.CharField(max_length = 100)
    ArmorDescription = models.TextField()
    ArmorStats = models.TextField()

    def __str__(self):
        return self.ArmorName

class Tonic(models.Model):
    TonicName = models.CharField(max_length = 100)
    TonicSize = models.CharField(max_length = 100)
    TonicDescription = models.TextField()
    ActionCost = models.TextField()

    def __str__(self):
        return self.TonicName


class Utilities(models.Model):
    UtilityName = models.CharField(max_length = 100)
    UtilityType = models.CharField(max_length = 100)
    ActionCost = models.FloatField()
    Range = models.CharField(max_length = 100)
    Effect = models.TextField()

    def __str__(self):
        return self.UtilityName

class Skill(models.Model):
    skillName = models.CharField(max_length = 30)
    skillAttribute = models.CharField(max_length = 30)







