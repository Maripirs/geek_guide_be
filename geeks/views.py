from django.shortcuts import render
from rest_framework.views import APIView
from . models import *
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, AllowAny
from rest_framework.response import Response
from . serializer import *


# Create your views here.

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


class LegendView(viewsets.ModelViewSet):
    queryset = Legend.objects.all()
    serializer_class = LegendSerializer
    permission_classes = [IsAdminUser | AllowAny]

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            self.permission_classes = [IsAdminUser]
        return super(LegendView, self).get_permissions()
