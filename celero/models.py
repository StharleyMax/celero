from django.db import models
from enum import Enum

class Athlete(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=255)
    sex = models.CharField(max_length=1)

    def __str__(self):
        return self.name

class Event(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    event = models.CharField(max_length=100)
    sport = models.CharField(max_length=100)

    def __str__(self):
        return self.event

class AthleteHasEvents(models.Model):
    atlheteId = models.ForeignKey(Athlete, on_delete=models.CASCADE,)
    eventId = models.ForeignKey(Event, on_delete=models.CASCADE)
    age = models.IntegerField()
    noc = models.CharField(max_length=3)
    team = models.CharField(max_length=25)
    medal = models.CharField(max_length=6)
    height = models.IntegerField(null=True)
    weight = models.IntegerField(null=True)

    def __str__(self):
        return self.eventId

#olimpiadas
class Game(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    game = models.CharField(max_length=255)
    year = models.IntegerField()
    city = models.CharField(max_length=100)
    seasson = models.CharField(max_length=10)

    def __str__(self):
        return self.game

class EventsHasGame(models.Model):
    gameId = models.ForeignKey(Game, on_delete=models.CASCADE,)
    eventId = models.ForeignKey(Event, on_delete=models.CASCADE)
    