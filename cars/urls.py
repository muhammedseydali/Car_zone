
from . import views
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
   path('newcars/',views.cars, name='cars'),
   path('cars/<int:id>', views.car_detail, name='car_detail')

]