from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=50)
    money = models.PositiveIntegerField()
    population = models.PositiveIntegerField()
    army = models.BooleanField(default=False)

    def __str__(self):
        return self.name