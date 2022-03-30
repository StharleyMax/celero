from dataclasses import replace
from   django.core.management.base import BaseCommand
import pandas as pd
from celero.models import Athlete
from sqlalchemy import create_engine

class Command(BaseCommand):
    help = "A command to add dataset to databases"

    def handle(self, *args, **options):
        file = 'athlete_events.csv'
        df = pd.read_csv(file)
        print(df)

        engine = create_engine('sqlite:///db.sqlite3' )
        df.to_sql(Athlete._meta.db_table, if_exists='replace', con=engine, index=False)