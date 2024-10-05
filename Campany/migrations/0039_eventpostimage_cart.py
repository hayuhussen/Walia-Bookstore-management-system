# Generated by Django 4.2.1 on 2023-07-18 08:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Campany', '0038_alter_eventpost_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventPostImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='post/')),
                ('title', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_edit_hold', models.BooleanField(default=False)),
                ('is_cancel_hold', models.BooleanField(default=False)),
                ('is_add_hold', models.BooleanField(default=False)),
                ('is_remove', models.BooleanField(default=False)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Campany.book')),
            ],
        ),
    ]
