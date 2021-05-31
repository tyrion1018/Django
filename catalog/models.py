from django.db import models


# Create your models here.


class Country(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name[0]


class City(models.Model):
    name = models.CharField(max_length=10)


class Person(models.Model):
    name = models.CharField(max_length=10, help_text="Enter your full name")
    birthdate = models.DateField(null=True, blank=True)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name
