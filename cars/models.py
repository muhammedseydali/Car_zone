from django.db import models

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

car_title = models.CharField    