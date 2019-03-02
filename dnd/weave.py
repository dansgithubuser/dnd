'''
This file explores a computational model of The Weave.

As it stands, to use magic, magic users must understand the rules of their class, including the various spells accessible to them.
This presents an interesting challenge and provides a workable analogy to magic.
Further, a DM may decide to allow embellishment of spells, challenged by skill checks.

What we seek here is a better analogy to what magic might be.
A way for a DM to easily put a player in a situation where exploring their flavor of magic is rewarding.

What would a good analogy to magic be?
In general a player feels rewarded when they do something creative and get a reward for it.
Players want to feel clever: to discover something, predict something based on it, and use it to their advantage.

This can be achieved as described above, but it requires a lot of attention from the DM.
In particular, we want to enable the player to research magic without requiring attention from the DM.

The first time a player plays a magic user, this is already solved.
The content available is rich and detailed.
But as the player learns more about the written material, it feels more like being a very small dictionary.
The player knows the DM, the situation, and the spells, and has a limited set of magical actions to take.

A magic user may explore interactions with magic and nonmagic, and this would enable similar gameplay to nonmagic users.
However, most spells are not designed this way.
For example, a firebolt does damage.
It is, in fact, designed to _not_ interact with the world physically in some pursuit of mechanical balance.
While a DM may, again, allow embellishment on the firebolt, it is work.
Further, just in terms of theming, magic users are described as practitioners of the weave.
This make magic sound learnable and practiceable, as it feels when a player learns spells for the first time.
How do we keep this feeling as magic user players learn the relatively static content?

The real-world analogy that comes to mind is cryptography.
A simple mapping might work like this.
The DM generates a secret.
The DM generates some plaintexts, each describing the effects of a spell.
The DM generates ciphertexts for the plaintexts with the secret.
The player is given some plaintexts and ciphertexts -- a spellbook, a message from their patron, feedback from their wand, or however the DM themes it.
If the player wants to cast a spell they know without embellishment, they can just describe it as usual.
If a player wants to embellish a spell, they must offer ciphertext to the DM.
The DM decodes the ciphertext and gets a plaintext, which may be anywhere between exactly what the player intended and complete gibberish.

To be clear, we seek broken cryptography so that the player has any chance of probing at it.

This setup is appealing because a significant amount of content can be created for a player in a short amount of time.
Like in cryptography, the player (adversary) has a harder problem to solve than the DM (user of cryptography).

We seek two other things on top of this computational asymmetry: theming and game-time efficiency.
In terms of theming, we want each player to have a unique problem to solve, but we also want magic users of a given class to have problems that fit with the class.
For example, an evocation wizard might have magic structured around states of matter, while a warlock must descend the fractal of their patron's mind.
For game-time efficiency, we simply want this whole process to not take up much more than it would usually.

How can we create classes of problems with themes?
Similar to the desire to create an experience for the player to explore and express magic, we simply seek a set medium expressive enough for a DM to construct a theme from.
In particular, we can create a set of subproblems that the DM may construct a themed problem out of.

How do we achieve game-time efficiency?
The intent is for the magic user to spend a lot of time learning magic -- not using it at the table.
In particular, the time between the player deciding to express something and the DM knowing the resulting effect is what we seek to reduce.
Spoken language is the quickest way to convey information from one person to another, so we seek spells that can be "named".
From there, we need a way for the DM to transform the name of a spell, using the secret, to plaintext describing the effect.
This can be implemented as a simple web application.
'''

import math
import random

#=====spoken language to ciphertext=====#
#simple mapping from "rune" to number based on secret

#=====ciphertext to plaintext=====#
#each of these transformations consume some ciphertext and produce some plaintext
#the set of transformations used and the possible plaintexts yielded by each transformation is based on the secret

#=====plaintext to spell effect=====#
#here we list features of a spell
#plaintext explicitly describes the features of a spell
#we also create a mapping between a set of spell features and an English description of the spell

elements = [
    'force',
    'fire',
    'lightning',
    'light',
    'thunder',
    'healing',
]

opposites = {
    'force': 'force',
    'fire': 'cold',
    'lightning': 'lightning',
    'light': 'dark',
    'thunder': 'thunder',
    'healing': 'necrotic',
}

transfigurations = [
    'acid',
    'poison',
    'psychic',
    'radiant',
    'wind',
    'water',
    'earth',
]

