from django.db import models


class HomeModel(models.Model):
    name = models.CharField(max_length=3)
    birth = models.DateField()
