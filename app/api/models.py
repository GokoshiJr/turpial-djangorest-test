from django.db import models

# Create your models here.

"""
{
    "location": "canalave-city",
    "name": "canalave-city-area",
    "pokemons": [
        "tentacool",
        "tentacruel",
        "staryu",
        "magikarp",
        "gyarados",
        "wingull",
        "pelipper",
        "shellos",
        "gastrodon",
        "finneon",
        "lumineon"
    ]
},
 """
class Area(models.Model):
    location = models.CharField(max_length=100, default='')
    name = models.CharField(max_length=100, default='')
    pokemons = models.JSONField(null=True)

"""
{
    "areas": [
        "canalave-city-area"
    ],
    "name": "canalave-city",
    "region": "sinnoh"
},
"""
class Location(models.Model):
    areas = models.JSONField(null=True)
    name = models.CharField(max_length=100, default='')
    region = models.CharField(max_length=100, default='')

"""
{
    "locations": [
        "celadon-city",
        "cerulean-city",
        "cinnabar-island",
    ],
    "name": "kanto"
},
"""
class Region(models.Model):
    locations = models.JSONField(null=True)
    name = models.CharField(max_length=100, default='')

"""
{
    "abilities": [
        "chlorophyll",
        "overgrow"
    ],
    "capture_rate": 45,
    "color": "green",
    "flavor_text": "Bulbasaur can be seen napping in bright sunlight.\nThere is a seed on its back. By soaking up the sun\u2019s rays,\nthe seed grows progressively larger.",
    "height": 7,
    "moves": [
        "razor-wind",
        "swords-dance",
        "cut",

    ],
    "name": "Bulbasaur",
    "sprites": {
        "back_default": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/1.png",
        "back_female": null,
        "back_shiny": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/shiny/1.png",
        "back_shiny_female": null,
        "front_default": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/1.png",
        "front_female": null,
        "front_shiny": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/1.png",
        "front_shiny_female": null
    },
    "stats": [
        {
            "name": "speed",
            "value": 45
        },
        {
            "name": "special-defense",
            "value": 65
        },
        {
            "name": "special-attack",
            "value": 65
        },
        {
            "name": "defense",
            "value": 49
        },
        {
            "name": "attack",
            "value": 49
        },
        {
            "name": "hp",
            "value": 45
        }
    ],
    "types": [
        "poison",
        "grass"
    ],
    "weight": 69
}
"""
class Pokemon(models.Model):
    abilities = models.JSONField(null=True)
    capture_rate = models.FloatField(default=0)
    color = models.CharField(max_length=100, default='')
    flavor_text = models.CharField(max_length=400, default='')
    height = models.FloatField(default=0)
    moves = models.JSONField(null=True)
    name = models.CharField(max_length=100, default='')
    sprites = models.JSONField(null=True)
    stats = models.JSONField(null=True)
    types = models.JSONField(null=True)
    weight = models.JSONField(null=True)

class PokemonStorage(models.Model):
    is_party_member = models.BooleanField(default=False)
    specie = models.ForeignKey(Pokemon, on_delete=models.DO_NOTHING, null=True)
    nick_name = models.CharField(max_length=100, default='pokemon')
