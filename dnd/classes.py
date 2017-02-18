import base, items

def add(object, member, value, method=lambda old, new: old):
	if hasattr(object, member): value=method(getattr(object, member), value)
	setattr(object, member, value)

def union(x, y): return x+[i for i in y if i not in x]
def plus(x, y): return x+y
def plus_string(x, y): return x+'+'+y
def dict_add(x, y): return dict(x, **y)

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
		return dice_sides_type(self.hit_dice)[1]+base.modifier(self.constitution)

	def level_up(self, roll=False):
		sides=dice_sides_type(self.hit_dice)[1]
		if roll: x=roll('d{}'.format(sides))
		else: x=sides//2+1
		self.max_hp+=x+base.modifier(self.constitution)

class Spellcaster(Standard):
	def __init__(self, level, **kwargs):
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
		self.cantrips=3
		if level>=4: self.cantrips+=1
		if level>=10: self.cantrips+=1
		add(self, 'choices', {'cantrips': self.cantrips}, dict_add)

	def spell_save_difficulty_class(self):
		return 8+self.proficiency_bonus+base.modifier(self.spellcasting_ability())

	def spell_attack_bonus(self):
		return self.proficiency_bonus+base.modifier(self.spellcasting_ability())

class SpellPreparer(Spellcaster):
	def prepared_spells(self):
		return max(base.modifier(self.spellcasting_ability())+self.level, 1)

class Cleric(SpellPreparer):
	def __init__(self, level, **kwargs):
		SpellPreparer.__init__(self, level, **kwargs)
		add(self, 'hit_dice', '{}d8'.format(level), plus_string)
		add(self, 'proficiencies', [
			'light_armor', 'medium_armor', 'shield',
			'wisdom_saving_throw', 'charisma_saving_throw',
		]+items.simple_weapons, union)
		add(self, 'special_qualities', ['ritual_casting'], union)
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
		if kwargs.get('new', False):
			add(self, 'choices', {
				'2 cleric skills': ['history', 'insight', 'medicine', 'persuasion', 'religion'],
				'cleric weapon': ['mace', 'warhammer'],
				'cleric armor': ['scale_mail', 'leather_armor', 'chain_mail'],
				'cleric weapon 2': ['light_crossbow']+items.simple_weapons,
				'cleric pack': ['priests_pack', 'explorers_pack'],
				'cleric alternate gp': '5d4*10',
			}, dict_add)
			self.wearing=['shield']

	def spellcasting_ability(self): return self.wisdom

