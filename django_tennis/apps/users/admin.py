from django.contrib import admin
from .models import *


class ClubAdmin(admin.ModelAdmin):
    class Meta:
        pass


class CourtAdmin(admin.ModelAdmin):
    class Meta:
        pass


class PlayerAdmin(admin.ModelAdmin):
    class Meta:
        pass


admin.site.register(Club, ClubAdmin)
admin.site.register(Court, CourtAdmin)
admin.site.register(Player, PlayerAdmin)