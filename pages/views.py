from django.shortcuts import render
from .models import Team
from cars.models import Cars
# Create your views here.
def home(request):
    team = Team.objects.all()
    featured_cars = Cars.objects.order_by('-created_date').filter(is_featured=True)
    all_cars = Cars.objects.order_by('-created_date')
    search_field = Cars.objects.values('model', 'city','year','body_style')
    data = {
        'teams':team,
        'featured_cars':featured_cars,
        'all_cars':all_cars,
        'search_field':search_field,
    }

    return render(request, 'pages/home.html',data)

def cars(request):
    return render(request, 'pages/cars.html')

def about(request):
     team = Team.objects.all()
     data = {
        'teams':team,
    }
     return render(request, 'pages/about.html',data)

def services(request):
    return render(request, 'pages/services.html')

def contact(request):
    return render(request, 'pages/contact.html')
