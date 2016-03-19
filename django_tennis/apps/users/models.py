from django.db import models
from model_utils.models import TimeStampedModel


class Club(TimeStampedModel):

    class Meta:
        pass


class Court(TimeStampedModel):
    club = models.ForeignKey(Club, related_name='courts', null=True, blank=True)

    class Meta:
        pass


class Player(TimeStampedModel):
    class Meta:
        pass
