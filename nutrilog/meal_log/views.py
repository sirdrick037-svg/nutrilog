from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'meal_log/home.html')