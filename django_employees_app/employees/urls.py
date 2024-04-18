from django.urls import path

from rest_framework import routers
from .views import PlayerSeasonStatViewSet, PlayerViewSet, SeasonViewSet

router = routers.DefaultRouter()

router.register('player', PlayerViewSet)

urlpatterns = router.urls