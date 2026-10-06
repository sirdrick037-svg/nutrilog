from django.contrib import admin
from .models import MealEntry

# Register your models here.
@admin.register(MealEntry)
class MealEntryAdmin(admin.ModelAdmin):
    list_display = ('name', 'calories', 'date', 'created_at')
    list_filter = ('date',)
    search_fields = ('name',)