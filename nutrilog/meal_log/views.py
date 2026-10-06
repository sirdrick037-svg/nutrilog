from django.shortcuts import render,redirect
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

    meals = MealEntry.objects.all().order_by('-date', '-created_at')

    return render(request, 'meal_log/home.html', {
        'form': form,
        'meals': meals,
    })