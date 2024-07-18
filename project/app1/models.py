from django.db import models

# Create your models here.
class Fuel(models.Model):
    fuel_name=models.CharField(max_length=50)
    fuel_price=models.IntegerField()
    def __str__(self):
        return self.fuel_name


class Car(models.Model):
    car_name=models.CharField(max_length=50)
    car_number=models.IntegerField()
    company_name=models.CharField(max_length=50)
    fuel_name=models.ManyToManyField(Fuel)

    def __str__(self):
        return self.car_name
