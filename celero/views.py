from multiprocessing import Event
from rest_framework import viewsets
from celero.models import Athlete, Event, AthleteHasEvents, Game
from celero.serializer import AthleteSerializer, EventSerializer, GamesSerializer, AthleteHasEventsSerializer

class AthleteViewSet(viewsets.ModelViewSet):
    queryset = Athlete.objects.all()
    serializer_class = AthleteSerializer

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class AthleteHasEventsViewSet(viewsets.ModelViewSet):
    queryset = AthleteHasEvents.objects.all()
    serializer_class = AthleteHasEventsSerializer

class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GamesSerializer