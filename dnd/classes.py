import base

def add(object, member, value, method=lambda old, new: old):
	if hasattr(object, member): value=method(getattr(object, member), value)
	setattr(object, member, value)

def union(x, y): return x+[i for i in y if i not in x]
def plus(x, y): return x+y
def plus_string(x, y): return x+'+'+y

class Progression:
	def __init__(self, list, level):
		import collections
		self.x=collections.defaultdict(int)
		for i in range(0, level):
			for j in list[i]: self.x[j]+=1

	def __repr__(self): return repr(dict(self.x))

	def __add__(self, other):
		result=Progression([], 0)
		result.x=self.x
		for k, v in other.x.items(): result.x[k]+=v
		return result

class Standard:
	def __init__(self, level):
		add(self, 'level', level, plus)
		add(self, 'proficiency_bonus', 2+(level-1)//4, plus)

	def first_level_hp(self):
		return parse_roll_request(self.hit_dice)[1]+base.modifier(self.constitution)

	def level_up(self, roll=False):
		sides=parse_roll_request(self.hit_dice)[1]
		if roll: x=sides
		else: x=sides//2+1
		self.max_hp+=x+base.modifier(self.constitution)

class Spellcaster(Standard):
	def __init__(self, level):
		Standard.__init__(self, level)
		add(self, 'slots', [
			[0, 0, 0, 0, 0, 0, 0, 0, 0],
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
		][level], lambda old, new: [old[i]+new[i] for i in range(9)])

	def spell_save_difficulty_class(self):
		return 8+self.proficiency_bonus+base.modifier(self.spellcasting_ability())

	def spell_attack_bonus(self):
		return self.proficiency_bonus+base.modifier(self.spellcasting_ability())

	def prepared_spells(self):
		return max(base.modifier(self.spellcasting_ability())+self.level, 1)

class Cleric(Spellcaster):
	def __init__(self, level):
		Spellcaster.__init__(self, level)
		add(self, 'hit_dice', '{}d8'.format(level), plus_string)
		add(self, 'proficiencies', [
			'light_armor', 'medium_armor', 'shields',
			'simple_weapons',
			'wisdom_saving_throw', 'charisma_saving_throw',
		], union)
		add(self, 'features', Progression([
			['spellcasting', 'divine_domain'],
			['channel_divinity', 'divine_domain'],
			[],
			['ability_score_improvement'],
			['destroy_undead'],
			['channel_divinity', 'divine_domain'],
			[],
			['ability_score_improvement', 'destroy_undead', 'divine_domain'],
			[],
			['divine_intervention'],
			['destroy_undead'],
			['ability_score_improvement'],
			[],
			['destroy_undead'],
			[],
			['ability_score_improvement'],
			['destroy_undead', 'divine_domain'],
			['channel_divinity'],
			['ability_score_improvement'],
			['divine_intervention_improvement'],
		], level), plus)
		add(self, 'spells', [
			[],
			['burning_hands', 'faerie_fire', 'bane', 'bless', 'cure_wounds', 'guiding_bolt', 'healing_word', 'protection_from_evil_and_good', 'sanctuary', 'shield_of_faith'],
		], lambda old, new: [union(old[i], new[i]) for i in range(9)])

	def spellcasting_ability(self): return self.wisdom

class Wizard(Spellcaster):
	def __init__(self, level):
		Spellcaster.__init__(self, level)
		add(self, 'hit_dice', '{}d6'.format(level), plus_string)
		add(self, 'proficiencies', [
			'daggers', 'darts', 'slings', 'quarterstaffs', 'light crossbows',
			'wisdom_saving_throw', 'intelligence_saving_throw',
		], union)
		add(self, 'features', Progression([
			['spellcasting', 'arcane_recovery'],
			['arcane_tradition'],
			[],
			['ability_score_improvement'],
			[],
			['arcane_tradition'],
			[],
			['ability_score_improvement'],
			[],
			['arcane_tradition'],
			[],
			['ability_score_improvement'],
			[],
			['arcane_tradition'],
			[],
			['ability_score_improvement'],
			[],
			['spell_mastery'],
			['ability_score_improvement'],
			['signature_spell'],
		], level), plus)

	def spellcasting_ability(self): return self.intelligence

class Rogue(Standard):
	def __init__(self, level):
		Standard.__init__(self, level)
		add(self, 'hit_dice', '{}d8'.format(level), plus_string)
		add(self, 'proficiencies', [
			'light_armor',
			'simple_weapons', 'hand_crossbows', 'longswords', 'rapiers', 'shortswords',
			'thieves_tools',
			'dexterity_saving_throw', 'intelligence_saving_throw',
		], union)
		add(self, 'features', Progression([
			['expertise', 'sneak_attack', 'thieves_cant'],
			['cunning_action'],
			['roguish_archetype'],
			['ability_score_improvement'],
			['uncanny_dodge'],
			['expertise'],
			['evasion'],
			['ability_score_improvement'],
			['roguish_archetype'],
			['ability_score_improvement'],
			['reliable_talent'],
			['ability_score_improvement'],
			['roguish_archetype'],
			['blindsense'],
			['slippery_mind'],
			['ability_score_improvement'],
			['roguish_archetype'],
			['elusive'],
			['ability_score_improvement'],
			['stroke_of_luck'],
		], level), plus)

	def sneak_attack(self): return '{}d6'.format((self.level-1)//2)

class Fighter(Standard):
	def __init__(self, level):
		Standard.__init__(self, level)
		add(self, 'hit_dice', '{}d10'.format(level), plus_string)
		add(self, 'proficiencies', [
			'all_armor', 'shields',
			'simple_weapons', 'martial_weapons',
			'strength_saving_throw', 'constitution_saving_throw',
		], union)
		add(self, 'features', Progression([
			['fighting_style', 'second_wind'],
			['action_surge'],
			['martial_archetype'],
			['ability_score_improvement'],
			['extra_attack'],
			['ability_score_improvement'],
			['martial_archetype'],
			['ability_score_improvement'],
			['indomitable'],
			['martial_archetype'],
			['extra_attack'],
			['ability_score_improvement'],
			['indomitable'],
			['ability_score_improvement'],
			['martial_archetype'],
			['ability_score_improvement'],
			['action_surge', 'indomitable'],
			['martial_archetype'],
			['ability_score_improvement'],
			['extra_attack'],
		], level), plus)

class Druid(Spellcaster):
	def __init__(self, level):
		Spellcaster.__init__(self, level)
		add(self, 'hit_dice', '{}d8'.format(level), plus_string)
		add(self, 'proficiencies', [
			'light_armor', 'medium_armor', 'shields',
			'clubs', 'daggers', 'darts', 'javelins', 'maces', 'quarterstaffs',
			'scimitars', 'sickles', 'slings', 'spears',
			'herbalism_kit',
			'intelligence_saving_throw', 'wisdom_saving_throw',
		], union)
		add(self, 'features', Progression([
			['druidic', 'spellcasting'],
			['wild_shape', 'druid_circle'],
			[],
			['wild_shape', 'ability_score_improvement'],
			[],
			['druid_circle'],
			[],
			['wild_shape', 'ability_score_improvement'],
			[],
			['druid_circle'],
			[],
			['ability_score_improvement'],
			[],
			['druid_circle'],
			[],
			['ability_score_improvement'],
			[],
			['timeless_body', 'beast_spells'],
			['ability_score_improvement'],
			['archdruid'],
		], level), plus)

class Bard(Spellcaster):
	def __init__(self, level):
		Spellcaster.__init__(self, level)
		add(self, 'hit_dice', '{}d8'.format(level), plus_string)
		add(self, 'proficiencies', [
			'light_armor',
			'simple_weapons', 'hand_crossbows', 'longswords', 'rapiers', 'shortswords',
			'dexterity_saving_throw', 'charisma_saving_throw',
		], union)
		add(self, 'features', Progression([
			['bardic_inspiration', 'spellcasting'],
			['jack_of_all_trades', 'song_of_rest'],
			['bard_college', 'expertise'],
			['ability_score_improvement'],
			['bardic_inspiration', 'font_of_inspiration'],
			['countercharm', 'bard_college'],
			[],
			['ability_score_improvement'],
			['song_of_rest'],
			['bardic_inspiration', 'expertise', 'magical_secrets'],
			[],
			['ability_score_improvement'],
			['song_of_rest'],
			['magical_secrets', 'bard_college'],
			['bardic_inspiration'],
			['ability_score_improvement'],
			['song_of_rest'],
			['magical_secrets'],
			['ability_score_improvement'],
			['superior_inspiration'],
		], level), plus)

class Sorcerer(Spellcaster):
	def __init__(self, level):
		Spellcaster.__init__(self, level)
		add(self, 'hit_dice', '{}d6'.format(level), plus_string)
		add(self, 'proficiencies', [
			'daggers', 'darts', 'slings', 'quarterstaffs', 'light crossbows',
			'constitution_saving_throw', 'charisma_saving_throw',
		], union)
		add(self, 'features', Progression([
			['sorcerous_origin', 'spellcasting'],
			['font_of_magic'],
			['metamagic'],
			['ability_score_improvement'],
			[],
			['sorcerous_origin'],
			[],
			['ability_score_improvement'],
			[],
			['metamagic'],
			[],
			['ability_score_improvement'],
			[],
			['sorcerous_origin'],
			[],
			['ability_score_improvement'],
			['metamagic'],
			['sorcerous_origin'],
			['ability_score_improvement'],
			['sorcerous_restoration'],
		], level), plus)
