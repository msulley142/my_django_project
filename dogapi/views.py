from django.shortcuts import render
from rest_framework import viewsets
from .models import Dog, Breed
from .serializers import DogSerializer, BreedSerializer
# Create your views here.
# Version 1
class DogViewSet(viewsets.ModelViewSet):
    queryset = Dog.objects.all().select_related('breed').all().order_by('name')
    serializer_class = DogSerializer

class BreedViewSet(viewsets.ModelViewSet):
    queryset = Breed.objects.all().order_by('name')
    serializer_class = BreedSerializer