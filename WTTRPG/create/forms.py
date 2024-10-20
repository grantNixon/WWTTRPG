from django import forms
from .models import *
from collections import Counter
from django.contrib.auth.models import User

#creating a form class to use in the createview so i can override the clean file method and do custom validation
class CharacterCreateForm(forms.ModelForm):
    def clean(self):
        chosenOptions = self.cleaned_data.items()
        chosenSkills = {}
        for k, v in chosenOptions:
            if k.__contains__("skill"):
                chosenSkills[k] = v
        counts = Counter(chosenSkills.values())
        result = {k: v for k , v in chosenSkills.items() if counts[v] > 1}
        if len(list(result.keys())) > 0:
            raise forms.ValidationError("Please make sure you are selecting a skill only once!")


    class Meta:
        model = Character
        fields = ['name', 'species', 'background', 'major_skill_1','major_skill_2','major_skill_3','minor_skill_1','minor_skill_2','minor_skill_3','minor_skill_4','minor_skill_5','strength','agility','intelligence','gumption','mysticism','personality','language','morals','weapon_proficiency','starting_weapon','starting_equipment','class_name']
        exclude = ['user']

class NewUserForm(forms.ModelForm):
    def clean(self):
        pass1 = self.cleaned_data.get("password")
        pass2 = self.cleaned_data.get("password2")

        if pass1 != pass2:
            raise forms.ValidationError("Passwords do not match")

    class Meta:
        model = User
        fields = "__all__"
        exclude = ['date_joined']