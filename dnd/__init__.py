from .base import *
from . import backgrounds
from . import characters
from . import classes
from . import creatures
from . import items
from . import languages
from . import names
from . import races
from . import skills
from . import special_qualities
from . import spells
from . import test
from . import tools
from . import weave

traveling={
	'slow'  : ['200 ft/min', '2 mi/h', '18 mi/day', 'may stealth'],
	'normal': ['300 ft/min', '3 mi/h', '24 mi/day'],
	'fast'  : ['400 ft/min', '4 mi/h', '30 mi/day', '-5 passive perception'],
}

cover={
	'half' : '+2 to ac and dex saving throws',
	'3/4'  : '+5 to ac and dex saving throws',
	'total': 'cannot be targeted by attacks or spells',
}

donning_and_doffing_armor={
	'light' : {'don': '1 min'   , 'doff': '1 min'},
	'medium': {'don': '5 min'   , 'doff': '1 min'},
	'heavy' : {'don': '10 min'  , 'doff': '5 min'},
	'shield': {'don': '1 action', 'doff': '1 action'},
}

exhaustion=[
	'disadvantage on ability checks',
	'speed halved',
	'disadvantage on attack rolls and saving throws',
	'max hp halved',
	'speed 0',
	'dead',
]

sizes={
	'tiny':       {'space':  2.5, 'examples': ['hawk', 'imp', 'rat', 'sprite']},
	'small':      {'space':  5  , 'examples': ['giant rat', 'goblin', 'kobold', 'gnome']},
	'medium':     {'space':  5  , 'examples': ['gnoll', 'orc', 'werewolf', 'human', 'elf', 'dwarf', 'dragonborn', 'tiefling']},
	'large':      {'space': 10  , 'examples': ['chimera', 'hippogriff', 'ogre', 'dire wolverine']},
	'huge':       {'space': 15  , 'examples': ['cyclops', 'stone giant', 'treant']},
	'gargantuan': {'space': 20  , 'examples': ['ancient dragon', 'kraken']},
}

