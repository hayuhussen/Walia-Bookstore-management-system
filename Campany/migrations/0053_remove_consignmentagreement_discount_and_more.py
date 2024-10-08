# Generated by Django 4.2.1 on 2024-06-30 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Campany', '0052_consignmentagreement_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='consignmentagreement',
            name='discount',
        ),
        migrations.AddField(
            model_name='consignmentagreement',
            name='discount_percent',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
        migrations.AddField(
            model_name='consignmentagreement',
            name='total_price',
            field=models.DecimalField(decimal_places=2, default=2, max_digits=10),
            preserve_default=False,
        ),
    ]
