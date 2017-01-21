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
		self.challenge_rating=2