def fall_damage(height): return '{}d6'.format(height//10)

def roll_encounter(threshold, rolls):
	encounters=0
	for i in range(rolls):
		if roll('d20')>=threshold: encounters+=1
	return encounters

def roll_encounter_dangerous(travel_hours=0, day_rest_hours=0, nights=0, sparse=False):
	return roll_encounter(19 if sparse else 18, int(travel_hours+day_rest_hours*3+nights))

def roll_encounter_uncivilized(days=0.5, sparse=False):
	return roll_encounter(18 if sparse else 17, int(days*2))

def roll_encounter_well_traveled(days=1):
	return roll_encounter(20, int(days))

def roll_encounter_hostile(hours=0.25, sparse=False):
	return roll_encounter(18 if sparse else 17, int(hours*4))

conditions={
	'blinded': "A blinded creature can't see and automatically fails any ability check that requires sight. Attack rolls against the creature have advantage, and the creature's attack rolls have disadvantage.",
	'charmed': "A charmed creature can't attack the charmer or target the charmer with harmful abilities or magical effects. The charmer has advantage on any ability check to interact socially with the creature.",
	'deafened': "A deafened creature can't hear and automatically fails any ability check that requires hearing.",
	'frightened': "A frightened creature has disadvantage on ability checks and attack rolls while the source of its fear is within line of sight. The creature can't willingly move closer to the source of its fear.",
	'grappled': "A grappled creature's speed becomes 0, and it can't benefit from any bonus to its speed. The condition ends if the grappler is incapacitated. The condition also ends if an effect removes the grappled creature from the reach of the grappler or grappling effect, such as when a creature is hurled away by the thunderwave spell.",
	'incapacitated': "An incapacitated creature can't take actions or reactions.",
	'invisible': "An invisible creature is impossible to see without the aid of magic or a special sense. For the purpose of hiding, the creature is heavily obscured. The creature's location can be detected by any noise it makes or any tracks it leaves. Attack rolls against the creature have disadvantage, and the creature's attack rolls have advantage.",
	'paralyzed': "A paralyzed creature is incapacitated (see the condition) and can't move or speak. The creature automatically fails Strength and Dexterity saving throws. Attack rolls against the creature have advantage. Any attack that hits the creature is a critical hit if the attacker is within 5 feet of the creature.",
	'petrified': "A petrified creature is transformed, along with any nonmagical object it is wearing or carrying, into a solid inanimate substance (usually stone). Its weight increases by a factor of ten, and it ceases aging. The creature is incapacitated (see the condition), can't move or speak, and is unaware of its surroundings. Attack rolls against the creature have advantage. The creature automatically fails Strength and Dexterity saving throws. The creature has resistance to all damage. The creature is immune to poison and disease, although a poison or disease already in its system is suspended, not neutralized.",
	'poisoned': "A poisoned creature has disadvantage on attack rolls and ability checks.",
	'prone': "A prone creature's only movement option is to crawl, unless it stands up and thereby ends the condition. The creature has disadvantage on attack rolls. An attack roll against the creature has advantage if the attacker is within 5 feet of the creature. Otherwise, the attack roll has disadvantage.",
	'restrained': "A restrained creature's speed becomes 0, and it can't benefit from any bonus to its speed. Attack rolls against the creature have advantage, and the creature's attack rolls have disadvantage. The creature has disadvantage on Dexterity saving throws.",
	'stunned': "A stunned creature is incapacitated (see the condition), can't move, and can speak only falteringly. The creature automatically fails Strength and Dexterity saving throws. Attack rolls against the creature have advantage.",
	'unconscious': "An unconscious creature is incapacitated (see the condition), can't move or speak, and is unaware of its surroundings. The creature drops whatever it's holding and falls prone. The creature automatically fails Strength and Dexterity saving throws. Attack rolls against the creature have advantage. Any attack that hits the creature is a critical hit if the attacker is within 5 feet of the creature.",
}

combat_free_interaction_examples=[
	'draw or sheathe a sword',
	'open or close a door',
	'withdraw a potion from your backpack',
	'pick up a dropped axe',
	'take a bauble from a table',
	'remove a ring from your finger',
	'stuff some food into your mouth',
	'plant a banner in the ground',
	'fish a few coins from your belt pouch',
	'drink all the ale in a flagon',
	'throw a lever or a switch',
	'pull a torch from a sconce',
	'take a book from a shelf you can reach',
	'extinguish a small flame',
	'don a mask',
	'pull the hood of your cloak up and over your head',
	'put your ear to a door',
	'kick a small stone',
	'turn a key in a lock',
	'tap the floor with a 10-foot pole',
	'hand an item to another character',
]

combat_actions={
	'attack': None,
	'cast a spell': None,
	'dash': 'double speed',
	'disengage': "your movement doesn't provoke opportunity attacks for the rest of the turn.",
	'dodge': "Until the start of your next turn, any attack roll made against you has disadvantage if you can see the attacker, and you make Dexterity saving throws with advantage. You lose this benefit if you are incapacitated or if your speed drops to 0.",
	'help': "When you take the Help action, the creature you aid gains advantage on the next ability check it makes to perform the task you are helping with, provided that it makes the check before the start of your next turn. Alternatively, you can aid a friendly creature in attacking a creature within 5 feet of you. You feint, distract the target, or in some other way team up to make your ally's attack more effective. If your ally attacks the target before your next turn, the first attack roll is made with advantage.",
	'hide': 'DM will ask for a stealth check.',
	'ready': '''Sometimes you want to get the jump on a foe or wait for a particular circumstance before you act. To do so, you can take the Ready action on your turn, which lets you act using your reaction before the start of your next turn. First, you decide what perceivable circumstance will trigger your reaction. Then, you choose the action you will take in response to that trigger, or you choose to move up to your speed in response to it. Examples include "If the cultist steps on the trapdoor, I'll pull the lever that opens it," and "If the goblin steps next to me, I move away." When the trigger occurs, you can either take your reaction right after the trigger finishes or ignore the trigger. Remember that you can take only one reaction per round. When you ready a spell, you cast it as normal but hold its energy, which you release with your reaction when the trigger occurs. To be readied, a spell must have a casting time of 1 action, and holding onto the spell's magic requires concentration. If your concentration is broken, the spell dissipates without taking effect. For example, if you are concentrating on the web spell and ready magic missile, your web spell ends, and if you take damage before you release magic missile with your reaction, your concentration might be broken."''',
	'search': 'DM will ask for a perception or investigation check.',
	'stabilize': 'DC 10 medicine check',
	'use an object': "You normally interact with an object while doing something else, such as when you draw a sword as part of an attack. When an object requires your action for its use, you take the use an object action. This action is also useful when you want to interact with more than one object on your turn.",
}

combat_special_attacks={
	'two-weapon': "When you take the attack action and attack with a light melee weapon that you're holding in one hand, you can use a bonus action to attack with a different light melee weapon that you're holding in the other hand. You don't add your ability modifier to the damage of the bonus attack, unless that modifier is negative. If either weapon has the thrown property, you can throw the weapon, instead of making a melee attack with it.",
	'grapple': "When you want to grab a creature or wrestle with it, you can use the attack action to make a special melee attack, a grapple. If you're able to make multiple attacks with the attack action, this attack replaces one of them. The target of your grapple must be no more than one size larger than you, and it must be within your reach. Using at least one free hand, you try to seize the target by making a grapple check, an athletics check contested by the target's athletics or acrobatics check (the target chooses the ability to use). If you succeed, you subject the target to the grappled condition. The condition specifies the things that end it, and you can release the target whenever you like (no action required). A grappled creature can use its action to escape. To do so, it must succeed on an athletics or acrobatics check contested by your athletics check. When you move, you can drag or carry the grappled creature with you, but your speed is halved, unless the creature is two or more sizes smaller than you.",
	'shove': "Using the Attack action, you can make a special melee attack to shove a creature, either to knock it prone or push it away from you. If you're able to make multiple attacks with the Attack action, this attack replaces one of them. The target of your shove must be no more than one size larger than you, and it must be within your reach. You make an athletics check contested by the starget's athletics or acrobatics check (the target chooses the ability to use). If you win sthe contest, you either knock the target prone or push it 5 feet away from you.",
}

concentration_breaks={
	'concentration': 'casting another spell that requires concentration',
	'damage': "Whenever you take damage while you are concentrating on a spell, you must make a constitution saving throw to maintain your concentration. The DC equals 10 or half the damage you take, whichever number is higher. If you take damage from multiple sources, such as an arrow and a dragon's breath, you make a separate saving throw for each source of damage.",
	'death': "Being incapacitated or killed. You lose concentration on a spell if you are incapacitated or if you die.",
	'environment': "The DM might also decide that certain environmental phenomena, such as a wave crashing over you while you're on a storm-tossed ship, require you to succeed on a DC 10 constitution saving throw to maintain concentration on a spell.",
}

def get_suggestions():
	concepts=[
		#plants
		'apple', 'apricot',
		'bean',
		'corn',
		'daffodil',
		'fungus',
		'lotus', 'lily',
		'mandragora',
		'olive', 'orchid',
		'potato',
		'rose', 'rice',
		'sunflower', 'sugarcane',
		'tree',
		'vine',
		'wheat',
		#animals
		'boar',
		'crab',
		'dragon',
		'eagle', 'elephant',
		'fish', 'frog',
		'goat',
		'horse',
		'lion',
		'monkey',
		'ox',
		'pheasant',
		'rat', 'rabbit', 'raven',
		'serpent', 'scorpion', 'spider',
		'tiger', 'turtle',
		'wolf',
		#colors
		'red', 'orange', 'yellow', 'green', 'blue', 'violet',
		'black', 'white', 'grey',
		#items
		'sword', 'hammer', 'axe', 'staff', 'scepter', 'spade', 'pick',
		'shield', 'helm',
		'gem', 'platinum', 'gold', 'silver', 'copper',
		'leather', 'steel', 'silk', 'fleece',
		'rope', 'paper', 'oil',
		#classes
		'fighter', 'wizard', 'cleric', 'rogue', 'sorcerer', 'warlock',
		'paladin', 'monk', 'barbarian', 'ranger', 'druid', 'bard',
		'alchemist',
		#races
		'human', 'dwarf', 'elf', 'gnome', 'dragonborn', 'tiefling', 'orc',
		'goblin', 'kobold', 'giant', 'angel', 'demon', 'sylph',
		'half',
		#small groups
		'earth', 'water', 'wind', 'fire', 'magic',
		'true', 'false',
		'male', 'female',
		'chaos', 'order',
		'greed', 'love', 'hate',
		'patience', 'judgment',
		'family', 'other',
		'war', 'peace',
		'victory', 'failure',
		'unknown', 'unknowable', 'infinite', 'normal', 'subtle', 'all',
		'tower', 'mine', 'road', 'bridge', 'tunnel',
		'sun', 'star', 'moon',
		'mountain', 'swamp', 'plains', 'forest', 'island', 'snow',
		'strength', 'dexterity', 'constitution',
		'intelligence', 'widsom', 'charisma',
		#misc
		'age',
		'blood', 'bread', 'broken',
		'crown', 'control',
		'death', 'destiny', 'door',
		'experiment',
		'fued', 'fool',
		'growth',
		'machine',
		'pact', 'parasite',
		'secret', 'shelter', 'sure', 'statue', 'sport',
		'trade', 'temporary', 'twin',
		'vessel',
	]
	for i in range(5):
		for j in range(5):
			print(' '*random.randint(1, 8), end='')
			print(random.choice(concepts), end='')
		print()

__all__=[i for i in locals().keys() if not i.startswith('_')]
