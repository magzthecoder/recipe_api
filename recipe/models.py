from django.db import models
from django.contrib.auth.models import User

class Recipe(models.Model):
    favourited_by = models.ManyToManyField(User)
    name = models.CharField(max_length=80)
    description = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=9,decimal_places=2)

    def __str__(self):
        return self.name