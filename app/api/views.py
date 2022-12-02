from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view
from .models import Area, Region, Location, Pokemon
from .serializers import AreaSerializer, RegionSerializer, LocationSerializer, PokemonSerializer
from rest_framework.views import APIView
import json

# Create your views here.

class Seed(APIView):
    def get(self, request, format=None):
        # seed regions
        if (len(Region.objects.all()) == 0):
            f = open('api/db/regions.json')
            regions_data = json.load(f)
            regions = regions_data["data"]
            bulk_array = []

            for region in regions:
                bulk_array.append(Region(
                    locations=region["locations"],
                    name=region["name"]
                ))
            Region.objects.bulk_create(bulk_array)
            f.close()
            print("Regions seeded successfully")

        # seed locations
        if (len(Location.objects.all()) == 0):
            f = open('api/db/locations.json')
            locations_data = json.load(f)
            locations = locations_data["data"]
            bulk_array = []
            for location in locations:
                bulk_array.append(Location(
                    areas=location["areas"],
                    name=location["name"],
                    region=location["region"]
                ))
            Location.objects.bulk_create(bulk_array)
            f.close()
            print("Locations seeded successfully")

        # seed areas
        if (len(Area.objects.all()) == 0):
            f = open('api/db/areas.json')
            areas_data = json.load(f)
            areas = areas_data["data"]
            bulk_array = []
            for area in areas:
                bulk_array.append(Area(
                    location=area["location"],
                    name=area["name"],
                    pokemons=area["pokemons"]
                ))
            Area.objects.bulk_create(bulk_array)
            f.close()
            print("Areas seeded successfully")

        # seed pokemons
        if (len(Pokemon.objects.all()) == 0):
            f = open('api/db/pokemons.json')
            pokemons_data = json.load(f)
            pokemons = pokemons_data["data"]
            bulk_array = []
            for pokemon in pokemons:
                bulk_array.append(Pokemon(
                    abilities=pokemon["abilities"],
                    capture_rate=pokemon["capture_rate"],
                    color=pokemon["color"],
                    flavor_text=pokemon["flavor_text"],
                    height = pokemon["height"],
                    moves = pokemon["moves"],
                    name = pokemon["name"],
                    sprites = pokemon["sprites"],
                    stats = pokemon["stats"],
                    types = pokemon["types"],
                    weight = pokemon["weight"],
                ))
            Pokemon.objects.bulk_create(bulk_array, batch_size=100)
            f.close()
            print("Pokemons seeded successfully")

        return HttpResponse(status=status.HTTP_201_CREATED)

class RegionList(APIView):
    def get(self, request, format=None):
        regions = Region.objects.all().values("name", "pk")
        serializer = RegionSerializer(regions, many=True)
        return JsonResponse(serializer.data, safe=False)

class RegionDetail(APIView):
    def get_object(self, pk):
        try:
            return Region.objects.get(pk=pk)
        except Region.DoesNotExist:
            HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk, format=None):
        region = self.get_object(pk)
        serializer = RegionSerializer(region)
        return JsonResponse(serializer.data)

class LocationDetail(APIView):
    def get_object(self, pk):
        try:
            return Location.objects.get(pk=pk)
        except Location.DoesNotExist:
            HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk, format=None):

        location = self.get_object(pk)
        serializer = LocationSerializer(location)

        # areas fetching
        area_array = []
        areas_data = Area.objects.filter(name__in=serializer.data["areas"]).all()

        for area in areas_data:
            r = AreaSerializer(area)
            my_dict = dict(r.data)
            count_pokemon = 0

            for pokemon in my_dict["pokemons"]:
                count_pokemon += 1

            my_dict.pop("pokemons")
            my_dict.update({"pokemon_count": count_pokemon})
            my_dict.update({"location": serializer.data["pk"]})
            area_array.append(my_dict)

        result = dict(serializer.data)
        result.update({"areas": area_array})

        region = Region.objects.filter(name=result["region"]).get()
        region_serilizer = RegionSerializer(region)

        result.update({"region": region_serilizer.data["pk"]})
        return JsonResponse(result)

class AreaDetail(APIView):
    def get_object(self, pk):
        try:
            return Area.objects.get(pk=pk)
        except Area.DoesNotExist:
            HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk, format=None):
        area = self.get_object(pk)
        area = AreaSerializer(area)
        area = area.data

        pokemons_array = []
        pokemon_count = 0
        for pokemon_name in area["pokemons"]:
            pokemon_count += 1
            pokemon = Pokemon.objects.filter(name=pokemon_name).get()
            pokemon = PokemonSerializer(pokemon)
            pokemons_array.append(pokemon.data)

        location = Location.objects.filter(name=area["location"]).get()
        location = LocationSerializer(location)

        area.update({"location": location.data["pk"]})
        area.update({"pokemons": pokemons_array})
        area.update({"pokemon_count": pokemon_count})

        return JsonResponse(area, status=status.HTTP_200_OK)
