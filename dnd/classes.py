import base

class Standard:
	def __init__(self, level):
		self.proficiency_bonus=2+(level-1)//2
		self.level=level

	def first_level_hp(self):
		return parse_roll_request(self.hit_dice)[1]+base.modifier(self.constitution)

	def level_up(self, roll=False):
		sides=parse_roll_request(self.hit_dice)[1]
		if roll: x=sides
		else: x=sides//2+1
		self.max_hp+=x+base.modifier(self.constitution)

class SpellCaster(Standard):
	def __init__(self, level):
		Standard.__init__(self, level)
		self.slots=[
			[2, 0, 0, 0, 0, 0, 0, 0, 0],
			[3, 0, 0, 0, 0, 0, 0, 0, 0],
			[4, 2, 0, 0, 0, 0, 0, 0, 0],
			[4, 3, 0, 0, 0, 0, 0, 0, 0],
			[4, 3, 2, 0, 0, 0, 0, 0, 0],
			[4, 3, 3, 0, 0, 0, 0, 0, 0],
			[4, 3, 3, 1, 0, 0, 0, 0, 0],
			[4, 3, 3, 2, 0, 0, 0, 0, 0],
			[4, 3, 3, 3, 1, 0, 0, 0, 0],
			[4, 3, 3, 3, 2, 0, 0, 0, 0],
			[4, 3, 3, 3, 2, 1, 0, 0, 0],
			[4, 3, 3, 3, 2, 1, 0, 0, 0],
			[4, 3, 3, 3, 2, 1, 1, 0, 0],
			[4, 3, 3, 3, 2, 1, 1, 0, 0],
			[4, 3, 3, 3, 2, 1, 1, 1, 0],
			[4, 3, 3, 3, 2, 1, 1, 1, 0],
			[4, 3, 3, 3, 2, 1, 1, 1, 1],
			[4, 3, 3, 3, 3, 1, 1, 1, 1],
			[4, 3, 3, 3, 3, 2, 1, 1, 1],
			[4, 3, 3, 3, 3, 2, 1, 1, 1],
		][level]

	def spell_save_difficulty_class(self):
		return 8+self.proficiency_bonus+base.modifier(self.spellcasting_ability())

	def spell_attack_bonus(self):
		return self.proficiency_bonus+base.modifier(self.spellcasting_ability())

	def prepared_spells(self):
		return max(base.modifier(self.spellcasting_ability())+self.level, 1)

class Cleric(SpellCaster):
	def __init__(self, level):
		SpellCaster.__init__(self, level)
		self.hit_dice='{}d8'.format(level)
		self.proficiencies+=[
			'light_armor', 'medium_armor', 'shields',
			'simple_weapons',
			'wisdom_saving_throw', 'charisma_saving_throw',
		]
		self.spells=[
			[],
			['burning_hands', 'faerie_fire', 'bane', 'bless', 'cure_wounds', 'guiding_bolt', 'healing_word', 'protection_from_evil_and_good', 'sanctuary', 'shield_of_faith'],
		]

	def spellcasting_ability(self): return self.wisdom

class Wizard(SpellCaster):
	def __init__(self, level):
		SpellCaster.__init__(self, level)
		self.hit_dice='{}d6'.format(level)
		self.proficiencies+=[
			'daggers', 'darts', 'slings', 'quarterstaffs', 'light crossbows',
			'wisdom_saving_throw', 'intelligence_saving_throw',
		]

	def spellcasting_ability(self): return self.intelligence

class Rogue(Standard):
	def __init__(self, level):
		Standard.__init__(self, level)
		self.hit_dice='{}d8'.format(level)
		self.proficiencies+=[
			'light_armor',
			'simple_weapons', 'hand_crossbows', 'longswords', 'rapiers', 'shortswords',
			'thieves_tools',
			'dexterity_saving_throw', 'intelligence_saving_throw',
		]

	def sneak_attack(self): return '{}d6'.format((self.level-1)//2)

class Fighter(Standard):
	def __init__(self, level):
		Standard.__init__(self, level)
		self.hit_dice='{}d10'.format(level)
		self.proficiencies=[
			'all_armor', 'shields',
			'simple_weapons', 'martial_weapons',
			'strength_saving_throw', 'constitution_saving_throw',
		]
		features=[
			['fighting_style', 'second_wind'],
			['action_surge'],
			['martial_archetype'],
			['ability_score_improvement'],
			['extra_attack'],
			['ability_score_improvement'],
			['martial_archetype_feature'],
			['ability_score_improvement'],
			['indomitable'],
			['martial_archetype_feature'],
			['extra_attack'],
			['ability_score_improvement'],
			['indomitable'],
			['ability_score_improvement'],
			['martial_archetype_feature'],
			['ability_score_improvement'],
			['action_surge', 'indomitable'],
			['martial_archetype_feature'],
			['ability_score_improvement'],
			['extra_attack'],
		]
		import collections
		self.features=collections.defaultdict(int)
		for i in range(0, level):
			for j in features[i]:
				self.features[j]+=1