class Wizard(SpellPreparer):
	def __init__(self, level, **kwargs):
		SpellPreparer.__init__(self, level, **kwargs)
		add(self, 'hit_dice', '{}d6'.format(level), plus_string)
		add(self, 'proficiencies', [
			'dagger', 'dart', 'sling', 'quarterstaff', 'light_crossbow',
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
		if kwargs.get('new', False):
			add(self, 'choices', {
				'2 wizard skills': ['arcana', 'history', 'insight', 'investigation', 'medicine', 'religion'],
				'wizard weapon': ['quarterstaff', 'dagger'],
				'wizard junk': ['component_pouch', 'arcane_focus'],
				'wizard pack': ['scholars_pack', 'explorers_pack'],
				'wizard alternate gp': '4d4*10',
			}, dict_add)
			self.carrying=['spellbook']

	def spellcasting_ability(self): return self.intelligence

class Rogue(Standard):
	def __init__(self, level, **kwargs):
		Standard.__init__(self, level)
		add(self, 'hit_dice', '{}d8'.format(level), plus_string)
		add(self, 'proficiencies', [
			'light_armor',
			'hand_crossbow', 'longsword', 'rapier', 'shortsword',
			'thieves_tools',
			'dexterity_saving_throw', 'intelligence_saving_throw',
		]+items.simple_weapons, union)
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
		if kwargs.get('new', False):
			add(self, 'choices', {
				'4 rogue skills': [
					'acrobatics', 'athletics', 'deception', 'insight',
					'intimidation', 'investigation', 'perception', 'performance',
					'persuasion', 'sleight_of_hand', 'stealth',
				],
				'rogue weapon': ['rapier', 'shortsword'],
				'rogue weapon 2': [['shortbow', 'quiver'], 'shortsword'],
				'rogue pack': ['burglars_pack', 'dungeoneers_pack', 'explorers_pack'],
				'rogue alternate gp': '4d4*10',
			}, dict_add)
			self.wearing=['leather_armor', 'dagger', 'dagger']
			self.carrying=['thieves_tools']

	def sneak_attack(self): return '{}d6'.format((self.level-1)//2)

class Fighter(Standard):
	def __init__(self, level, **kwargs):
		Standard.__init__(self, level)
		add(self, 'hit_dice', '{}d10'.format(level), plus_string)
		add(self, 'proficiencies', [
			'light_armor', 'medium_armor', 'heavy_armor', 'shield',
			'strength_saving_throw', 'constitution_saving_throw',
		]+items.simple_weapons+items.martial_weapons, union)
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
		import types
		self.attack=types.MethodType(Fighter.attack, self, Fighter)
		if kwargs.get('new', False):
			add(self, 'choices', {
				'2 fighter skills': [
					'acrobatics', 'athletics', 'animal_handling', 'history',
					'insight', 'intimidation', 'perception', 'survival',
				],
				'fighter armor': ['chain_mail', ['leather_armor', 'longbow', 'quiver']],
				'fighter weapon': items.martial_weapon,
				'fighter shield': ['shield']+items.martial_weapon,
				'fighter weapon 2': [['light_crossbow', 'quiver'], {'handaxe': 2}],
				'fighter pack': ['dungeoneers_pack', 'explorers_pack'],
				'fighter alternate gp': '5d4*10',
			}, dict_add)

	def attack(self, *args, **kwargs):
		critical_hit=20
		if hasattr(self, 'martial_archetype') and self.martial_archetype=='champion' and self.level>=3:
			critical_hit=19
		return base.Entity.attack(self, *args, **kwargs)

class Druid(SpellPreparer):
	def __init__(self, level, **kwargs):
		SpellPreparer.__init__(self, level, **kwargs)
		add(self, 'hit_dice', '{}d8'.format(level), plus_string)
		add(self, 'proficiencies', [
			'light_armor', 'medium_armor', 'shield',
			'club', 'dagger', 'dart', 'javelin', 'mace', 'quarterstaff',
			'scimitar', 'sickle', 'sling', 'spear',
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
		if kwargs.get('new', False):
			add(self, 'choices', {
				'2 druid skills': [
					'arcana', 'animal_handling', 'insight', 'medicine',
					'nature', 'perception', 'religion', 'survival',
				],
				'druid shield': ['shield']+items.simple_weapons,
				'druid weapon': ['scimitar']+items.simple_weapon,
				'druid alternate gp': '2d4*10',
			}, dict_add)
			self.wearing=['leather_armor']
			self.carrying=items.explorers_pack+['druidic_focus']

	def spellcasting_ability(self): return self.wisdom

class Bard(Spellcaster):
	def __init__(self, level, **kwargs):
		Spellcaster.__init__(self, level, **kwargs)
		add(self, 'hit_dice', '{}d8'.format(level), plus_string)
		add(self, 'proficiencies', [
			'light_armor',
			'hand_crossbow', 'longsword', 'rapier', 'shortsword',
			'dexterity_saving_throw', 'charisma_saving_throw',
		]+items.simple_weapons, union)
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
		if kwargs.get('new', False):
			add(self, 'choices', {
				'3 bard skills': 'any',
				'3 bard tools': 'musical instruments',
				'bard weapon': ['rapier', 'longsword']+items.simple_weapons,
				'bard pack': ['diplomats_pack', 'entertainers_pack'],
				'bard instrument': 'musical instrument',
				'bard alternate gp': '5d4*10',
			}, dict_add)
			self.wearing=['leather_armor', 'dagger']

	def spellcasting_ability(self): return self.charisma

class Sorcerer(Spellcaster):
	def __init__(self, level, **kwargs):
		Spellcaster.__init__(self, level, **kwargs)
		add(self, 'hit_dice', '{}d6'.format(level), plus_string)
		add(self, 'proficiencies', [
			'dagger', 'dart', 'sling', 'quarterstaff', 'light_crossbow',
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
		if kwargs.get('new', False):
			add(self, 'choices', {
				'2 sorceror skills': [
					'arcana', 'deception', 'insight', 'intimidation',
					'persuasion', 'religion',
				],
				'sorceror weapon': items.simple_weapons,
				'sorceror pack': ['dungeoneers_pack', 'explorers_pack'],
				'sorceror junk': ['component_pouch', 'arcane_focus'],
				'sorceror alternate gp': '3d4*10',
			}, dict_add)
			self.wearing=['dagger', 'dagger']

	def spellcasting_ability(self): return self.charisma

class Ranger(Spellcaster):
	def __init__(self, level, **kwargs):
		Spellcaster.__init__(self, level, **kwargs)
		add(self, 'hit_dice', '{}d10'.format(level), plus_string)
		add(self, 'proficiencies', [
			'light_armor', 'medium_armor', 'shield',
			'dexterity_saving_throw', 'strength_saving_throw',
		]+items.simple_weapons+items.martial_weapons, union)
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
		if kwargs.get('new', False):
			add(self, 'choices', {
				'3 ranger skills': [
					'animal_handling', 'athletics', 'insight', 'investigation',
					'nature', 'perception', 'stealth', 'survival',
				],
				'ranger armor': ['scale_mail', 'leather_armor'],
				'ranger weapon': items.simple_weapons,
				'ranger weapon 2': items.simple_weapons,
				'ranger pack': ['dungeoneers_pack', 'explorers_pack'],
				'ranger alternate gp': '5d4*10',
			}, dict_add)
			self.wearing=['longbow']
			self.carrying=['quiver']

	def spellcasting_ability(self): return self.wisdom
