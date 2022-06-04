from cgitb import enable
from email import message
import re
from django.shortcuts import render,redirect
from django.contrib import messages
# Create your views here.
from django.shortcuts import render
from .models import Contact
from django.core.mail import send_mail
from django.contrib.auth.models import User
# Create your views here.
def Enquiry(request):
    if request.method == 'POST':
        car_id = request.POST['car_id']
        car_title = request.POST['car_title']
        user_id = request.POST['user_id']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        customer_need = request.POST['customer_need']
        city = request.POST['city']
        state = request.POST['state']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']

        if request.user.is_authenticated:
            user_id = request.user.id

            has_contacted = Contact.objects.all().filter(car_id=car_id,user_id=user_id)
            if has_contacted:
                messages.error(request,'ypu are already enquire about this car')
                return redirect('/cars/'+car_id)

        contact = Contact(car_id=car_id,car_title=car_title,user_id=user_id,first_name=first_name,
        last_name=last_name,customer_need=customer_need,city=city,state=state,email=email,phone=phone,message=message)

        admin_info = User.objects.get(is_superuser=True)
        admin_email = admin_info.email
        send_mail(
                'New car enquiry',
                'You have enquiry for the car ' + car_title + '. please login to your account ',
                'seydali.zewia@gmail.com',
                [admin_email],
                fail_silently=False
        )

        contact.save()
        messages.success(request,'Youre request has been submitted, will get back you shortly')
        return redirect('/cars/'+car_id)