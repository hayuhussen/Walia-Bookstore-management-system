# Generated by Django 4.2.1 on 2023-07-04 07:23

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('Campany', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='slide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('image2', models.ImageField(upload_to='')),
                ('titles1', models.CharField(max_length=200)),
                ('descriptions1', tinymce.models.HTMLField()),
                ('paragraphs1', tinymce.models.HTMLField()),
                ('image3', models.ImageField(upload_to='')),
                ('titles2', models.CharField(max_length=200)),
                ('descriptions2', tinymce.models.HTMLField()),
                ('paragraphs2', tinymce.models.HTMLField()),
            ],
        ),
    ]
