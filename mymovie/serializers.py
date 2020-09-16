from rest_framework import serializers
from .models import Movie,Customer

class Movieserializer(serializers.ModelSerializer):
    class Meta:
        model=Movie
        fields='__all__'

class Customerserializer(serializers.ModelSerializer):
    class Meta:
        model=Customer
        fields='__all__'