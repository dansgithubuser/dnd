import enum
import random

Feature = enum.Enum('Feature', [
    'BIG_BAD',
    'COMBAT',
    'EXPLORATION',
    'OUTDOORS',
    'QUEST',
    'QUEST_GIVER',
    'TOWN',
])

class Encounter:
    def __init__(self, description, features):
        self.description = description
        self.features = features

def enc(description, features):
    return Encounter(description, [getattr(Feature, i) for i in features.split()])

listing = [
    enc('grey (neutral) dragon that hordes treasure', 'QUEST_GIVER'),
    enc('order of clerics that are actually necromancers', 'BIG_BAD'),
    enc('a raccoon drank all the potions in the apothecary', 'QUEST TOWN'),
    enc('goblin ambush!', 'QUEST COMBAT'),
    enc('attacked by local wildlife', 'OUTDOORS COMBAT'),
    enc('amateur necromancy', 'COMBAT QUEST'),
    enc('pirates!', 'COMBAT QUEST'),
    enc('sylph', 'OUTDOORS'),
    enc('meteor', 'QUEST'),
    enc('something eating the farm animals', 'QUEST'),
    enc('precious cargo', 'QUEST'),
    enc('the town elder', 'QUEST_GIVER'),
    enc('children abducted for blood ritual', 'QUEST'),
    enc('the underdark', 'EXPLORATION'),
    enc('a teleportation circle', 'EXPLORATION'),
]
