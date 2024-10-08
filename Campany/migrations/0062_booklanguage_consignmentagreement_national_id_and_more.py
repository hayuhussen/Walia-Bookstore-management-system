# Generated by Django 4.2.1 on 2024-07-09 06:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Campany', '0061_remove_consignmentagreement_national_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookLanguage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='consignmentagreement',
            name='national_id',
            field=models.ImageField(blank=True, null=True, upload_to='national_id/'),
        ),
        migrations.AddField(
            model_name='book',
            name='language',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='Campany.booklanguage'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='consignmentagreement',
            name='language',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='Campany.booklanguage'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='walia_published_book',
            name='language',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Campany.booklanguage'),
            preserve_default=False,
        ),
    ]