extras = {
    'force': [
        ('you exert up to 10 pounds of force (any direction) on the target', 0),
        ('target is pushed 10 feet away from you', 0),
        ('target is knocked prone', 1),
        ('floating disk is cast at the target', 1),
        ('jump is cast on the target', 1),
        ('mage armor is cast on the target', 1),
        ('shield is cast on the target', 1),
        ('unseen servant is cast at the target', 1),
        ('enlarge reduce is cast on the target', 2),
        ('knock is cast on the target', 2),
        ('levitate is cast on the target', 2),
        ('spider climb is cast on the target', 2),
        ('blink is cast on the target', 3),
        ('fly is cast on the target', 3),
        ('magic circle is cast on the target', 3),
        ('phantom steed is cast at the target', 3),
        ("a force wall similar to tiny hut is created at the spell's boundary", 3),
        ('arcane hand is cast at the target', 5),
        ('wall of force is cast at the target', 5),
        ('this spell disintegrates as in the disintegration spell', 2),
        ('forcecage is cast on the target', 7),
    ],
    'fire': [
        ('you may light a candle, torch, or campfire within the spell area', 0),
        ('you slightly increase or reduce flames within range', 0),
        ('you may cast continual flame instead', 2),
        ('heat metal is cast on the target', 2),
        ('this spell obscures vision', 1),
    ],
    'lightning': [
        ('target knows which way is magnetic North', 0),
        ('target cannot take reactions for a round', 0),
        ('call lightning is cast on the target', 3),
        ("targets within 5 feet of the spell's area are also affected", 1),
        ('flammable objects are ignited', 1),
        ('this spell chains as in chain lightning', 2),
    ],
    'light': [
        ('light is created within range', 0),
        ('light is created within 20 feet of the target (dim for additional 20)', 0),
        ('you create a small visual illusion at the target', 0),
        ('you create an arbitrarily-shaped light source at the target', 0),
        ('you change the color of nearby light sources', 0),
        ('target is blinded', 1),
        ('disguise self is cast on the target', 1),
        ('target creates light in a 10 foot radius and attacks against it have advantage', 1),
        ('you may cast illusory script on the target', 1),
        ('you may cast silent image on the target', 1),
        ('blur is cast on the target', 2),
        ('target becomes visible if it is invisible', 1),
        ('darkvision is cast on the target', 2),
        ('invisibility is cast on the target', 2),
        ('mirror image is cast on the target', 2),
        ('a shapechanger makes its saving throw with disadvantage', 1),
        ('target can see invisible creatures', 2),
        ('darkness created by an equal or lower level spell overlapping this spell is dispelled', 0),
        ('target is incapacitated and has speed 0', 3),
        ('major image is cast on the target', 3),
        ('greater invisibility is cast on the target', 4),
        ('mislead is cast on the target', 5),
        ('seeming is cast on the target', 4),
        ('programmed illusion is cast at the target', 6),
        ("targets within 5 feet of the spell's area are also affected", 1),
        ('light created by this spell is sunlight', 2),
        ('mirage arcane is cast at the target', 7),
        ('project image is cast at the target', 7),
    ],
    'thunder': [
        ('you are deafened until your next long rest', -1),
        ('sound magically transits between you and the target', 0),
        ("target's voice is up to three times louder", 0),
        ('a sound of your choice originates from the target', 0),
        ('target is pushed 10 feet away from you', 0),
        ('target is deafened', 1),
        ('target gains +5 to stealth checks', 1),
        ('brittle targets have disadvantage on the saving throw', 1),
        ('target is silenced and immune to thunder damage', 2),
    ],
    'healing': [
        ('this spell has no effects on constructs or undead', -1),
        ('mending is cast on the target', 0),
        ('target may add a d4 to a saving throw', 0),
        ('spare the dying is cast on the target', 0),
        ('target may add a d4 to an attack roll or saving throw', 1),
        ('expeditious retreat is cast on the target', 1),
        ('heroism is cast on the target', 1),
        ('longstrider is cast on the target', 1),
        ('sanctuary is cast on the target', 1),
        ('shield of faith is cast on the target', 1),
        ('aid is cast on the target', 2),
        ('enhance ability is cast on the target', 2),
        ('lesser restoration is cast on the target', 2),
        ('warding bond is cast on the target', 2),
        ('target has advantage on wisdom saving throws', 1),
        ('target has advantage on death saving throws', 1),
        ('target regains maximum number of hit points possible from any healing', 1),
        ('haste is cast on the target', 3),
        ('protection from energy is cast on the target', 3),
        ('remove curse is cast on the target', 3),
        ('death ward is cast on the target', 4),
        ('freedom of movement is cast on the target', 4),
        ('private sanctum is cast at the target', 4),
        ('resilient sphere is cast at the target', 4),
        ('antilife shell is cast on the target', 5),
        ('greater restoration is cast on the target', 5),
        ('reincarnate is cast on the target', 5),
        ('forbiddance is cast on the target', 6),
        ('globe of invulnerability is cast on the target', 6),
        ('this spell ends blindness, deafness, and diseases affecting the target', 3),
        ('this spell repairs severed body parts', 4),
        ('holy aura is cast at the target', 8),
        ('mind blank is cast on the target', 8),
    ],
    'cold': [
        ("target's speed is reduced by 10 feet for a round", 0),
        ('ice storm is cast at the target', 4),
        ('this spell freezes water like freezing sphere', 2),
        ('wall of ice is cast at the target', 6),
        ('simulacrum is cast on the target', 7),
    ],
    'dark': [
        ('you are blinded until your next long rest', -1),
        ('darkness is created within range', 2),
        ('darkness is created within 15 feet of the target', 2),
        ('target gains +5 to stealth checks', 1),
    ],
    'necrotic': [
        ("this spell can't reduce a target's hit points below 1", -1),
        ('target cannot heal for a round', 0),
        ('undead target has disadvantage on attack rolls against you for a round', 0),
        ('you gain 1d4+4 temporary hit points for 1 hour', 1),
        ('gentle repose is cast on the target', 2),
        ('ray of enfeeblement is cast on the target', 2),
        ('animate dead is cast on the target', 3),
        ('bestow curse is cast on the target', 3),
        ('revivify is cast on the target', 3),
        ('speak with dead is cast on the target', 3),
        ('you gain half damage dealt', 2),
        ('plants make saving throws with disadvantage and take maximum damage', 1),
        ('contagion is cast on the target', 5),
        ('raise dead is cast on the target', 5),
        ('create undead is cast at the target', 6),
        ('target is frightened of you', 3),
        ('target has disadvantage on attack rolls and ability checks', 3),
        ('target falls unconscious', 3),
        ("target's hit point maximum is affected as in harm", 2),
        ('magic jar is cast on the target', 6),
        ('this spell may raise zombies as finger of death', 3),
        ('resurrection is cast on the target', 7),
        ('clone is cast on the target', 8),
        ('astral projection is cast on the target', 9),
        ('true resurrection is cast on the target', 9),
    ],
    'acid': [
        ('grease is cast on the target', 1),
        ('target takes 2d4 acid damage at the end of its turn', 1),
        ('web is cast on the target', 2),
    ],
    'poison': [
        ('you are poisoned', -1),
        ('you may cast detect poison and disease', 1),
        ('protection from poison is cast on the target', 2),
        ('stinking cloud is cast at the target', 3),
        ('cloudkill is cast at the target', 5),
    ],
    'psychic': [
        ('you may create an instantaneous, harmless sensory effect', 0),
        ('target has disadvantage on its next attack', 0),
        ('animal friendship is cast on the target', 1),
        ('target is charmed', 1),
        ('command is cast on the target', 1),
        ('you understand all spoken language', 1),
        ('hideous laughter is cast on the target', 1),
        ('speak with animals is cast on the target', 1),
        ('animal messenger is cast on the target', 2),
        ('calm emotions is cast on the target', 2),
        ('detect thoughts is cast on the target', 2),
        ('enthrall is cast on the target', 2),
        ('target is paralyzed', 2),
        ('suggestion is cast on the target', 2),
        ('zone of truth is cast on the target', 2),
        ('target is frightened of you', 3),
        ('sending is cast on the target', 3),
        ('compulsion is cast on the target', 4),
        ('confusion is cast on the target', 4),
        ('dominate beast is cast on the target', 4),
        ('hallucinatory terrain is cast at the target', 4),
        ("when this target ends its turn frightened of you, repeat this spell's damage", 1),
        ('dominate person is cast on the target', 5),
        ('dream is cast on the target', 5),
        ('geas is cast on the target', 5),
        ('hold monster is cast on the target', 5),
        ('modify memory is cast on the target', 5),
        ('telekinesis is cast at the target', 5),
        ('telepathic bond is cast on the target', 5),
        ('irresistible dance is cast on the target', 6),
        ('mass suggestion is cast on the target', 6),
        ('target suffers one of the effects of symbol', 7),
        ('antipathy sympathy is cast on the target', 8),
        ('dominate monster is cast on the target', 8),
        ('feeblemind is cast on the target', 8),
        ('target is stunned', 2),
        ('weird is cast on the target', 9),
    ],
    'radiant': [
        ('target may add a d4 to a skill check', 0),
        ('you gain advantage on your next attack against the target', 0),
        ('you understand all written language', 1),
        ('you may cast detect evil and good', 1),
        ('protection from evil and good is cast on the target', 1),
        ('arcanists magic aura is cast on the target', 2),
        ('augury is cast', 2),
        ('find traps is cast', 2),
        ('locate object is cast', 2),
        ('tongues is cast on the target', 3),
        ('you may cast divination', 4),
        ('guardian of faith is cast at the target', 4),
        ('you may cast locate creature', 4),
        ('you may cast commune', 5),
        ('dispel evil and good is cast at the target', 5),
        ('hallow is cast on the target', 5),
        ('you may cast legend lore on the target', 5),
        ('find the path is cast on the target', 6),
        ('true seeing is cast on the target', 6),
        ('word of recall is cast on the target', 6),
        ('target cannot be surprised', 2),
        ('target has advantage on attack rolls', 2),
        ('target has advantage on ability checks', 2),
        ('target has advantage on saving throws', 2),
        ('attacks against target have disadvantage', 2),
    ],
    'wind': [
        ('you learn what the weather will be for the next 24 hours', 0),
        ('target is knocked prone', 3),
        ('you may snuff a candle within range', 0),
        ('feather fall is cast on the target', 1),
        ('gust of wind is cast on the target', 2),
        ('gaseous form is cast on the target', 3),
        ('wind as in wind wall appears at the target', 3),
        ('wind walk is cast on the target', 6),
        ('control weather is cast at the target', 8),
        ('storm of vengeance is cast at the target', 9),
    ],
    'water': [
        ('you may cast create or destroy on the target', 1),
        ('target is knocked prone', 2),
        ('fog cloud is cast on the target', 1),
        ('purify food and drink is cast on the target', 1),
        ('alter self (aquatic adaptation) is cast on the target', 1),
        ('you may cast create food and water on the target', 3),
        ('sleet storm is cast on the target', 3),
        ('water breathing is cast on the target', 3),
        ('water walk is cast on the target', 3),
        ('control water is cast at the target', 4),
    ],
    'earth': [
        ('you are petrified for 10 minutes', -1),
        ('target is knocked prone', 1),
        ('you may make a bud bloom', 0),
        ('you may clean or soil an object no larger than 1 cubic foot', 0),
        ('you cause harmless tremors in the ground', 0),
        ('entangle is cast on the target', 1),
        ('you may cast goodberry', 1),
        ('alter self (natural weapons) is cast on the target', 1),
        ('alter self (change appearance) is cast on the target', 1),
        ('barkskin is cast on the target', 2),
        ('you may cast locate animals or plants', 2),
        ('spike growth is cast on the target', 2),
        ('conjure animals is cast on the target', 3),
        ('meld into stone is cast on the target', 3),
        ('plant growth is cast on the target', 3),
        ('speak with plants is cast on the target', 3),
        ('conjure woodland beings is cast', 4),
        ('giant insect is cast on the target', 4),
        ('polymorth is cast on the target', 4),
        ('stone shape is cast on the target', 4),
        ('stoneskin is cast on the target', 4),
        ('awaken is cast on the target', 5),
        ('commune with nature is cast', 5),
        ('creation is cast at the target', 5),
        ('insect plague is cast at the target', 5),
        ('tree stride is cast', 5),
        ('wall of stone is cast at the target', 5),
        ('blade barrier is cast at the target', 6),
        ('flesh to stone is cast on the target', 6),
        ('heroes feast is cast at the target', 6),
        ('instant summons is cast on the target', 6),
        ('move earth is cast at the target', 6),
        ('transport via plants is cast', 6),
        ('wall of thorns is cast at the target', 6),
        ('reverse gravity is cast on the target', 7),
        ('animal shapes is cast at the target', 8),
        ('earthquake is cast at the target', 8),
        ('shapechange is cast on the target', 9),
        ('true polymorph is cast on the target', 9),
    ],
}

