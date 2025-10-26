from rest_framework import status
from rest_framework.response import Response 
from rest_framework.views import APIView 
from .models import Dog , Breed
from .serializers import DogSerializer, BreedSerializer
from django.shortcuts import get_object_or_404



# Version 2

#Dog Detail, Dog List
class DogDetail(APIView):
    def get(self, request, pk):
        dog = get_object_or_404(Dog, pk=pk)
        serializer = DogSerializer(dog)
        return Response(serializer.data)

    def put(self, request, pk):
        dog = get_object_or_404(Dog, pk=pk)
        serializer = DogSerializer(dog, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        dog = get_object_or_404(Dog, pk=pk)
        dog.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    


class DogList(APIView):
    def get(self, request):
        dogs = Dog.objects.all().select_related('breed').order_by('name')
        serializer = DogSerializer(dogs, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

#Breed Detail, Breed List
class BreedDetail(APIView):
    def get(self, request, pk):
        breed = get_object_or_404(Breed, pk=pk)
        serializer = BreedSerializer(breed)
        return Response(serializer.data)

    def put(self, request, pk):
        breed = get_object_or_404(Breed, pk=pk)
        serializer = BreedSerializer(breed, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        breed = get_object_or_404(Breed, pk=pk)
        breed.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class BreedList(APIView):
    def get(self, request):
        breeds = Breed.objects.all().order_by('name')
        serializer = BreedSerializer(breeds, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BreedSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)