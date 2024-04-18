from rest_framework.serializers import ModelSerializer

from .models import PlayerSeasonStat, Season, Player

class PlayerSeasonStatSerializer(ModelSerializer):
    class Meta:
        model = PlayerSeasonStat
        fields = ["stat_id", "player", "season", "fgm", "fga", "fgp"]

class PlayerSerializer(ModelSerializer):
    class Meta:
        model = Player
        fields = ["player_id", "name", "position"]

class SeasonSerializer(ModelSerializer):
    class Meta:
        model = Season
        fields = ["season_id", "year"]