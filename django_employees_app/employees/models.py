from django.db import models

# Create your models here.

class PlayerSeasonStat(models.Model):
    stat_id = models.BigIntegerField()
    player = models.ForeignKey('Player', on_delete=models.DO_NOTHING) #player_id
    season = models.ForeignKey('Season', on_delete=models.DO_NOTHING) #season_id
    
class Player(models.Model):
    player_id = models.BigIntegerField()
    name = models.CharField(max_length=255)
    pos = models.CharField(max_length = 8) 

    class Meta:
        ordering = ['player_id']   #order by player_id



class Season(models.Model):
    season_id = models.BigIntegerField()
    year = models.PositiveBigIntegerField()

    class Meta:
        ordering = ['season_id']   #order by player_id