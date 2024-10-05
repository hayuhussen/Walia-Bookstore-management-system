# Generated by Django 4.2.1 on 2024-07-09 16:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Campany', '0065_consignmentagreement'),
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
            model_name='book',
            name='language',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Campany.booklanguage'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='consignmentagreement',
            name='language',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Campany.booklanguage'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='walia_published_book',
            name='language',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='Campany.booklanguage'),
            preserve_default=False,
        ),
    ]
