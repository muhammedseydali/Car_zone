
from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField
from multiselectfield import MultiSelectField

# Create your models here.
class Cars(models.Model):
    
    state_choice = (
        ('kerala','kerala'),
        ('tamilnadu','tamilnadu'),
        ('assam','assam'),
        ('maharashtra','maharashtra'),
        ('goa','goa'),
        ('karnataka','karnataka'),
        ('gujarat','gujarat'),
        ('madhyapradesh','madhyapradesh'),
        ('jharkhand','jharkhand'),
        ('telangana','telangana'),
        ('andhrapradesh','andhrapradesh'),
        ('westbangal','westbangal'),
        ('punjab','punjab'),
    )

    year_choice = []
    for r in range(2000,(datetime.now().year+1)):
        year_choice.append((r,r))


    feature_choices = (
        ('cruise control','cruise control'),
        ('Audio Interface', 'Audio Interface'),
        ('Airbags','Airbags'),
        ('Air conditioning','Air conditioning'),
        ('seat heating','seat heating'),
        ('Alarm system','Alarm system',),
        ('Park assistant','Park assistant'),
        ('Power steering','Power steering'),
        ('Reverse camera','Reverse camera'),
        ('Direct fuel injection','Direct fuel injection'),
        ('Auto start/stop','Auto start/stop'),
        ('wind deflector','wind deflector'),
        ('Bluetooth Handset','Bluetooth Handset'),
    )

    door_choice = (
        ('2','2'),
        ('4','4'),
        ('6','6'),
    )


    car_title = models.CharField(max_length=100)
    state = models.CharField(choices=state_choice, max_length=100)
    city = models.CharField(max_length=100)
    colour = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField(('year'),choices=year_choice)
    condition = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    description = RichTextField(max_length=2000)
    car_photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    car_photo1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    car_photo2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    car_photo3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    car_photo4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    features = MultiSelectField(choices=feature_choices)
    body_style = models.CharField(max_length=100)
    engine = models.CharField(max_length=100)
    transmission = models.CharField(max_length=100)
    interior = models.CharField(max_length=100)
    miles = models.IntegerField()
    doors = models.CharField(choices=door_choice, max_length=10)
    passengers = models.IntegerField()
    vin_no = models.CharField(max_length=100)
    milege = models.IntegerField()
    fuel_type = models.CharField(max_length=50)
    no_of_owners = models.CharField(max_length=100)
    is_featured = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.car_title