from django.db import models

# Create your models here.

class IceCream(models.Model):
    flavor = models.CharField(max_length=100)
    topping = models.CharField(max_length=100)
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.flavor} ice cream"