from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view
from .models import Area, Region, Location, Pokemon, PokemonStorage
from .serializers import AreaSerializer, RegionSerializer, PokemonSerializer, PokemonStorageSerializer, PokemonStorageStringSerializer
from rest_framework.views import APIView
import json
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

# Create your views here.

class PokemonStorageList(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    # Pokemon Storage
    def get(self, request, format=None):
        pokemon_storage = PokemonStorage.objects.select_related('specie').all()
        serializer = PokemonStorageSerializer(pokemon_storage, many=True)
        return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)

    # Pokemon Catch
    def post(self, request, format=None):
        serializer = PokemonStorageStringSerializer(data=request.data)
        if (len(PokemonStorage.objects.all())):
            if (len(PokemonStorage.objects.filter(is_party_member=True)) == 6 and request.data["is_party_member"] == True):
                return JsonResponse(data={'msg': 'the storage is at its limit of 6 pokemon'}, status=status.HTTP_400_BAD_REQUEST)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PokemonStorageDetail(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    # check if pokemonstorage exists
    def get_object(self, pk):
        try:
            return PokemonStorage.objects.get(pk=pk)
        except PokemonStorage.DoesNotExist:
            HttpResponse(status=status.HTTP_404_NOT_FOUND)

    # Pokemon Rename
    def put(self, request, pk, format=None):
        try:
            PokemonStorage.objects.filter(pk=pk).update(nick_name=request.data["nick_name"])
            pokemon_storage = self.get_object(pk)
            pokemon_storage = PokemonStorageStringSerializer(pokemon_storage)
            return JsonResponse(pokemon_storage.data, status=status.HTTP_200_OK)
        except:
            return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

    # Pokemon Release
    def delete(self, request, pk, format=None):
        try:
            pokemon_storage = self.get_object(pk)
            pokemon_storage.delete()
            return HttpResponse(status=status.HTTP_204_NO_CONTENT)
        except:
            return HttpResponse(status=status.HTTP_400_BAD_REQUEST)
