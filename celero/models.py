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
    event = models.CharField(primary_key=True, max_length=100)
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

    def RenameColumnDataframe(dataframe: pd.DataFrame):
        return dataframe.rename(
            columns={
                'ID': 'athleteId_id',
                'Event': 'eventId_id',
                'Age': 'age',
                'NOC': 'noc',
                'Team': 'team',
                'Medal': 'medal',
                'Height': 'height',
                'Weight': 'weight'
            })

    def create(dataframe: pd.DataFrame, engine):
        columns = ["ID", "Event", "Age", "NOC", "Team", "Games", "Medal", "Height", "Weight"]
        athleteHasEvent = dataframe[columns].drop_duplicates(columns)
        athleteHasEvent = AthleteHasEvents.RenameColumnDataframe(athleteHasEvent)
        athleteHasEvent.to_sql(
            'testgames', if_exists="append", con=engine, index=False)

# olimpiadas


class Game(models.Model):
    game = models.CharField(primary_key=True, max_length=255)
    year = models.IntegerField()
    city = models.CharField(max_length=100)
    seasson = models.CharField(max_length=10)

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
    gameId = models.ForeignKey(Game, on_delete=models.CASCADE,)
    eventId = models.ForeignKey(Event, on_delete=models.CASCADE)

    def RenameColumnDataframe(dataframe: pd.DataFrame):
        return dataframe.rename(
            columns={
                'Games': 'gameId_id',
                'Event': 'eventId_id',
            })

    def create(dataframe: pd.DataFrame, engine):
        columns = ["Games", "Event"]
        eventGames = dataframe[columns].drop_duplicates(columns)
        eventGames = EventsHasGame.RenameColumnDataframe(eventGames)
        eventGames.to_sql(
            'celero_eventshasgame', if_exists="append", con=engine, index=False)

