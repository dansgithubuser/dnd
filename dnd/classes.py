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

class SpellPreparer(Spellcaster):
	def prepared_spells(self):
		return max(base.modifier(self.spellcasting_ability())+self.level, 1)

class Cleric(SpellPreparer):
	def __init__(self, level):
		SpellPreparer.__init__(self, level)
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
			['bane', 'bless', 'command', 'create_or_destroy_water', 'cure_wounds', 'detect_evil_and_good', 'detect_magic', 'detect_poison_and_disease', 'guiding_bolt', 'healing_word', 'inflict_wounds', 'protection_from_evil_and_good', 'purify_food_and_drink', 'sanctuary', 'shield_of_faith'],
			['aid', 'augury', 'blindness_deafness', 'calm_emotions', 'continual_flame', 'enhance_ability', 'find_traps', 'gentle_repose', 'hold_person', 'lesser_restoration', 'locate_object', 'prayer_of_healing', 'protection_from_poison', 'silence', 'spiritual_weapon', 'warding_bond', 'zone_of_truth'],
			['animate_dead', 'beacon_of_hope', 'bestow_curse', 'clairvoyance', 'create_food_and_water', 'daylight', 'dispel_magic', 'glyph_of_warding', 'magic_circle', 'mass_healing_word', 'meld_into_stone', 'protection_from_energy', 'remove_curse', 'revivify', 'sending', 'speak_with_dead', 'spirit_guardians', 'tongues', 'water_walk'],
			['banishment', 'control_water', 'death_ward', 'divination', 'freedom_of_movement', 'guardian_of_faith', 'locate_creature', 'stone_shape'],
			['commune', 'contagion', 'dispel_evil_and_good', 'flame_strike', 'geas', 'greater_restoration', 'hallow', 'insect_plague', 'legend_lore', 'mass_cure_wounds', 'planar_binding', 'raise_dead', 'scrying'],
			['blade_barrier', 'create_undead', 'find_the_path', 'forbiddance', 'harm', 'heal', 'heroes_feast', 'planar_ally', 'true_seeing', 'word_of_recall'],
			['conjure_celestial', 'divine_word', 'etherealness', 'fire_storm', 'plane_shift', 'regenerate', 'resurrection', 'symbol'],
			['antimagic_field', 'control_weather', 'earthquake', 'holy_aura'],
			['astral_projection', 'gate', 'mass_heal', 'true_resurrection'],
		], lambda old, new: [union(old[i], new[i]) for i in range(9)])

	def spellcasting_ability(self): return self.wisdom

class Wizard(SpellPreparer):
	def __init__(self, level):
		SpellPreparer.__init__(self, level)
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

class Druid(SpellPreparer):
	def __init__(self, level):
		SpellPreparer.__init__(self, level)
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

	def spellcasting_ability(self): return self.wisdom

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

	def spellcasting_ability(self): return self.charisma

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

	def spellcasting_ability(self): return self.charisma

class Ranger(Spellcaster):
	def __init__(self, level):
		Spellcaster.__init__(self, level)
		add(self, 'hit_dice', '{}d10'.format(level), plus_string)
		add(self, 'proficiencies', [
			'light_armor', 'medium_armor', 'shields',
			'simple_weapons', 'martial_weapons',
			'dexterity_saving_throw', 'strength_saving_throw',
		], union)
		add(self, 'features', Progression([
			['favored_enemy', 'natural_explorer'],
			['spellcasting', 'fighting_style'],
			['ranger_archetype', 'primeval_awareness'],
			['ability_score_improvement'],
			['extra_attack'],
			['favored_enemy', 'natural_explorer'],
			['ranger_archetype'],
			['ability_score_improvement', 'lands_stride'],
			[],
			['natural_explorer', 'hide_in_plain_sight'],
			['ranger_archetype'],
			['ability_score_improvement'],
			[''],
			['favored_enemy', 'vanish'],
			['ranger_archetype'],
			['ability_score_improvement'],
			[],
			['feral_senses'],
			['ability_score_improvement'],
			['foe_slayer'],
		], level), plus)

	def spellcasting_ability(self): return self.wisdom
