# Generated by Django 4.2.1 on 2023-07-18 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Campany', '0037_eventpost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventpost',
            name='image',
            field=models.ImageField(upload_to='eventpost/'),
        ),
    ]
