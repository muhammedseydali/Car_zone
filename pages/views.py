from django.shortcuts import render
from .models import Team
from cars.models import Cars
# Create your views here.
def home(request):
    team = Team.objects.all()
    featured_cars = Cars.objects.order_by('-created_date').filter(is_featured=True)
    all_cars = Cars.objects.order_by('-created_date')
    # search_field = Cars.objects.values('model', 'city','year','body_style')
    city_search = Cars.objects.values_list('city', flat=True).distinct()
    model_search = Cars.objects.values_list('model', flat=True).distinct()
    year_search = Cars.objects.values_list('year', flat=True).distinct()
    body_style_search = Cars.objects.values_list('body_style', flat=True).distinct()
    data = {
        'teams':team,
        'featured_cars':featured_cars,
        'all_cars':all_cars,
        # 'search_field':search_field,
        'city_search':city_search,
        'model_search':model_search,
        'year_search':year_search,
        'body_style_search':body_style_search,
    }

    return render(request, 'pages/home.html',data)

# def cars(request):
#     return render(request, 'pages/cars.html')

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
