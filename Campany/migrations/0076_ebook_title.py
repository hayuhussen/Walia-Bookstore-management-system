# Generated by Django 4.2.1 on 2024-07-13 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Campany', '0075_audiobook_title_audiobooks_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='ebook',
            name='title',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