casting_times = [
    ('action', 0),
    ('bonus', 1),
    ('reaction', 1),
    ('long', 0),
]

shapes = [
    'self',
    'touch',
    'line',
    'cone',
    'cylinder',
    'sphere',
    'cube',
]

durations = [
    'instantaneous',
    'round',
    'long',
]

deliveries = [
    'attack',
    'saving throw full',
    'saving throw half',
]

misc = [
    ('you are psychopathic until your next long rest', -2),
    ('you forget your ideals until your next long rest', -2),
    ('you forget your name until your next long rest, or someone tells you', -2),
    ('your hit points drop to 1', -1),
    ('you fall unconscious', -1),
    ('you can only cast this on a target to your left', -1),
    ('this spell is aimed randomly (use a d12)', -1),
    ("this spell's effects are applied to the caster instead of the target", -1),
    ('your strength decreases by 1 until your next long rest', -1),
    ('your dexterity decreases by 1 until your next long rest', -1),
    ('your constitution decreases by 1 until your next long rest', -1),
    ('your intelligence decreases by 1 until your next long rest', -1),
    ('your wisdom decreases by 1 until your next long rest', -1),
    ('your charisma decreases by 1 until your next long rest', -1),
    ('your proficiency bonus decreases by 1 until your next long rest', -1),
    ('your speed decreases by 10 until your next long rest', -1),
    ('you gain a level of exhaustion', -1),
    ('you lose one of your highest remaining spell slots', -1),
    ("this spell uses strength divided in half instead of your spellcasting ability", -1),
    ("this spell uses dexterity divided in half instead of your spellcasting ability", -1),
    ("this spell uses constitution divided in half instead of your spellcasting ability", -1),
    ("this spell uses intelligence instead of your spellcasting ability", -1),
    ("this spell uses wisdom instead of your spellcasting ability", -1),
    ("this spell uses charisma instead of your spellcasting ability", -1),
    ('you lose inspiration', -1),
    ('you lose half your hit dice', -1),
    ('you lose proficiency with melee weapons until your next long rest', -1),
    ('you lose proficiency with ranged weapons until your next long rest', -1),
    ('you lose proficiency with tools until your next long rest', -1),
    ('you are silenced until your next long rest', -1),
    ('you are paralyzed until your next long rest', -1),
    ('you are stunned for 1 round', -1),
    ('an entity within 5 feet of a target can also be affected', 0),
    ('this spell does not have to follow a straight line (cannot be used to increase number of targets)', 0),
    ('this spell can be cast through up to 3 feet of wood, 1 foot of stone, 1 inch of metal, or thin lead', 0),
    ('you may reduce the intensity of this spell', 0),
    ('target gains no benefit from cover for saving throw', 0),
    ('shillelagh is cast on the target', 0),
    ('alarm is cast on the target', 0),
    ('this spell cannot miss', 0),
    ('add 1 to each die roll', 0),
    ('spell may be cast as a ritual', 0),
    ('you may modify directions specified in this spell', 1),
    ('target must subtract a d4 from their next attack roll or saving throw', 1),
    ('you may cast detect magic', 1),
    ("your weapon deals an additional 1d4 of this spell's damage type", 1),
    ('you may cast identify', 1),
    ("you may cast find familiar instead; the familiar must associated with this spell's element", 1),
    ('you may cast arcane lock on the target', 2),
    ("you create a blade similar to flame blade, which has this spell's effect instead of doing 3d6 fire damage", 2),
    ('you may move the affected area up to 30 feet, or rotate it any number of degrees, as a bonus action', 1),
    ('you cast this spell into an object, similar to magic mouth, except the object dispels after an hour', 2),
    ('you cast this spell into an object, similar to magic mouth, except only one object may be affected this way at a time', 2),
    ('you cast this spell into a weapon, letting it act as though the spell was cast on each attack with 1s rolled; the weapon dispels after an hour', 2),
    ('if you choose, target gains +1 to attack and damage rolls', 2),
    ('you may cast misty step', 2),
    ('if you choose, target cannot be tracked except by magical means', 1),
    ('you cast this spell holding a rope (up to 60 feet) and have it act at the other end of the rope', 2),
    ('an extradimensional space, as in rope trick, is created at the target', 2),
    ('you can see into the Ethereal Plane', 2),
    ('you cast this spell into a spectral weapon like spiritual weapon; the weapon acts as though this spell was casted with 1s rolled (20s for saving throws)', 2),
    ('clairvoyance is cast on the target', 3),
    ('counterspell is cast on the target', 3),
    ('dispel magic is cast on the target', 3),
    ('nondetection is cast on the target', 3),
    ('slow is cast on the target', 3),
    ('cast spirit guardians', 3),
    ('arcane eye is cast on the target', 4),
    ('banishment is cast on the target', 4),
    ('black tentacles is cast on the target', 4),
    ("conjure minor elementals of this spell's element", 4),
    ('you may cast dimension door', 4),
    ('fabricate is cast on the target', 4),
    ('faithful hound is cast at the target', 4),
    ('you may instead work this spell like fire shield', 4),
    ('secret chest is cast on the target', 4),
    ("you may cast animate objects on objects associated with this spell's element", 5),
    ("conjure elementals of this spell's element", 5),
    ('contact other plane is cast', 5),
    ('passwall is cast at the target', 5),
    ('planar binding is cast', 5),
    ('scrying is cast', 5),
    ('teleportation circle is cast at the target', 5),
    ('conjure fey is cast at the target', 6),
    ('you may refrain from firing this spell similar to freezing sphere', 2),
    ("you can make this spell's effects permanent by casting it the same way every day for a year", 1),
    ('planar ally is cast', 6),
    ('conjure celestial is cast at the target', 7),
    ('add a damage die every turn this spell is being concentrated on', 1),
    ('divine word is cast on the target', 7),
    ('etherealness is cast on the target', 7),
    ('you may cast magnificent mansion', 7),
    ('planeshift is cast', 7),
    ('prismatic spray is cast on the target', 7),
    ('sequester is cast on the target', 7),
    ('this spell is cast similar to symbol, and does half damage', 6),
    ('teleport is cast at the target', 7),
    ('antimagic field is cast at the target', 8),
    ('you may cast demiplane', 8),
    ('glibness is cast on the target', 8),
    ('maze is cast on the target', 8),
    ("do not roll for damage; if the target's hit points is below the maximum possible damage, the full affect happens, otherwise nothing happens", 2),
    ('gate is cast', 9),
    ('imprisonment is cast on the target', 9),
    ('power word kill is cast on the target', 9),
    ('prismatic wall is cast at the target', 9),
    ('time stop is cast', 9),
    ('wish is cast', 9),
    ("you may redistribute this spell's damage as you choose", 7),
    ('this spell can be cast at a higher level, adding a damage die per level above; if it is a cantrip, add a damage die at your 5th, 11th, and 17th level', 0),
    ('for the duration, your 9th level spell slots can cast spells of any level', 9),
    ('your target may be in a different plane', 9),
    ('you can choose which targets within the area are affected', 1),
    ('targets in multiple shapes are affected multiple times', 3),
]

