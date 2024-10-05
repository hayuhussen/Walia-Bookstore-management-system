# Generated by Django 4.2.1 on 2023-07-15 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Campany', '0024_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.CharField(choices=[('ebook', 'Ebook'), ('eaudio', 'Eaudio'), ('magazine', 'Magazine'), ('video', 'Video')], max_length=20)),
                ('name', models.CharField(max_length=50)),
                ('counter', models.PositiveIntegerField()),
            ],
            options={
                'verbose_name_plural': 'Facts',
            },
        ),
    ]
