# Generated by Django 4.0.4 on 2022-05-13 10:45

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0004_alter_cars_description_alter_cars_features'),
    ]

    operations = [
        migrations.AddField(
            model_name='cars',
            name='car_title',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cars',
            name='state',
            field=models.CharField(choices=[('kerala', 'kerala'), ('tamilnadu', 'tamilnadu'), ('assam', 'assam'), ('maharashtra', 'maharashtra'), ('goa', 'goa'), ('karnataka', 'karnataka'), ('gujarat', 'gujarat'), ('madhyapradesh', 'madhyapradesh'), ('jharkhand', 'jharkhand'), ('telangana', 'telangana'), ('andhrapradesh', 'andhrapradesh'), ('westbangal', 'westbangal'), ('punjab', 'punjab')], default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cars',
            name='description',
            field=ckeditor.fields.RichTextField(max_length=2000),
        ),
    ]
