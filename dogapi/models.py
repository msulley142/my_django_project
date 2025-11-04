from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

# Create your models here.
#The following lines of codes were completed using GitHub Copilot assistant.
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
    friendliness = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    trainability = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    shedding_amount = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    exercise_needs = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
   

    def __str__(self):
        return self.name
    

#The following lines of codes were completed using GitHub Copilot assistant.

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
    
