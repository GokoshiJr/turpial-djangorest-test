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

class PokemonStoragePartyList(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    # Pokemon Party
    def get(self, request, format=None):
        pokemon_storage = PokemonStorage.objects.select_related('specie').filter(is_party_member=True)
        serializer = PokemonStorageSerializer(pokemon_storage, many=True)
        return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)

class PokemonStoragePartyDetail(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    # Swap party member
    def post(self, request, format=None):
        if (request.data["leaving_the_party"] != None):
            try:
                # check if pokemon exists in party badge
                PokemonStorage.objects.get(pk=request.data["leaving_the_party"])
                # filter and update
                PokemonStorage.objects.filter(pk=request.data["leaving_the_party"]).update(is_party_member=False)
            except PokemonStorage.DoesNotExist:
                return JsonResponse(data={"msg":"(leaving) dont have this pokemon in your storage"}, status=status.HTTP_400_BAD_REQUEST)

        if (request.data["entering_the_party"] != None):
            try:
                # check if pokemon exists in party badge
                PokemonStorage.objects.get(pk=request.data["entering_the_party"])
                # check if badge is full
                if (len(PokemonStorage.objects.filter(is_party_member=True)) != 6):
                    PokemonStorage.objects.filter(pk=request.data["entering_the_party"]).update(is_party_member=True)
                else:
                    return JsonResponse(data={"msg":"party badge is full"}, status=status.HTTP_400_BAD_REQUEST)
            except PokemonStorage.DoesNotExist:
                return JsonResponse(data={"msg":"(entering) dont have this pokemon in your storage"}, status=status.HTTP_400_BAD_REQUEST)

        pokemon_storage = PokemonStorage.objects.select_related('specie').filter(is_party_member=True)
        serializer = PokemonStorageSerializer(pokemon_storage, many=True)
        return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)
