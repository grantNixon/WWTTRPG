from django.db import models
from .create_settings import *

def get_races():
    return {i: i for i in Races.races}

# Create your models here.
class Character(models.Model):
    name = models.CharField(max_length = 30)
    race = models.CharField(max_length = 30, choices = get_races)
    