from django.shortcuts import render
import json
import os
from . import apihandling

def HomePage(request):
    return render(request, "home page.html")

def SearchPage(request):
    summonerName = request.GET['query']

    summoner_json = apihandling.getSummoner(summonerName)
    ranked_json = apihandling.getRanked(summoner_json['id'])
    matches_json = apihandling.getMatchList(summoner_json['accountId'], '0', '10')

    summoner = apihandling.insert_Summoner(summoner_json)
    ranked_queue = apihandling.insert_RankedQueue(summoner_json['id'], ranked_json)
    apihandling.insert_Match(matches_json)

    matches= apihandling.get_matches_for_participant(summoner.encrypted_id)
    match_details = []
    participants = []
    for match in matches:
        match_details.append(apihandling.get_match_details_from_db(match.match_id.match_id))
        participants.append(apihandling.get_participants_for_a_game(match.match_id.match_id))

    with open(os.path.dirname(os.path.realpath(__file__)) + '/static/jsons/queues.json') as json_file:
        queue_types = json.load(json_file)

    profileIconPath = str("/static/images/profileicon/" + str(summoner_json['profileIconId']) + ".png")
    ranked_image = apihandling.get_ranked_image(summoner_json['id'])

    params = {'search': summoner_json, 'profileIconPath': profileIconPath, 'ranked_json' : ranked_queue, 'ranked_image': ranked_image, 'matches' : matches, 'match_details': match_details, 'queue_types':queue_types,
              'participants':participants}
    return render(request, 'search.html', params)

def webpage1(request):
    return render(request, "home page.html")

def test(request):
    return render(request, "search.html")

