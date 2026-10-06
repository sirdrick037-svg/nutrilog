from django.shortcuts import render,redirect
from .forms import MealEntryForm

# Create your views here.
def home(request):
    if request.method == 'POST':
        form = MealEntryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = MealEntryForm()

    return render(request, 'meal_log/home.html', {'form': form})