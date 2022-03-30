from   django.core.management.base import BaseCommand
import pandas as pd

class Command(BaseCommand):
    help = "A command to add dataset to databases"

    def handle(self, *args, **options):
        file = 'athlete_events.csv'
        df = pd.read_csv(file)
        print(df)