# Generated by Django 4.2.1 on 2023-07-18 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Campany', '0042_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='fact',
            name='image',
            field=models.ImageField(default='random', upload_to='fact/'),
            preserve_default=False,
        ),
    ]
