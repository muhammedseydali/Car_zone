from email import message
from sre_parse import SubPattern
from django.shortcuts import redirect, render
from .models import Team
from cars.models import Cars
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth.models import User
# Create your views here.
def home(request):
    team = Team.objects.all()
    featured_cars = Cars.objects.order_by('-created_date').filter(is_featured=True)
    print(featured_cars)
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

    return render(request, 'pages/home1.html',data)

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
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        phone = request.POST['phone']
        message = request.POST['message']

        email_subject = "You have new message from Carzone website regarding " +subject
        message_body = 'name:' +name + 'email : ' + email + 'subject : ' + subject + 'phone : '+ phone + 'message : ' +message 

        admin_info = User.objects.get(is_superuser=True)
        admin_email = admin_info.email 

        send_mail(
        email_subject,
        message_body,
        'seydali.zewia@gmail.com',
        [admin_email],
        fail_silently=False,
)
        messages.success(request,'Thank you for contacting us, we will get back you shortly')
        return redirect('contact')
        
    return render(request, 'pages/contact.html')
