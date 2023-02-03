from django.shortcuts import render
from rest_framework.views import APIView
from . models import *
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, AllowAny
from rest_framework.response import Response
from . serializer import *
from django.http import HttpResponse
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
# Create your views here.


class GameView(CreateView):
    model = Game
    fields ='__all__'
    template_name = "Game.html"
    success_url = "api/games"


class AllGamesView(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    permission_classes = [IsAdminUser | AllowAny]

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            self.permission_classes = [IsAdminUser]
        return super(AllGamesView, self).get_permissions()


class SingleGameView(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = SingleGameSerializer
    permission_classes = [IsAdminUser | AllowAny]
    lookup_field = 'name'

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            self.permission_classes = [IsAdminUser]
        return super(SingleGameView, self).get_permissions()


class SectionView(viewsets.ModelViewSet):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer
    permission_classes = [IsAdminUser | AllowAny]

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            self.permission_classes = [IsAdminUser]
        return super(SectionView, self).get_permissions()
