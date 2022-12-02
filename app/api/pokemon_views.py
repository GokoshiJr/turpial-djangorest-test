from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view
from .models import Area, Region, Location, Pokemon
from .serializers import AreaSerializer, RegionSerializer, PokemonSerializer
from rest_framework.views import APIView
import json

# Create your views here.

class PokemonList(APIView):
    def get(self, request, format=None):
        pokemons = Pokemon.objects.all()
        serializer = PokemonSerializer(pokemons, many=True)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request, format=None):
        serializer = PokemonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PokemonDetail(APIView):
    def get_object(self, pk):
        try:
            return Pokemon.objects.get(pk=pk)
        except Pokemon.DoesNotExist:
            HttpResponse(status=status.HTTP_404_NOT_FOUND)

    # Pokemon specie detail
    def get(self, request, pk, format=None):
        pokemon = self.get_object(pk)
        serializer = PokemonSerializer(pokemon)
        return JsonResponse(serializer.data, status=status.HTTP_200_OK)

    """ def put(self, request, pk, format=None):
        pokemon = self.get_object(pk)
        serializer = PokemonSerializer(pokemon, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        pokemon = self.get_object(pk)
        pokemon.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT) """
