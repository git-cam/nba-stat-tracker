from django.contrib import admin

# Register your models here.
from .models import PlayerSeasonStat, Season, Player

admin.site.register(PlayerSeasonStat)
admin.site.register(Player)
admin.site.register(Season)