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
    'ITEM',
    'POWERFUL_ALLY',
    'SOMETHINGS_UP',
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
    enc('sylph', 'OUTDOORS POWERFUL_ALLY'),
    enc('meteor', 'QUEST'),
    enc('something eating the farm animals', 'QUEST'),
    enc('precious cargo', 'QUEST'),
    enc('the town elder', 'QUEST_GIVER'),
    enc('children abducted for blood ritual', 'QUEST'),
    enc('the underdark', 'EXPLORATION'),
    enc('a teleportation circle', 'EXPLORATION'),
    enc('a slumbering elder dragon', 'POWERFUL_ALLY'),
    enc('an intelligent wand', 'ITEM'),
    enc('a dragon egg', 'ITEM'),
    enc('a magical monocle wth an agenda', 'ITEM'),
    enc('intelligent fungus', 'POWERFUL_ALLY'),
    enc('a zone of disablement', 'SOMETHINGS_UP'),
    enc('children on the run', 'QUEST'),
    enc('the lady in glowing armor', 'POWERFUL_ALLY'),
    enc('famine', 'TOWN QUEST'),
    enc('a map to a legendary treasure', 'QUEST'),
    enc('a legendary vessel of magical power', 'ITEM'),
    enc('a coalescence of magic', 'ITEM'),
    enc('a lich', 'BIG_BAD'),
    enc('humanoid wolves infested by magic wasps', 'COMBAT OUTDOORS'),
    enc('billdads (beaver with kangaroo legs and hawk beak)', 'COMBAT OUTDOORS'),
    enc('nogtails (pig with long legs)', 'COMBAT OUTDOORS'),
    enc('erklings (rabbitty humanoid)', 'COMBAT OUTDOORS'),
    enc('big teleporting spiders', 'COMBAT OUTDOORS'),
    enc('witherweed', 'OUTDOORS'),
    enc('aerial facehugging manta ray', 'COMBAT OUTDOORS'),
    enc('a phoenix', 'POWERFUL_ALLY'),
    enc('an evil shapeshifting tree', 'BIG_BAD'),
    enc('a weapon of perfect death (one use)', 'ITEM'),
    enc('a potion of water-breathing', 'ITEM'),
    enc('eyes leering up from the pit latrine', 'QUEST'),
    enc('gabbering ghost', 'QUEST'),
    enc('flying broomstick', 'ITEM'),
    enc('invisibility cloak', 'ITEM'),
    enc('mana steal weapon', 'ITEM'),
    enc('mana burn weapon', 'ITEM'),
    enc('a weapon of perfect petrification', 'ITEM'),
    enc('arrow of multiplication', 'ITEM'),
]
