# Generated by Django 4.0.4 on 2022-11-02 09:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0005_cars_car_title_cars_state_alter_cars_description'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cars',
            options={'verbose_name': 'cars', 'verbose_name_plural': 'cars'},
        ),
    ]