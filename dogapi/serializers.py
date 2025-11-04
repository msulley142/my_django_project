from rest_framework import serializers
from .models import Dog, Breed


#The following lines of codes were completed using GitHub Copilot assistant.
class DogSerializer(serializers.ModelSerializer):
    breed = serializers.PrimaryKeyRelatedField(queryset=Breed.objects.all())
    
    class Meta:
        model = Dog
        fields = '__all__'


class BreedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Breed
        fields = '__all__'