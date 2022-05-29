import imp
from django.shortcuts import render,get_object_or_404
from .models import Cars
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
# Create your views here.
def cars(request):
    cars = Cars.objects.order_by('-created_date')
    paginator = Paginator(cars, 4)
    page = request.GET.get('page')
    paged_cars = paginator.get_page(page)
    data = {
        'cars':paged_cars,
    }
    return render(request,'cars/cars.html',data)


def car_detail(request,id):
    single_car = get_object_or_404(Cars, pk=id)
    data = {
        'single_car':single_car,
    }

    return render(request, 'cars/car-details.html',data)    