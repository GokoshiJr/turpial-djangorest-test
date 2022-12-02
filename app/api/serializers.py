from rest_framework import serializers
from .models import Area, Region, Pokemon, Location, PokemonStorage

class AreaSerializer(serializers.ModelSerializer):
  class Meta:
    model = Area
    fields = ['pk', 'location', 'name', 'pokemons']

class RegionSerializer(serializers.ModelSerializer):
  class Meta:
    model = Region
    fields = ['pk', 'locations', 'name']

class PokemonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pokemon
        fields = [
            'pk',
            'abilities',
            'capture_rate',
            'color',
            'flavor_text',
            'height',
            'moves',
            'name',
            'sprites',
            'stats',
            'types',
            'weight'
        ]

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['pk', 'areas', 'name', 'region']

class PokemonStorageSerializer(serializers.ModelSerializer):
    specie = PokemonSerializer(many=False, read_only=True)

    class Meta:
        model = PokemonStorage
        fields = ['pk', 'specie', 'nick_name', 'is_party_member']

class PokemonStorageStringSerializer(serializers.ModelSerializer):
    class Meta:
        model = PokemonStorage
        fields = ['pk', 'specie', 'nick_name', 'is_party_member']
