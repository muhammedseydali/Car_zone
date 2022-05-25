# Generated by Django 4.0.4 on 2022-05-13 10:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cars',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=100)),
                ('colour', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
                ('year', models.IntegerField(choices=[(2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019), (2020, 2020), (2021, 2021), (2022, 2022)], verbose_name='year')),
                ('condition', models.CharField(max_length=100)),
                ('price', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('car_photo', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('car_photo1', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('car_photo2', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('car_photo3', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('car_photo4', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('features', models.CharField(choices=[('cruise control', 'cruise control'), ('Audio Interface', 'Audio Interface'), ('Airbags', 'Airbags'), ('Air conditioning', 'Air conditioning'), ('seat heating', 'seat heating'), ('Alarm system', 'Alarm system'), ('Park assistant', 'Park assistant'), ('Power steering', 'Power steering'), ('Reverse camera', 'Reverse camera'), ('Direct fuel injection', 'Direct fuel injection'), ('Auto start/stop', 'Auto start/stop'), ('wind deflector', 'wind deflector'), ('Bluetooth Handset', 'Bluetooth Handset')], max_length=100)),
                ('body_style', models.CharField(max_length=100)),
                ('engine', models.CharField(max_length=100)),
                ('transmission', models.CharField(max_length=100)),
                ('interior', models.CharField(max_length=100)),
                ('miles', models.IntegerField(max_length=100)),
                ('doors', models.CharField(choices=[('2', '2'), ('4', '4'), ('6', '6')], max_length=10)),
                ('passengers', models.IntegerField(max_length=100)),
                ('vin_no', models.CharField(max_length=100)),
                ('milege', models.IntegerField(max_length=100)),
                ('fuel_type', models.CharField(max_length=100)),
                ('no_of_owners', models.CharField(max_length=100)),
                ('is_featured', models.BooleanField(max_length=100)),
                ('created_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]
