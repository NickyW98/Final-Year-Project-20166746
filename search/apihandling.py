from .models import Summoner, RankedQueue, Match, Participant
import requests

REGION = "euw1"
APIKEY = "API Key can be requested"

def getSummoner(summonerName):
    URL = "https://" + REGION + ".api.riotgames.com/lol/summoner/v4/summoners/by-name/" + summonerName + "?api_key=" + APIKEY
    response = requests.get(URL)
    json = response.json()
    return json

def getRanked(encrypted_id):
    URL = "https://" + REGION + ".api.riotgames.com/lol/league/v4/entries/by-summoner/" + encrypted_id + "?api_key=" + APIKEY
    response = requests.get(URL)
    json = response.json()
    return json

def getMatchList(account_id, start_index, end_index):
    URL = "https://" + REGION + ".api.riotgames.com/lol/match/v4/matchlists/by-account/" + account_id + "?endIndex=" + end_index + "&beginIndex=" + start_index + "&api_key=" + APIKEY
    response = requests.get(URL)
    json = response.json()
    return json

def getMatchDetails(gameId):
    URL = "https://" + REGION + ".api.riotgames.com/lol/match/v4/matches/" + str(gameId) + "?api_key=" + APIKEY
    response = requests.get(URL)
    json = response.json()
    return json


def insert_Summoner(json):
    encrypted_id = json['id']
    account_id = json['accountId']
    puuid = json['puuid']
    summoner_name = json['name']
    summoner_level = json['summonerLevel']
    profile_icon_id = json['profileIconId']
    if(len(Summoner.objects.filter(summoner_name=summoner_name))==0):
        summoner = Summoner.objects.create(encrypted_id=encrypted_id, account_id=account_id, puuid=puuid, summoner_name=summoner_name, summoner_level=summoner_level, profile_icon_id=profile_icon_id)
    else:
        summoner = Summoner.objects.filter(summoner_name=summoner_name).first()
    return summoner

def insert_RankedQueue(summoner_id, json):
    user = ''
    encrypted_id = summoner_id
    if (len(RankedQueue.objects.filter(encrypted_id=encrypted_id)) == 0):
        summoner = Summoner.objects.filter(encrypted_id=encrypted_id).first()
        user = RankedQueue.objects.create(encrypted_id=summoner)
    else:
        user = RankedQueue.objects.filter(encrypted_id=encrypted_id).first()
    for rank in json:
        if rank['queueType'] == "RANKED_SOLO_5x5":
            user.solo_queue_tier = rank['tier']
            user.solo_queue_rank = rank['rank']
            user.solo_queue_league_points = rank['leaguePoints']
            user.solo_queue_wins = rank['wins']
            user.solo_queue_losses = rank['losses']
        if rank['queueType'] == "RANKED_FLEX_SR":
            user.flex_queue_tier = rank['tier']
            user.flex_queue_rank = rank['rank']
            user.flex_queue_league_points = rank['leaguePoints']
            user.flex_queue_wins = rank['wins']
            user.flex_queue_losses = rank['losses']
    user.save()
    return user

def insert_Match(json):
    for match in json['matches']:
        if (len(Match.objects.filter(match_id=match['gameId'])) == 0):
            match_details = getMatchDetails(match['gameId'])
            new_match = Match.objects.create(match_id=match['gameId'], queue=match['queue'], match_duration=match_details['gameDuration'], date_played=match_details['gameCreation'])
            insert_Participant(match_details, new_match)

def insert_Participant(match_details, match):
    for participant in match_details['participantIdentities']:
        if (len(Participant.objects.filter(match_id=match_details['gameId'], encrypted_id=participant['player']['summonerId'])) == 0 ):
            for pp in match_details['participants']:
                if pp['participantId'] == participant['participantId']:
                    pick = pp['championId']
                    spell_one = pp['spell1Id']
                    spell_two = pp['spell2Id']
                    win = pp['stats']['win']
                    item_one = pp['stats']['item0']
                    item_two = pp['stats']['item1']
                    item_three = pp['stats']['item2']
                    item_four = pp['stats']['item3']
                    item_five = pp['stats']['item4']
                    item_six = pp['stats']['item5']
                    kills = pp['stats']['kills']
                    deaths = pp['stats']['deaths']
                    assists = pp['stats']['assists']
                    champion_level = pp['stats']['champLevel']
                    primary_rune_one = pp['stats']['perk0']
                    primary_rune_two = pp['stats']['perk1']
                    primary_rune_three = pp['stats']['perk2']
                    primary_rune_four = pp['stats']['perk3']
                    secondary_rune_one = pp['stats']['perk4']
                    secondary_rune_two = pp['stats']['perk5']
                    stat_rune_one = pp['stats']['statPerk0']
                    stat_rune_two = pp['stats']['statPerk1']
                    stat_rune_three = pp['stats']['statPerk2']
                    break
            encrypted_id = participant['player']['summonerId']
            participants = Participant.objects.create(match_id=match, name=participant['player']['summonerName'], participant_index=participant['participantId'], pick=pick, summoner_spell_one=spell_one,
                                                      summoner_spell_two=spell_two, win=win, item_one=item_one, item_two=item_two, item_three=item_three,
                                                      item_four=item_four, item_five=item_five, item_six=item_six, kills=kills,
                                                      deaths=deaths, assists=assists, champion_level=champion_level, primary_rune_one=primary_rune_one,
                                                      primary_rune_two=primary_rune_two, primary_rune_three=primary_rune_three, primary_rune_four=primary_rune_four,
                                                      secondary_rune_one=secondary_rune_one, secondary_rune_two=secondary_rune_two, stat_rune_one=stat_rune_one,
                                                      stat_rune_two=stat_rune_two, stat_rune_three=stat_rune_three, encrypted_id=encrypted_id)
    return

def get_matches_for_participant(participant):
    matches = Participant.objects.filter(encrypted_id=participant).order_by('-match_id')
    return matches

def get_match_details_from_db(matchId):
    details = Match.objects.filter(match_id=matchId)
    return details

def get_ranked_image(encrypted_id):
    images = {}
    user = RankedQueue.objects.filter(encrypted_id=encrypted_id).first()
    if len(user.flex_queue_rank) < 1:
        images['flex'] = "/static/images/ranks/" + 'unranked.png'
    else:
        images['flex'] = "/static/images/ranks/" + user.flex_queue_tier.lower() + ".png"
    if len(user.solo_queue_rank) < 1:
        images['solo'] = "/static/images/ranks/" + 'unranked.png'
    else:
        images['solo'] = "/static/images/ranks/" + user.solo_queue_tier.lower() + ".png"

    return images

def get_participants_for_a_game(matchId):
    participants = []
    match = Match.objects.filter(match_id=matchId).first()
    for participant in Participant.objects.filter(match_id=match):
            participants.append(participant)
    return participants




