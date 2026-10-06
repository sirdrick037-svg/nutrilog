from django.shortcuts import get_object_or_404, render,redirect, get_list_or_404
from django.utils import timezone
from django.views.decoraters.http import require_post

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


def edit_meal(request, meal_id):
    meal = get_object_or_404(MealEntry, id=meal_id)

    if request.method == 'POST':
        form = MealEntryForm(request.POST, instance=meal)

        if form.is_valid():
            form.save()
            return redirect('home')

    else:
        form = MealEntryForm(instance=meal)

    return render(request, 'meal_log/edit_meal.html', {
        'form': form,
        'meal': meal,
    })

@require_POST
def delete_meal(request, meal_id):
    meal = get_object_or_404(MealEntry, id=meal_id)
    meal.delete()
    return redirect('home')