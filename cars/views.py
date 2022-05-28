from django.shortcuts import render,get_object_or_404
from .models import Cars
# Create your views here.
def cars(request):
    return render(request,'cars/cars.html')


def car_detail(request,id):
    single_car = get_object_or_404(Cars, pk=id)
    data = {
        'single_car':single_car,
    }

    return render(request, 'cars/car-details.html',data)    