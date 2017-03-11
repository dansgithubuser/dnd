import base, classes, names, races, spells

import random, re

class PhaseCentipede(base.Entity):
	'''A phase centipede will phase to an attacker that misses it. They attack by jumping at the target -- if they miss, they end up behind the target.'''
	def __init__(self):
		self.type='vermin'
		self.size='small'
		self.hit_dice='1d8+5'
		self.speed=30
		self.strength=10
		self.dexterity=12
		self.constitution=10
		self.intelligence=5
		self.wisdom=8
		self.charisma=2
		self.special_qualities=['phase']
		self.challenge_rating=1.0/8
		self.natural_armor=2
		self.attacks=[
			('jump and bite', 1, '1d4 PIERCING'),
		]
		self.organization=['1d20']
		self.roll_stats()

class Kobold(base.Entity):
	def __init__(self):
		self.type='kobold'
		self.size='small'
		self.hit_dice='2d6+-2'
		self.alignment=['lawful', 'evil']
		self.proficiencies=['dagger', 'sling']
		self.wearing=['dagger', 'sling']
		self.speed=30
		self.strength=7
		self.dexterity=15
		self.constitution=9
		self.intelligence=8
		self.wisdom=7
		self.charisma=8
		self.special_qualities=['darkvision']
		self.languages=['common', 'draconic']
		self.challenge_rating=1.0/8
		self.roll_stats()

