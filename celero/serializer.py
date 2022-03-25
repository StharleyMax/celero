from rest_framework import serializers
from celero.models import Athlete

class AthleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Athlete
        fields = ['id', 'name', 'sex']
    