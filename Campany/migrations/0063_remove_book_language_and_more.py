# Generated by Django 4.2.1 on 2024-07-09 06:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Campany', '0062_booklanguage_consignmentagreement_national_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='language',
        ),
        migrations.RemoveField(
            model_name='consignmentagreement',
            name='language',
        ),
        migrations.RemoveField(
            model_name='walia_published_book',
            name='language',
        ),
        migrations.DeleteModel(
            name='BookLanguage',
        ),
    ]
