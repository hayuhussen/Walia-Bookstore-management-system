# Generated by Django 4.2.1 on 2023-07-13 16:54

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('Campany', '0018_books'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bookks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('discount_price', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('inventory', models.IntegerField()),
                ('audio_book', models.FileField(blank=True, null=True, upload_to='audio_books')),
                ('descriptions1', tinymce.models.HTMLField()),
                ('publish_date', models.DateField()),
                ('image', models.ImageField(upload_to='')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Campany.author')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Campany.category')),
            ],
        ),
    ]
