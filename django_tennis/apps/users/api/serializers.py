from ..models import *
from django.contrib.auth.models import User, Group
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class PlayerSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Player
        # fields = ('url', 'username', 'email', 'groups')


class ClubSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Club
        # fields = ('url', 'username', 'email', 'groups')