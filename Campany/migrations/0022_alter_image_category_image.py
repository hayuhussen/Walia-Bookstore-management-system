# Generated by Django 4.2.1 on 2023-07-14 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Campany', '0021_image_category_event_news_event_detail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image_category',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
