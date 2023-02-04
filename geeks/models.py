from django.db import models
from django import forms

# Create your models here.


class Game(models.Model):
    displayName = models.CharField(max_length=30)
    name = models.CharField(max_length=30, unique=True)
    image = models.ImageField(upload_to='images/', default=None)
    players = models.CharField(max_length=30)
    playingTime = models.CharField(max_length=30)
    bgg = models.CharField(max_length=1000)
    year = models.CharField(max_length=30)
    banner = models.ImageField(
        upload_to='images/', default=None, blank=True, null=True)

    def __str__(self):
        return self.displayName


class Section(models.Model):
    SECTION_TYPES = (
        ("Icon Legend", "Icon Legend"),
        ("Round Order", "Round Order"),
        ("Turn Order", "Turn Order")
    )
    HASHID_TYPES = (
        ("legend", "legend"),
        ("round", "round"),
        ("turn", "turn")
    )
    game = models.ForeignKey(
        Game, related_name="sections", on_delete=models.CASCADE)
    type = models.CharField(max_length=20, choices=SECTION_TYPES)

    hashid = models.CharField(max_length=20, choices=HASHID_TYPES)

    def __str__(self):
        return f'{self.type} {self.game.displayName}'


class Content(models.Model):
    CONTENT_TYPES = (
        ("legend", "legend"),
        ("example", "example"),
        ("description", "description")
    )
    DIRECTIONS = (
        ("flex-row", "flex-row"),
        ("flex-col", "flex-col"),
    )
    section = models.ForeignKey(
        Section, related_name='contents', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    text = models.TextField(max_length=1000)
    order = models.IntegerField()
    type = models.CharField(max_length=20, choices=CONTENT_TYPES)
    image = models.ImageField(upload_to='images/', default=None, blank=True)
    direction = models.CharField(max_length=20, choices=DIRECTIONS, default='flex-row')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['order']


class ExtendedContent(models.Model):
    CONTENT_TYPES = (
        ("legend", "legend"),
        ("example", "example"),
        ("description", "description")
    )
    DIRECTIONS = (
        ("flex-row", "flex-row"),
        ("flex-col", "flex-col"),
    )
    type = models.CharField(max_length=21, choices=CONTENT_TYPES)
    content = models.ForeignKey(
        Content, related_name='extended', on_delete=models.CASCADE
    )
    text = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='images/', default=None, blank=True)
    order = models.IntegerField()
    direction = models.CharField(max_length=20, choices=DIRECTIONS, default='flex-row')

    def __str__(self):
        return f'{self.type}'
