from rest_framework import serializers
from . models import *


class GameSerializer(serializers.ModelSerializer):

    class Meta:
        model = Game
        fields = ['id', 'name', 'image']


class LegendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Legend
        fields = ['section', 'image', 'description', 'name']


class SectionSerializer(serializers.ModelSerializer):
    legends = LegendSerializer(
        many=True,
        read_only=True,
    )

    class Meta:
        model = Section
        fields = ['game', 'type', 'legends', 'content']


class SingleGameSerializer(serializers.ModelSerializer):
    sections = SectionSerializer(
        many=True,
        read_only=True,
    )

    class Meta:
        model = Game
        fields = ['name', 'image', 'year', 'players',
                  'playingTime', 'bgg', 'sections']
