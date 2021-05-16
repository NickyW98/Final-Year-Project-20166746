from django.contrib import admin
from .models import Summoner, RankedQueue, Match, Participant, MatchList

admin.site.register(Summoner)
admin.site.register(RankedQueue)
admin.site.register(Match)
admin.site.register(Participant)
admin.site.register(MatchList)