from django.db import models
from django.contrib.auth.models import User
from model_utils.models import TimeStampedModel


class Club(TimeStampedModel):
    name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        pass


class Court(TimeStampedModel):
    club = models.ForeignKey(Club, related_name='courts', null=True, blank=True)

    class Meta:
        pass


class Player(TimeStampedModel):

    user = models.OneToOneField(User, related_name='player_profile', blank=True, null=True)

    class Meta:
        pass
