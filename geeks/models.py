from django.db import models
from django import forms
from django_jsonform.models.fields import ArrayField

# Create your models here.


class Game(models.Model):
    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to='images/', default=None)
    players = models.CharField(max_length=30)
    playingTime = models.CharField(max_length=30)
    bgg = models.CharField(max_length=1000)
    year = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Section(models.Model):
    SECTION_TYPES = (
        ("Icon Legend", " Icon Legend"),
        ("Turn Order", "Turn Order")
    )
    game = models.ForeignKey(
        Game, related_name="sections", on_delete=models.CASCADE)
    type = models.CharField(max_length=20, choices=SECTION_TYPES)
    content = ArrayField(models.CharField(
        max_length=2000, blank=True))

    def __str__(self):
        return f'{self.type} {self.game.__str__}'


class Legend(models.Model):
    section = models.ForeignKey(
        Section, related_name='legends', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/', default=None)
    description = models.CharField(max_length=1000)
    name = models.CharField(max_length=100)
    order = models.IntegerField()

    def __str__(self):
        return self.name
