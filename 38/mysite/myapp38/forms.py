from django import forms
from .models import Animal


class AddAnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = ('name', 'gender', 'type', 'age')
