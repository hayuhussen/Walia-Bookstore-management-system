# Generated by Django 4.2.1 on 2024-07-09 06:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Campany', '0059_remove_book_language_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consignmentagreement',
            name='national_id',
            field=models.ImageField(blank=True, null=True, upload_to='national_id/'),
        ),
        migrations.CreateModel(
            name='EBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='Audio/')),
                ('file', models.FileField(upload_to='ebooks/')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Campany.book')),
            ],
        ),
    ]
