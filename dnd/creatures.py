import base

class DireBadger(base.Entity):
	'''These vicious creatures tolerate no intrusions. They cannot burrow into solid rock, but can move through just about any material softer than that. A dire badger usually leaves behind a usable tunnel 5 feet in diameter when burrowing unless the material it's moving through is very loose.

A dire badger is from 5 to 7 feet in length and can weigh up to 500 pounds.

A dire badger that takes damage in combat flies into a berserk rage on its next turn, clawing and biting madly until either it or its opponent is dead. It gains +4 Strength, +4 Constitution, and -2 AC. The creature cannot end its rage voluntarily.

A dire badger can use a full turn to attack with both claws and bite.'''
	def __init__(self):
		self.type='animal'
		self.size='medium'
		self.hit_dice='3d8+15'
		self.speed=30
		self.natural_armor=3
		self.attacks=[
			('l claw', 4, '1d4+2'),
			('r claw', 4, '1d4+2'),
			('bite', -1, '1d6+1'),
		]
		self.special_qualities=['darkvision', 'keen_smell']
		self.strength=14
		self.dexterity=17
		self.constitution=19
		self.intelligence=2
		self.wisdom=12
		self.charisma=10
		self.proficiencies=['perception']
		self.environment=['temperate_forest']
		self.organization=['1', '1d4+1']
		self.challenge_rating=2
		self.raged=False
		self.roll_stats()

	def damage(self, amount):
		if not self.raged:
			self.raged=True
			self.strength+=4
			self.constitution+=4
			self.natural_armor-=2
			print('raged')
		Entity.damage(self, amount)

class Witherweed(base.Entity):
	'''Thistle-like plant that grows in mounds.

Attacks with 1d4 fronds. Each hit reduces dexterity by 1d4. Target is stunned on a 4. Dexterity resets after a short rest.

If burnt, toxic fumes are released. DC 13 constitution check or 3d12 poision damage.'''
	def __init__(self):
		self.type='plant'
		self.hit_dice='1d4'
		self.speed=0
		self.attacks=[
			('frond', 2, '1'),
		]
		self.strength=3
		self.dexterity=1
		self.constitution=10
		self.intelligence=1
		self.wisdom=3
		self.charisma=1
		self.environment=['temperate_forest']
		self.roll_stats()

class ShockerLizard(base.Entity):
	'''A shocker lizard can shock an opponent. 2d8 damage, half if opponent makes a DC 12 dex saving throw.

Shoulder is 1 foot off the ground. Blue or gray.'''
	def __init__(self):
		self.type='magical beast'
		self.size='small'
		self.hit_dice='2d10+2'
		self.speed=40
		self.natural_armor=3
		self.attacks=[
			('bite', 3, '1d4'),
		]
		self.spells=[['shock']]
		self.special_qualities=['darkvision']
		self.strength=10
		self.dexterity=15
		self.constitution=13
		self.intelligence=2
		self.wisdom=12
		self.charisma=6
		self.proficiencies=['athletics', 'stealth', 'perception']
		self.environment=['temperate_forest']
		self.organization=['1', '2', '1d3+2']
		self.challenge_rating=1
		self.roll_stats()

class GiantVenemousSnake(base.Entity):
	'''Actions:

Bite. Melee Weapon Attack: +6 to hit, reach 10 ft., one target. Hit: 1d4+4 piercing damage, and the target must make a DC 11 Constitution saving throw, taking 3d6 poison damage on a failed save, or half as much damage on a successful one.'''
	def __init__(self):
		self.type='beast'
		self.size='medium'
		self.hit_dice='2d8+2'
		self.speed={'land': 30, 'swim': 30}
		self.attacks=[
			('bite', 6, '1d4+4'),
		]
		self.special_qualities={'blindsight': 10}
		self.strength=10
		self.dexterity=18
		self.constitution=13
		self.intelligence=2
		self.wisdom=10
		self.charisma=3
		self.proficiencies=['perception']
		self.challenge_rating=1
		self.roll_stats()

class GiantAntWorker(base.Entity):
	def __init__(self):
		self.type='vermin'
		self.size='medium'
		self.hit_dice='2d8'
		self.speed={'land': 50, 'climb': 20}
		self.natural_armor=7
		self.attacks=[
			('bite', 1, '1d6'),
		]
		self.special_qualities={'darkvision': None}
		self.strength=10
		self.dexterity=10
		self.constitution=10
		self.wisdom=11
		self.charisma=9
		self.proficiencies=['perception', 'constitution_saving_throw']
		self.challenge_rating=1
		self.environment=['temperate_plains']
		self.roll_stats()

