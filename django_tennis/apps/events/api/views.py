from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import *


class TournamentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Tournament.objects.all()
    serializer_class = TournamentSerializer


class MatchViewset(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Match.objects.all()
    serializer_class = MatchSerializer