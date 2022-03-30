from rest_framework import viewsets
from celero.models import Athlete
from celero.serializer import AthleteSerializer

class AthleteViewSet(viewsets.ModelViewSet):
    queryset = Athlete.objects.all()
    serializer_class = AthleteSerializer