class GrayOozeling(base.Entity):
	'''Amorphous. The oozeling can move through a space as narrow as 1 inch wide without squeezing.

Corrode Metal. Any nonmagical weapon made of metal that hits the oozeling corrodes. After dealing damage, the weapon takes a permanent and cumulative -1 penalty to damage rolls. If its penalty drops to -5, the weapon is destroyed. Nonmagical ammunition made of metal that hits the ooze is destroyed after dealing damage.
The oozeling can eat through 1-inch-thick, nonmagical metal in 1 round.

Spider Climb. The oozeling can climb difficult surfaces, including upside down on ceilings, without needing to make an ability check.

False Appearance. While the oozeling remains motionless, it is indistinguishable from an oily pool or wet rock.

Actions:

Pseudopod. Melee Weapon Attack: +3 to hit, reach 5 ft., one creature. Hit: 2 (1d4) bludgeoning damage plus 2 (1d4) acid damage and if the target is wearing nonmagical metal armor, its armor is partly corroded and takes a permanent and cumulative -1 penalty to the AC it offers. The armor is destroyed if the penalty reduces its AC to 10.
'''
	def __init__(self):
		self.type='ooze'
		self.size='small'
		self.hit_dice='3d4+9'
		self.speed={'land': 20, 'climb': 20}
		self.attacks=[
			('pseudopod', 3, '2d4'),
		]
		self.special_qualities={'blindsight': 60}
		self.strength=11
		self.dexterity=8
		self.constitution=16
		self.intelligence=3
		self.wisdom=6
		self.charisma=2
		self.proficiencies=['stealth']
		self.resistances=['acid', 'cold', 'fire']
		self.condition_immunities=['blinded', 'charmed', 'deafened', 'exhaustion', 'frightened', 'prone']
		self.challenge_rating=1
		self.environment=['temperate_plains']
		self.roll_stats()

class DireWolverine(base.Entity):
	'''Dire wolverines grow to about 12 feet in length and can weigh as much as 2,000 pounds. Dire wolverines attack opponents wantonly, fearing no other creatures.

A dire wolverine that takes damage in combat flies into a berserk rage on its next turn, clawing and biting madly until either it or its opponent is dead. An enraged dire wolverine gains +4 Strength, +4 Constitution, and -2 AC. The creature cannot end its rage voluntarily.

A dire badger can use a full turn to attack with both claws.'''
	def __init__(self):
		self.type='animal'
		self.size='large'
		self.hit_dice='5d8+23'
		self.speed={'land': 30, 'climb': 10}
		self.natural_armor=4
		self.attacks=[
			('l claw', 8, '1d6+6'),
			('r claw', 8, '1d6+6'),
		]
		self.special_qualities=['darkvision', 'keen_smell']
		self.strength=22
		self.dexterity=17
		self.constitution=19
		self.intelligence=2
		self.wisdom=12
		self.charisma=10
		self.proficiencies=['climb', 'perception']
		self.proficiency_bonus=7
		self.environment=['cold_forest']
		self.organization=['1d2']
		self.challenge_rating=4
		self.raged=False
		self.roll_stats()

	def damage(self, amount):
		if not self.raged:
			self.raged=True
			self.strength+=4
			self.constitution+=4
			self.natural_armor-=2
			print('raged')
		Entity.damage(self, amount)

class Blazehawk(base.Entity):
	'''Blazehawks are red birds that resemble hawks that are enwreathed in flame, and the effects of fire have dampened effect on them. They build nests in high mountains, but rarely attack travellers, sometimes even assisting them in severe cold by starting small fires. Understands primordial language but can't speak it.
ACTIONS
Beak. Melee Weapon Attack: +3 to hit, reach 5 ft., one target. Hit: 3 (1d4 + 1) piercing damage plus 4 (1d8) fire damage.
Talons. Melee Weapon Attack: +3 to hit, reach 5 ft., one target. Hit: 6 (2d4 + 1) slashing damage plus 4 (1d8) fire damage.
'''
	def __init__(self):
		self.type='magical beast'
		self.size='small'
		self.hit_dice='4d6'
		self.speed={'land': 10, 'fly': 60}
		self.natural_armor=1
		self.attacks=[
			('beak', 3, '1d4+1+1d8'),
			('talons', 3, '2d4+1+1d8'),
		]
		self.special_qualities=['darkvision']
		self.strength=9
		self.dexterity=13
		self.constitution=10
		self.intelligence=5
		self.wisdom=12
		self.charisma=7
		self.proficiencies=['perception']
		self.proficiency_bonus=4
		self.resistances=['fire']
		self.challenge_rating=1
		self.environment=['mountains']
		self.roll_stats()

class StoneGiant(base.Entity):
	'''Stone giants are reclusive, quiet, and peaceful as long as they are left alone. Their granite-gray skin, gaunt features, and black, sunken eyes endow stone giants with a stern countenance. They are private creatures, hiding their lives and art away from the world.

The giant has advantage on Dexterity (Stealth) checks made to hide in rocky terrain.

ACTIONS
Multiattack. The giant makes two greatclub attacks.

Greatclub. Melee Weapon Attack: +9 to hit, reach 5 ft., one target. Hit: 19 (3d8 + 6) bludgeoning damage.

Rock. Ranged Weapon Attack: +9 to hit, range 60/240 ft., one target. Hit: 28 (4d10 + 6) bludgeoning damage. If the target is a creature, it must succeed on a DC 17 Strength saving throw or be knocked prone.

REACTIONS
Rock Catching. If a rock or similar object is hurled at the giant, the giant can, with a successful DC 10 Dexterity saving throw, catch the missile and take no bludgeoning damage from it.
'''
	def __init__(self):
		self.type='giant'
		self.size='huge'
		self.alignment=['neutral', 'neutral']
		self.hit_dice='11d12+55'
		self.speed=40
		self.natural_armor=5
		self.attacks=[
			('greatclub', 9, '3d8+6'),
			('rock', 9, '4d10+6'),
		]
		self.special_qualities=['darkvision']
		self.strength=23
		self.dexterity=15
		self.constitution=20
		self.intelligence=10
		self.wisdom=12
		self.charisma=9
		self.proficiencies=['athletics', 'perception']
		self.proficiency_bonus=3
		self.challenge_rating=7
		self.environment=['mountains']
		self.roll_stats()
