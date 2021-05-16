from django import template
from os.path import dirname, abspath
import json

register = template.Library()

@register.filter
def match_champion(id):
    champion_name =''
    with open(dirname(dirname(abspath(__file__)))  + '/static/jsons/champions.json',
              encoding="utf8") as json_file:
        champions = json.load(json_file)

    for key,value in champions['data'].items():
        if str(id) == str(value['key']):
            champion_name = value['id']

    return champion_name

@register.filter
def get_champion_image(name):
    image_path = str("/static/images/champion/" + str(name) + ".png")
    return image_path


@register.filter
def get_spell_image(id):
    spell_key = ''

    with open(dirname(dirname(abspath(__file__)))  + '/static/jsons/summoner.json',
              encoding="utf8") as json_file:
        spells = json.load(json_file)

    for key,value in spells['data'].items():
        if str(id) == str(value['key']):
            spell_key = value['id']

    image_path = str("/static/images/spell/" + str(spell_key) + ".png")
    return image_path

@register.filter
def get_rune_image(id):
    rune_icon = ''

    with open(dirname(dirname(abspath(__file__)))  + '/static/jsons/runesReforged.json',
              encoding="utf8") as json_file:
        runes = json.load(json_file)

    for rune_type in runes:
        for slot in rune_type['slots']:
            for rune in slot['runes']:
                if id == rune['id']:
                    rune_icon = rune['icon']

    image_path = str("/static/images/" + str(rune_icon))
    return image_path

@register.filter
def get_secondary_rune_image(id):
    rune_icon = ''

    with open(dirname(dirname(abspath(__file__)))  + '/static/jsons/runesReforged.json',
              encoding="utf8") as json_file:
        runes = json.load(json_file)

    for rune_type in runes:
        for slot in rune_type['slots']:
            for rune in slot['runes']:
                if id == rune['id']:
                    rune_icon = rune_type['icon']

    image_path = str("/static/images/" + str(rune_icon))
    return image_path

@register.filter
def get_perk_image(id):
    image_path = str("/static/images/perk-images/StatMods/" + str(id) +".png")
    return image_path

@register.filter
def get_item_image(id):
    item_key = ''

    with open(dirname(dirname(abspath(__file__)))  + '/static/jsons/item.json',
              encoding="utf8") as json_file:
        item = json.load(json_file)

    for key,value in item['data'].items():
        if str(id) == str(key):
            item_key = key

    image_path = str("/static/images/item/" + str(item_key) + ".png")
    return image_path