from django.core.validators import MinValue, MaxValue
from django.db import models

# Create your models here.
class Breed(models.Model):
    TINY = 'Tiny'
    SMALL = 'Small'
    MEDIUM = 'Medium'
    LARGE = 'Large'

    SIZE_CHOICES = [
        (TINY, 'Tiny'),
        (SMALL, 'Small'),
        (MEDIUM, 'Medium'),
        (LARGE, 'Large'),
    ]

    name = models.CharField(max_length=100)
    size = models.CharField(max_length=10, choices=SIZE_CHOICES)
    friendliness = models.IntegerField(validators=[MinValue(1), MaxValue(5)])
    trainability = models.IntegerField(validators=[MinValue(1), MaxValue(5)])
    shedding_amount = models.IntegerField(validators=[MinValue(1), MaxValue(5)])
    exercise_needs = models.IntegerField(validators=[MinValue(1), MaxValue(5)])
   

    def __str__(self):
        return self.name

class Dog(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE)
    gender = models.CharField(max_length=10)
    color = models.CharField(max_length=50)
    favorite_food = models.CharField(max_length=100)
    favorite_toy = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
