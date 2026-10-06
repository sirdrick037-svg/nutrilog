from django import forms
from .models import MealEntry


class MealEntryForm(forms.ModelForm):
    class Meta:
        model = MealEntry
        fields = ['name', 'calories', 'date']

        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Enter food name'
            }),
            'calories': forms.NumberInput(attrs={
                'placeholder': 'Enter calories',
                'min': '0'
            }),
            'date': forms.DateInput(attrs={
                'type': 'date'
            }),
        }