class DireBadger(base.Entity):
	'''These vicious creatures tolerate no intrusions. They cannot burrow into solid rock, but can move through just about any material softer than that. A dire badger usually leaves behind a usable tunnel 5 feet in diameter when burrowing unless the material it's moving through is very loose.

A dire badger is from 5 to 7 feet in length and can weigh up to 500 pounds.'''
	def __init__(self):
		self.type='animal'
		self.size='medium'
		self.hit_dice='3d8+15'
		self.speed=30
		self.natural_armor=3
		self.attacks=[
			('l claw', 1, '1d4 SLASHING', 'finesse'),
			('r claw', 1, '1d4 SLASHING', 'finesse'),
			('bite', -1, '1d6+-1 PIERCING'),
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
		base.Entity.damage(self, amount)

class Witherweed(base.Entity):
	'''Thistle-like plant that grows in mounds.

If burnt, toxic fumes are released.'''
	def __init__(self):
		self.type='plant'
		self.size='tiny'
		self.hit_dice='1d4'
		self.speed=0
		self.attacks=[('frond', 7, '1d4 DEXTERITY+5 POISON')]
		self.spells=[['witherweed_fumes']]
		spells.spells['witherweed_fumes']={
			'damage': '3d12 POISON',
			'save': '13 CONSTITUTION',
			'save_effect': lambda damage: 0,
			'area': ('sphere', 10),
		}
		self.strength=3
		self.dexterity=1
		self.constitution=10
		self.intelligence=1
		self.wisdom=3
		self.charisma=1
		self.environment=['temperate_forest']
		self.roll_stats()
		self.notes={'attack': 'Attacks with 1d4 fronds. Target is stunned if a frond deals 4 dexterity damage. Dexterity resets after a short rest.'}

class ShockerLizard(base.Entity):
	'''Shoulder is 1 foot off the ground. Blue or gray.'''
	def __init__(self):
		self.type='magical beast'
		self.size='small'
		self.hit_dice='2d10+2'
		self.speed=40
		self.natural_armor=3
		self.attacks=[('bite', 1, '1d4 PIERCING')]
		self.spells=[['shocker_lizard_shock']]
		spells.spells['shocker_lizard_shock']={
			'damage': '2d8 LIGHTNING',
			'save': '12 DEXTERITY',
			'save_effect': spells.half,
		}
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
	def __init__(self):
		self.type='beast'
		self.size='medium'
		self.hit_dice='2d8+2'
		self.speed={'land': 30, 'swim': 30}
		self.attacks=[
			('bite', 3, '1d4+4 PIERCING POISONOUS'),
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
		self.notes={'attack': '3d6 poison damage, half on DC 11 constitution saving throw'}

class GiantAntWorker(base.Entity):
	def __init__(self):
		self.type='vermin'
		self.size='medium'
		self.hit_dice='2d8'
		self.speed={'land': 50, 'climb': 20}
		self.natural_armor=7
		self.attacks=[
			('bite', 1, '1d6 PIERCING'),
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

The oozeling can eat through 1-inch-thick, nonmagical metal in 1 round.

Spider Climb. The oozeling can climb difficult surfaces, including upside down on ceilings, without needing to make an ability check.

False Appearance. While the oozeling remains motionless, it is indistinguishable from an oily pool or wet rock.'''
	def __init__(self):
		self.type='ooze'
		self.size='small'
		self.hit_dice='3d4+9'
		self.speed={'land': 20, 'climb': 20}
		self.attacks=[
			('pseudopod', 4, '1d4 BLUDGEONING+1d4 ACID'),
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
		self.notes={
			'attack': 'If the target is wearing nonmagical metal armor, its armor is partly corroded and takes a permanent and cumulative -1 penalty to the AC it offers. The armor is destroyed if the penalty reduces its AC to 10.',
			'damage': 'Any nonmagical weapon made of metal that hits the oozeling corrodes. After dealing damage, the weapon takes a permanent and cumulative -1 penalty to damage rolls. If its penalty drops to -5, the weapon is destroyed. Nonmagical ammunition made of metal that hits the ooze is destroyed after dealing damage.'
		}

class DireWolverine(base.Entity):
	'''Dire wolverines grow to about 12 feet in length and can weigh as much as 2,000 pounds. Dire wolverines attack opponents wantonly, fearing no other creatures.'''
	def __init__(self):
		self.type='animal'
		self.size='large'
		self.hit_dice='5d8+23'
		self.speed={'land': 30, 'climb': 10}
		self.natural_armor=4
		self.attacks=[
			('l claw', 5, '1d6 SLASHING', 'finesse'),
			('r claw', 5, '1d6 SLASHING', 'finesse'),
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
		base.Entity.damage(self, amount)

class Blazehawk(base.Entity):
	'''Blazehawks are red birds that resemble hawks that are enwreathed in flame, and the effects of fire have dampened effect on them. They build nests in high mountains, but rarely attack travellers, sometimes even assisting them in severe cold by starting small fires. Understands primordial language but can't speak it.'''
	def __init__(self):
		self.type='magical beast'
		self.size='small'
		self.hit_dice='4d6'
		self.speed={'land': 10, 'fly': 60}
		self.natural_armor=1
		self.attacks=[
			('beak', 2, '1d4+2 PIERCING+1d8 FIRE', 'finesse'),
			('talons', 2, '2d4+2 SLASHING+1d8 FIRE', 'finesse'),
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
			('greatclub', 6, '3d8 BLUDGEONING'),
			('rock', 6, '4d10 BLUDGEONING'),
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

class TypicalHumanArcher(races.Human):
	def __init__(self, **kwargs):
		stats=sorted([base.roll('3d6') for i in range(6)])
		for i in range(3):
			if base.maybe(): base.swap(stats, base.rn(6), base.rn(6))
		self.charisma, self.wisdom, self.intelligence, self.strength, self.constitution, self.dexterity=stats
		if self.dexterity<12: self.dexterity=12
		self.max_hp=10+base.modifier(self.constitution)
		self.hp=self.max_hp
		races.Human.__init__(self, **kwargs)
		self.name=names.human(self.gender)
		self.proficiencies=['longbow', 'shortbow', 'dagger', 'medium_armor', 'light_armor']
		self.wearing=['leather_armor', 'longbow', 'dagger', 'quiver']
		self.carrying=[]
		if base.maybe(): self.carrying+=[{'gp': base.rn(5)}]
		if base.maybe(): self.carrying+=[{'sp': base.rn(20)}]

class Dretch(base.Entity):
	'''A typical demon for practicing summoners to call forth. They are lazy, untrustworthy, and out to cause a ruckus. Their arms drag on the floor, they have a backward-hunched back, and ears as long as their head.'''
	def __init__(self):
		self.type='fiend'
		self.size='small'
		self.alignment=['chaotic', 'evil']
		self.hit_dice='4d6+4'
		self.speed=20
		self.natural_armor=1
		self.attacks=[
			('bite', 2, '1d6 PIERCING'),
			('claws', 2, '2d4 SLASHING'),
		]
		self.special_qualities=['darkvision']
		self.spells=[['message']]
		self.languages=['abyssal']
		self.damage_immunities=['poison']
		self.condition_immunities=['poison']
		self.resistances=['cold', 'fire', 'lightning']
		self.strength=11
		self.dexterity=11
		self.constitution=12
		self.intelligence=5
		self.wisdom=8
		self.charisma=3
		self.challenge_rating=1.0/4
		self.roll_stats()

class FlyingWeapon(base.Entity):
	def __init__(self, type='dagger'):
		self.type='construct'
		self.size='small'
		self.natural_armor=5
		self.hit_dice='5d6'
		self.speed={'land': 0, 'fly': 50}
		self.strength=12
		self.dexterity=15
		self.constitution=11
		self.intelligence=1
		self.wisdom=5
		self.charisma=1
		self.proficiencies=['dexterity_saving_throw']
		self.special_qualitites=['blindsight']
		self.damage_immunities=['poision', 'psychic']
		self.condition_immunities=[
			'blinded', 'charmed', 'deafened', 'frightened', 'paralyzed',
			'petrified', 'poisoned',
		]
		self.challenge_rating=1.0/4
		self.wearing=[type]
		self.roll_stats()

class Goblin(races.Gendered):
	def __init__(self, **kwargs):
		self.type='goblin'
		self.size='small'
		self.alignment=['neutral', 'evil']
		self.hit_dice='2d6'
		self.speed=30
		self.strength=8
		self.dexterity=14
		self.constitution=10
		self.intelligence=10
		self.wisdom=8
		self.charisma=8
		races.Gendered.__init__(self, **kwargs)
		self.special_qualitites=['darkvision']
		self.proficiencies=['stealth', 'shortbow', 'scimitar']
		self.expertise=['stealth']
		self.languages=['common', 'goblin']
		self.challenge_rating=1.0/4
		self.wearing=['leather_armor', 'shield', 'scimitar']
		self.carrying=['shortbow']
		self.name=names.goblin()
		self.roll_stats()

class Skeleton(races.Human,
	classes.Fighter, classes.Rogue, classes.Ranger, classes.Barbarian,
	classes.Wizard, classes.Druid, classes.Monk, classes.Sorcerer,
	classes.Warlock
):
	def __init__(self, level=1):
		stats=base.random_typical_stats().items()
		for stat, score in stats: setattr(self, stat, score)
		potential_classes={
			'strength':     ['Fighter'],
			'dexterity':    ['Rogue'],
			'constitution': ['Ranger', 'Barbarian'],
			'intelligence': ['Wizard'],
			'wisdom':       ['Druid', 'Monk'],
			'charisma':     ['Sorcerer', 'Warlock'],
		}[sorted(stats, key=lambda x: x[1])[0][0]]
		c=getattr(classes, base.pick(potential_classes))
		races.Human.__init__(self)
		c.__init__(self, level, new=True)
		for name, options in self.choices.items():
			n=1
			m=re.match(r'(\d+)', name)
			if m: n=int(m.group(1))
			if re.search('skill|weapon|armor', name):
				picked=base.flatten(base.pick_n(options, n))
				base.add(self, 'proficiencies', picked, base.union)
				base.add(self, 'wearing', base.pick_n(picked, 1), base.union)
			elif 'cantrip' in name:
				base.add(self, 'spells', options, base.union)
		self.type='undead'
		self.natural_armor=1
		self.condition_immunities=['exhaustion', 'poison']
		self.damage_immunities=['poison']
		self.vulnerabilities=['bludgeoning']
		self.roll_stats()
