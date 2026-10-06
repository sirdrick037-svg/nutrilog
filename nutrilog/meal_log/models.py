from django.db import models

# Create your models here.
class MealEntry(models.Model):
    name = models.CharField(max_length=200)
    calories = models.PositiveIntegerField()
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name