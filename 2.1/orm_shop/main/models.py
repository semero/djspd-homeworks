from django.db import models

from django.core.validators import MinValueValidator, MaxValueValidator
import datetime


class Client(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.name} {self.middle_name} {self.last_name}'


GEARBOX_CHOICES = (
    ('manual', 'Механика'),
    ('automatic', 'Автомат'),
    ('вариатор', 'CVT'),
    ('robot', 'Робот')
)

FUEL_TYPE_CHOICES = (
    ('gasoline', 'Бензин'),
    ('diesel', 'Дизель'),
    ('hybrid', 'Гибрид'),
    ('electro', 'Электро')
)

BODY_TYPE_CHOICES = (
    ('sedan', 'Седан'),
    ('hatchback', 'Хэтчбек'),
    ('SUV', 'Внедорожник'),
    ('wagon', 'Универсал'),
    ('minivan', 'Минивэн'),
    ('pickup', 'Пикап'),
    ('coupe', 'Купе'),
    ('cabrio', 'Кабриолет')
)


DRIVE_UNIT_CHOICES = (
    ('rear', 'Задний'),
    ('front', 'Передний'),
    ('full', 'Полный')
)


def current_year():
    return datetime.date.today().year


class Car(models.Model):
    model = models.CharField(max_length=50)
    year = models.IntegerField(default=current_year, validators=[MinValueValidator(2000),
                                                                 MaxValueValidator(current_year)])
    color = models.CharField(max_length=20)
    mileage = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    volume = models.DecimalField(default=0, max_digits=3, decimal_places=1)
    body_type = models.CharField(choices=BODY_TYPE_CHOICES, blank=True)
    drive_unit = models.CharField(choices=DRIVE_UNIT_CHOICES, blank=True)
    gearbox = models.CharField(choices=GEARBOX_CHOICES, blank=True)
    fuel_type = models.CharField(choices=FUEL_TYPE_CHOICES, blank=True)
    price = models.IntegerField(default=0, validators=[MinValueValidator(1),
                                                       MaxValueValidator(99_999_999)])
    image = models.ImageField()
    
    def __str__(self):
        return f'{self.model} {self.year}'


class Sale(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, default=None)
    car = models.ForeignKey(Car, on_delete=models.CASCADE, default=None)
    created_at = models.DateField(auto_now_add=True, null=True)

    def __str__(self):
        return f'{self.client} {self.car}'
