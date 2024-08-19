# Generated by Django 4.2.14 on 2024-08-19 11:57

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import main.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=50)),
                ('year', models.IntegerField(default=main.models.current_year, validators=[django.core.validators.MinValueValidator(2000), django.core.validators.MaxValueValidator(main.models.current_year)])),
                ('color', models.CharField(max_length=20)),
                ('mileage', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('volume', models.DecimalField(decimal_places=1, default=0, max_digits=3)),
                ('body_type', models.CharField(blank=True, choices=[('sedan', 'Седан'), ('hatchback', 'Хэтчбек'), ('SUV', 'Внедорожник'), ('wagon', 'Универсал'), ('minivan', 'Минивэн'), ('pickup', 'Пикап'), ('coupe', 'Купе'), ('cabrio', 'Кабриолет')])),
                ('drive_unit', models.CharField(blank=True, choices=[('rear', 'Задний'), ('front', 'Передний'), ('full', 'Полный')])),
                ('gearbox', models.CharField(blank=True, choices=[('manual', 'Механика'), ('automatic', 'Автомат'), ('вариатор', 'CVT'), ('robot', 'Робот')])),
                ('fuel_type', models.CharField(blank=True, choices=[('gasoline', 'Бензин'), ('diesel', 'Дизель'), ('hybrid', 'Гибрид'), ('electro', 'Электро')])),
                ('price', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(99999999)])),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('middle_name', models.CharField(max_length=50)),
                ('date_of_birth', models.DateField()),
                ('phone_number', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True, null=True)),
                ('car', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='main.car')),
                ('client', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='main.client')),
            ],
        ),
    ]
