from django.db import models


class Summoner(models.Model):
    encrypted_id = models.CharField(max_length=63, primary_key=True)
    summoner_name = models.CharField(max_length=16)
    account_id = models.CharField(max_length=56)
    puuid = models.CharField(max_length=78)
    summoner_level = models.CharField(max_length=4)
    profile_icon_id = models.CharField(max_length=5)

    def __str__(self):
        return self.summoner_name

class RankedQueue(models.Model):
    ranked_queue_id = models.IntegerField(primary_key=True)
    encrypted_id = models.ForeignKey(Summoner, on_delete=models.CASCADE)
    solo_queue_tier = models.CharField(max_length=12)
    solo_queue_rank = models.CharField(max_length=3)
    solo_queue_league_points = models.CharField(max_length=3)
    solo_queue_wins = models.CharField(max_length=4)
    solo_queue_losses = models.CharField(max_length=4)
    flex_queue_tier = models.CharField(max_length=12)
    flex_queue_rank = models.CharField(max_length=3)
    flex_queue_league_points = models.CharField(max_length=3)
    flex_queue_wins = models.CharField(max_length=4)
    flex_queue_losses = models.CharField(max_length=4)

    def __str__(self):
        return str(self.encrypted_id)

class Match(models.Model):
    match_id = models.IntegerField(primary_key=True)
    queue = models.IntegerField()
    match_duration = models.IntegerField()
    date_played = models.IntegerField()

class Participant(models.Model):
    participant_id = models.IntegerField(primary_key=True)
    participant_index = models.IntegerField()
    match_id = models.ForeignKey(Match, on_delete=models.CASCADE)
    name = models.CharField(max_length=16)
    encrypted_id = models.CharField(max_length=63)
    pick = models.IntegerField()
    win = models.BooleanField()
    summoner_spell_one = models.IntegerField()
    summoner_spell_two = models.IntegerField()
    item_one = models.IntegerField()
    item_two = models.IntegerField()
    item_three = models.IntegerField()
    item_four = models.IntegerField()
    item_five = models.IntegerField()
    item_six = models.IntegerField()
    kills = models.IntegerField()
    deaths = models.IntegerField()
    assists = models.IntegerField()
    champion_level = models.IntegerField()
    primary_rune_one = models.IntegerField()
    primary_rune_two = models.IntegerField()
    primary_rune_three = models.IntegerField()
    primary_rune_four = models.IntegerField()
    secondary_rune_one = models.IntegerField()
    secondary_rune_two = models.IntegerField()
    stat_rune_one = models.IntegerField()
    stat_rune_two = models.IntegerField()
    stat_rune_three = models.IntegerField()

    def __str__(self):
        return str(self.name)

class MatchList(models.Model):
    match_list_id = models.IntegerField(primary_key=True)
    encrypted_id = models.ForeignKey(Summoner, on_delete=models.CASCADE)
    champion = models.IntegerField()
    role = models.CharField(max_length=6)
    match_outcome = models.CharField(max_length=4)


