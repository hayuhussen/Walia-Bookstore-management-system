# Generated by Django 4.2.1 on 2023-07-16 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Campany', '0031_address_blog_eventhomeimage_meetstaff_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.AlterField(
            model_name='slide',
            name='image',
            field=models.ImageField(upload_to='slides/'),
        ),
    ]
