from django.db import models
from django.contrib.auth import get_user_model
class Country(models.Model):
    name = models.CharField(max_length=50)
    money = models.PositiveIntegerField()
    population = models.PositiveIntegerField()
    army = models.BooleanField(default=False)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True, blank=True, default=None)

    def __str__(self):
        return self.name