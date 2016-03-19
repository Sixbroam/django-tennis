from django.db import models
from model_utils.models import TimeStampedModel, TimeFramedModel
from django_tennis.apps.users.models import Player


class Set(models.Model):
    # format = None
    number = models.IntegerField(blank=True, null=True)
    tiebreak_loser_score = models.IntegerField(blank=True, null=True)
    winner_score = models.IntegerField(blank=True, null=True)
    loser_score = models.IntegerField(blank=True, null=True)

    class Meta:
        pass


class Tournament(TimeFramedModel, TimeStampedModel):
    class Meta:
        pass


class Match(TimeStampedModel):

    players = models.ManyToManyField(Player, related_name='matches')
    winner = models.ForeignKey(Player, related_name='wins', blank=True, null=True)
    loser = models.ForeignKey(Player, related_name='losses', blank=True, null=True)
    sets = models.ManyToManyField(Set, related_name='score')

    class Meta:
        pass
