from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import *


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PlayerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer


class ClubViewset(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Club.objects.all()
    serializer_class = ClubSerializer