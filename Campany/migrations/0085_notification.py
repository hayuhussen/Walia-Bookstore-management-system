# Generated by Django 4.2.1 on 2024-07-30 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Campany', '0084_remove_customer_information_book'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('message', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
