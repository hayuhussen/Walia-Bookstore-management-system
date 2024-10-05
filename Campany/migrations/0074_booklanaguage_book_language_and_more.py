# Generated by Django 4.2.1 on 2024-07-13 05:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Campany', '0073_remove_book_language_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookLanaguage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='language',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Campany.booklanaguage'),
        ),
        migrations.AddField(
            model_name='consignmentagreement',
            name='language',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Campany.booklanaguage'),
        ),
        migrations.AddField(
            model_name='walia_published_book',
            name='language',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Campany.booklanaguage'),
        ),
    ]
