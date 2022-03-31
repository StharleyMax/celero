from multiprocessing import Event
from rest_framework import serializers
from celero.models import Athlete, Game, Event, AthleteHasEvents

class AthleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Athlete
        fields = ['id', 'name', 'sex']

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['id', 'event', 'sport']

class GamesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ['game', 'season', 'year', 'city']

class AthleteHasEventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AthleteHasEvents
        fields = ['id', 'athlete', 'event', 'age', 'height', 'weight',
                  'team', 'medal']