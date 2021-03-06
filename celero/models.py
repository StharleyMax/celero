from pyexpat import model
from django.db import models
import pandas as pd


class Athlete(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=255)
    sex = models.CharField(max_length=1)

    def __str__(self):
        return self.name

    def RenameColumnDataframe(dataframe: pd.DataFrame):
        return dataframe.rename(
            columns={'ID': 'id', 'Name': 'name', 'Sex': 'sex'})

    def create(dataframe: pd.DataFrame, engine):
        columns = ["ID", "Name", "Sex"]
        athletes = dataframe[columns].drop_duplicates(columns)
        athletes = Athlete.RenameColumnDataframe(athletes)
        athletes.to_sql(
            'celero_athlete', if_exists="append", con=engine, index=False)


class Event(models.Model):
    id = models.AutoField(primary_key=True)
    event = models.CharField( max_length=100)
    sport = models.CharField(max_length=100)

    def __str__(self):
        return self.event

    def RenameColumnDataframe(dataframe: pd.DataFrame):
        return dataframe.rename(
            columns={'Event': 'event', 'Sport': 'sport'})

    def create(dataframe: pd.DataFrame, engine):
        columns = ["Event", "Sport"]
        events = dataframe[columns].drop_duplicates(columns)
        events = Event.RenameColumnDataframe(events)
        events.to_sql(
            'celero_event', if_exists="append", con=engine, index=False)


class AthleteHasEvents(models.Model):
    id = models.AutoField(primary_key=True)
    athlete = models.ForeignKey(Athlete, on_delete=models.CASCADE,)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    age = models.IntegerField(null=True)
    noc = models.CharField(max_length=3)
    team = models.CharField(max_length=25)
    medal = models.CharField(max_length=6, null=True)
    height = models.IntegerField(null=True)
    weight = models.IntegerField(null=True)
    game = models.CharField(max_length=100)

    def __str__(self):
        return self.eventId

    def RenameColumnDataframe(dataframe: pd.DataFrame):
        return dataframe.rename(
            columns={
                'ID': 'athlete_id',
                'Event': 'event_id',
                'Age': 'age',
                'NOC': 'noc',
                'Team': 'team',
                'Medal': 'medal',
                'Height': 'height',
                'Weight': 'weight',
                'Games': 'game'
            })

    def create(dataframe: pd.DataFrame, engine):
        columns = ["ID", "Event", "Age", "NOC", "Team", "Games", "Medal", "Height", "Weight"]
        athleteHasEvent = dataframe[columns].drop_duplicates(columns)
        athleteHasEvent = AthleteHasEvents.RenameColumnDataframe(athleteHasEvent)
        athleteHasEvent.to_sql(
            'celero_athletehasevents', if_exists="append", con=engine, index=False)

# olimpiadas


class Game(models.Model):
    id = models.AutoField(primary_key=True)
    game = models.CharField(max_length=255)
    year = models.IntegerField()
    city = models.CharField(max_length=100)
    season = models.CharField(max_length=10)

    def __str__(self):
        return self.game
    
    def RenameColumnDataframe(dataframe: pd.DataFrame):
        return dataframe.rename(
            columns={
                'Games': 'game',
                'Year': 'year',
                'City': 'city',
                'Season': 'season',
            })

    def create(dataframe: pd.DataFrame, engine):
        columns = ["Games", "Year", "City", "Season"]
        games = dataframe[columns].drop_duplicates(columns)
        games = Game.RenameColumnDataframe(games)
        games.to_sql(
            'celero_game', if_exists="append", con=engine, index=False)


class EventsHasGame(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE,)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

    def RenameColumnDataframe(dataframe: pd.DataFrame):
        return dataframe.rename(
            columns={
                'Games': 'game_id',
                'Event': 'event_id',
            })

    def create(dataframe: pd.DataFrame, engine):
        columns = ["Games", "Event"]
        eventGames = dataframe[columns].drop_duplicates(columns)
        eventGames = EventsHasGame.RenameColumnDataframe(eventGames)
        eventGames.to_sql(
            'celero_eventshasgame', if_exists="append", con=engine, index=False)

