# Generated by Django 4.2.1 on 2024-07-25 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Campany', '0081_customer_information'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer_information',
            name='phone_Number',
            field=models.CharField(max_length=15),
        ),
    ]
