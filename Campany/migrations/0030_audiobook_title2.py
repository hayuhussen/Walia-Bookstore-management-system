# Generated by Django 4.2.1 on 2023-07-16 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Campany', '0029_books_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='audiobook',
            name='title2',
            field=models.CharField(default='random title', max_length=255),
            preserve_default=False,
        ),
    ]
