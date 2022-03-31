from django.contrib import admin
from django.urls import path, include
from celero.views import AthleteHasEventsViewSet, AthleteViewSet, EventViewSet, GameViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'atlhetes', AthleteViewSet)
router.register(r'events', EventViewSet)
router.register(r'atlhete_has_events', AthleteHasEventsViewSet)
router.register(r'games', GameViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
