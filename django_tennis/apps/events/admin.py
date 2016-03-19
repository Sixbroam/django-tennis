from django.contrib import admin
from .models import *


class TournamentAdmin(admin.ModelAdmin):
    class Meta:
        pass


class MatchModelAdmin(admin.ModelAdmin):
    class Meta:
        pass


admin.site.register(Tournament, TournamentAdmin)
admin.site.register(Match, MatchModelAdmin)