from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import PlayerSeasonStat, Player, Season
from .serializers import PlayerSeasonStatSerializer, PlayerSerializer, SeasonSerializer

# Create your views here.
class PlayerSeasonStatViewSet(ModelViewSet):
    queryset = PlayerSeasonStat.objects.all()
    serializer_class = PlayerSeasonStatSerializer

class PlayerViewSet(ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

class SeasonViewSet(ModelViewSet):
    queryset = Season.objects.all()
    serializer_class = SeasonSerializer
