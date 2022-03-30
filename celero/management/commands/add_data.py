from dataclasses import replace
from django.core.management.base import BaseCommand
import pandas as pd
from celero.models import Athlete, Event, AthleteHasEvents, EventsHasGame, Game
from sqlalchemy import create_engine

class Command(BaseCommand):
    help = "A command to add dataset to databases"

    def handle(self, *args, **options):
        file = 'athlete_events.csv'
        df = pd.read_csv(file)

        engine = create_engine('sqlite:///db.sqlite3' )


        Athlete.create(df, engine)
        Event.create(df, engine)
        AthleteHasEvents.create(df, engine)
        Game.create(df, engine)
        EventsHasGame.create(df, engine)