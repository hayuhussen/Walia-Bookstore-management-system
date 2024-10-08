# Generated by Django 4.2.1 on 2023-07-15 13:43

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('Campany', '0025_fact'),
    ]

    operations = [
        migrations.CreateModel(
            name='slides',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('titles1', models.CharField(max_length=200)),
                ('descriptions1', tinymce.models.HTMLField()),
                ('paragraphs1', tinymce.models.HTMLField()),
            ],
        ),
    ]
