from rest_framework import serializers
from . models import *


class ExtendedContentSerializer(serializers.ModelSerializer):

    class Meta:
        model = ExtendedContent
        fields = ['image', 'text', 'type', 'order', 'direction']


class ContentSerializer(serializers.ModelSerializer):

    extended = ExtendedContentSerializer(
        many=True,
        read_only=True
    )

    class Meta:
        model = Content
        fields = ['text', 'name', 'extended', 'image', 'type', 'direction']


class SectionSerializer(serializers.ModelSerializer):
    contents = ContentSerializer(
        many=True,
        read_only=True
    )

    class Meta:
        model = Section
        fields = ['type', 'contents', 'hashid']


class SectionNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = ['type',  'hashid']


class GameSerializer(serializers.ModelSerializer):
    sections = SectionNameSerializer(
        many=True,
        read_only=True,
    )

    class Meta:
        model = Game
        fields = ['id', 'displayName', 'name', 'image', 'sections']


class SingleGameSerializer(serializers.ModelSerializer):
    sections = SectionSerializer(
        many=True,
        read_only=True,
    )

    class Meta:
        model = Game
        fields = ['displayName', 'name', 'image', 'year', 'players',
                  'playingTime', 'bgg', 'sections', 'banner']
        lookup_field = 'name'
        extra_kwargs = {
            'url': {'lookup_field': 'name'}
        }