def select(l, g): return l[next(g) % len(l)]

def clamp(x, lo=None, hi=None):
    if lo is not None: x = max(x, lo)
    if hi is not None: x = min(x, hi)
    return x

def plaintext_to_english(plaintext):
    g = (i for i in plaintext + [0 for i in range(100)])
    spell = []
    #element
    if next(g) % 2:
        element = select(transfigurations, g)
    else:
        element = select(elements, g)
        if next(g) % 2: element = opposites[element]
    spell.append('element: {}'.format(element))
    #damage
    damage_die = select([4, 6, 8, 10, 12], g)
    damage_dice = next(g) % {
        4: 5,
        6: 21,
        8: 11,
        10: 11,
        12: 5,
    }[damage_die]
    if element == 'healing':
        spell.append('target heals {}d{} hit points'.format(damage_dice, damage_die, element))
    else:
        damage_type = {
            'light': 'radiant',
            'dark': 'force',
            'wind': 'bludgeoning',
            'water': 'bludgeoning',
            'earth': 'bludgeoning',
        }.get(element, element)
        spell.append('target takes {}d{} {} damage'.format(damage_dice, damage_die, damage_type))
    #range
    rng = select([
        0, 5, 30, 60, 90, 120, 160, 300, 600,
        5e3, 5e4, 5e5, 5e6, 5e7,
        math.inf
    ], g)
    spell.append('range: {} feet'.format(rng))
    #shape
    shape = select(shapes, g)
    shape_size = 0
    if shape in ['cylinder', 'sphere', 'cube']:
        shape_size = select([
            0, 5, 10, 15, 20, 30, 60, 90, 120, 160, 300, 600,
            5e3, 5e4, 5e5, 5e6, 5e7,
            math.inf
        ], g)
        spell.append('shape: {} foot {}'.format(shape_size, shape))
    else: spell.append('shape: {}'.format(shape))
    if shape == 'cone': shape_size = rng
    #targets
    targets = 1 + next(g) % 10
    if targets > 1:
        spell.append('spell has up to {} targets'.format(targets))
    #duration
    concentration = next(g) % 2
    if concentration: spell.append('spell requires concentration')
    duration = select(durations, g)
    if duration == 'long':
        duration = select([
            1, 10, 60,
            2 * 60,
            3 * 60,
            4 * 60,
            6 * 60,
            8 * 60,
            24 * 60,
            7 * 24 * 60,
            30 * 24 * 60,
            365 * 24 * 60,
        ], g)
        if duration < 60:
            spell.append('duration: {} minutes'.format(duration))
        elif duration < 24 * 60:
            spell.append('duration: {} hours'.format(duration / 60))
        else:
            spell.append('duration: {} days'.format(duration / 60 / 24))
    else: spell.append('duration: {}'.format(duration))
    #casting time
    casting_time = select(casting_times, g)
    if casting_time[0] == 'long':
        casting_time = select([
            1, 10, 60,
            2 * 60,
            3 * 60,
            4 * 60,
            6 * 60,
            8 * 60,
            24 * 60,
        ], g)
        if casting_time < 60:
            spell.append('casting time: {} minutes'.format(casting_time))
        else:
            spell.append('casting time: {} hours'.format(casting_time / 60))
    else: spell.append('casting time: {}'.format(casting_time[0]))
    #delivery
    delivery = select(deliveries, g)
    spell.append(delivery)
    #extras
    n = next(g) % 4
    for i in range(n):
        if next(g) % 2:
            spell.append(select(misc, g))
        else:
            spell.append(select(extras[element], g))
    #level
    value = damage_die * damage_dice
    if type(duration) == int and not concentration: targets *= duration
    dim = 0
    if rng != 0:
        if shape in ['line']: dim = 1
        if shape in ['cone', 'cylinder', 'sphere', 'cube']: dim = 3
    targets *= clamp((rng / 10 + shape_size + 30) / 20, 1, 2 ** 128) ** dim
    value *= targets
    if type(casting_time) == int: value /= casting_time
    value = max(1, value - 10)
    feature_levels = [i[1] for i in spell if type(i) != str and len(i) > 1] + [0]
    feature_level = max(0, (sum(feature_levels) + max(feature_levels)) / 2)
    value += targets * (4 ** feature_level - 1)
    level = int(math.log(value) / math.log(4))
    if element == 'healing': level += 1
    spell.append('this is a level {} spell'.format(level))
    #major defects
    if any([i == -2 for i in feature_levels]):
        spell.append('casting this spell a second time kills the caster')
    #done!
    spell = [i if type(i) == str else i[0] for i in spell]
    return spell

#=====helpers=====#
def describe_spell(plaintext):
    print(plaintext)
    english = plaintext_to_english(plaintext)
    for line in english: print(line)
    print(
'''
"Target" ultimately refers to the entities contained within the spell area.
In the context of multiple targets, it refers to an entity or a shape.
For example, a linear spell with multiple targets creates multiple lines, one per specified target.
A spherical spell with multiple targets creates multiple spheres within range, and targets exist within those spheres.
When another spell is applied on a target, the effects are applied on each entity targeted by the spell.
When another localized spell is applied at a target, its effects are applied at each entity within the spell area.
When another distribued spell is applied at a target, its effects are applied within the spell area.

Spells with longer durations apply their entire effects each round.
When another spell is cast, its effect lasts one round,
so effects do not compound, and last as long as this spell.
'''
    )

def random_spell(plaintext=None):
    if not plaintext: plaintext = [random.randint(0, 256) for i in range(20)]
    return plaintext
