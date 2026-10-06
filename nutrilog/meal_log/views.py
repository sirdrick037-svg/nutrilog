from django.shortcuts import render,redirect
from django.utils import timezone

from .forms import MealEntryForm
from .models import MealEntry

# Create your views here.
def home(request):
    if request.method == 'POST':
        form = MealEntryForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('home')

    else:
        form = MealEntryForm()

    today = timezone.localdate()

    meals = MealEntry.objects.filter(
        date=today
    ).order_by('-created_at')

    total_calories = sum(
        meal.calories for meal in meals
    )

    return render(request, 'meal_log/home.html', {
        'form': form,
        'meals': meals,
        'total_calories': total_calories,
    })