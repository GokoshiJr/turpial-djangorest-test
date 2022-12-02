from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api import views, pokemon_views, pokemon_storage_view, pokemon_party_view, user_view

urlpatterns = [

    path('login/', user_view.UserLogin.as_view()),

    path('seed/', views.Seed.as_view()),

    path('location/<int:pk>/', views.LocationDetail.as_view()),

    path('areas/<int:pk>/', views.AreaDetail.as_view()),

    path('regions/', views.RegionList.as_view()),
    path('regions/<int:pk>', views.RegionDetail.as_view()),

    path('pokemons/', pokemon_views.PokemonList.as_view()),
    path('pokemons/<int:pk>/', pokemon_views.PokemonDetail.as_view()),

    path('pokemons/own/', pokemon_storage_view.PokemonStorageList.as_view()),
    path('pokemons/own/<int:pk>/', pokemon_storage_view.PokemonStorageDetail.as_view()),

    path('pokemons/own/party/', pokemon_party_view.PokemonStoragePartyList.as_view()),
    path('pokemons/own/swap/', pokemon_party_view.PokemonStoragePartyDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
