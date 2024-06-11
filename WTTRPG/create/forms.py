from django import forms
from .models import *
from collections import Counter

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
        print (len(list(result.keys())))

    class Meta:
        model = Character
        fields = "__all__"
        exclude = ['user']