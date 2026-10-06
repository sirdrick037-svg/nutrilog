from django import forms
from .models import MealEntry
from django.utils import timezone

class MealEntryForm(forms.ModelForm):
    class Meta:
        model = MealEntry
        fields = ['name', 'calories', 'date']
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Enter food name',
                'class': 'w-full border border-gray-300 rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-green-500',
            }),
            'calories': forms.NumberInput(attrs={
                'placeholder': 'Enter calories',
                'min': '0',
                'class': 'w-full border border-gray-300 rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-green-500',
            }),
            'date': forms.DateInput(attrs={
                'type': 'date',
                'class': 'w-full border border-gray-300 rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-green-500',
            }),
        }

def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)

    if not self.instance.pk:
        self.fields['date'].initial = timezone.localdate()        