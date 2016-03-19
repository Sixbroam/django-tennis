from ..models import *
from rest_framework import serializers


class TournamentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tournament
        # fields = ('url', 'username', 'email', 'groups')


class MatchSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Match
        # fields = ('url', 'username', 'email', 'groups')