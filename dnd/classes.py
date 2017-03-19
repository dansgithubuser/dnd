import base, items

class _Progression:
	def __init__(self, list, level):
		import collections
		self.x=collections.defaultdict(int)
		for i in range(0, level):
			for j in list[i]: self.x[j]+=1

	def __repr__(self): return repr(dict(self.x))

	def __add__(self, other):
		result=_Progression([], 0)
		result.x=self.x
		for k, v in other.x.items(): result.x[k]+=v
		return result

class Standard:
	@staticmethod
	def init(self, level, **kwargs):
		base.add(self, 'level', level, base.plus)
		base.add(self, 'proficiency_bonus', 2+(level-1)//4, base.plus)
		base.set_methods(self, Standard)

	def first_level_hp(self):
		return dice_sides_type(self.hit_dice)[1]+base.modifier(self.constitution)

	def level_up(self, roll=False):
		sides=dice_sides_type(self.hit_dice)[1]
		if roll: x=roll('d{}'.format(sides))
		else: x=sides//2+1
		self.max_hp+=x+base.modifier(self.constitution)

class Spellcaster:
	@staticmethod
	def init(self, level, **kwargs):
		Standard.init(self, level, **kwargs)
		base.add(self, 'slots', [
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
		if kwargs.get('new', False):
			cantrips=3
			if level>=4: cantrips+=1
			if level>=10: cantrips+=1
			base.add(self, 'choices', {'cantrips': cantrips}, base.dict_add)

class SpellPreparer:
	@staticmethod
	def init(self, level, **kwargs):
		Spellcaster.init(self, level, **kwargs)
		base.set_methods(self, SpellPreparer)

	def prepared_spells(self, **kwargs):
		return max(base.modifier(self.spellcasting_ability())+self.level, 1)

class Cleric:
	@staticmethod
	def init(self, level, **kwargs):
		SpellPreparer.init(self, level, **kwargs)
		base.set_methods(self, Cleric)
		base.add(self, 'hit_dice', '{}d8'.format(level), base.plus_string)
		base.add(self, 'proficiencies', [
			'light_armor', 'medium_armor', 'shield',
			'wisdom_saving_throw', 'charisma_saving_throw',
		]+items.simple_weapons, base.union)
		base.add(self, 'special_qualities', ['ritual_casting'], base.union)
		base.add(self, 'features', _Progression([
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
		], level), base.plus)
		base.add(self, 'spells', [
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
		], lambda old, new: [base.union(old[i], new[i]) for i in range(9)])
		if kwargs.get('new', False):
			base.add(self, 'choices', {
				'2 cleric skills': ['history', 'insight', 'medicine', 'persuasion', 'religion'],
				'cleric weapon': ['mace', 'warhammer'],
				'cleric armor': ['scale_mail', 'leather_armor', 'chain_mail'],
				'cleric weapon 2': ['light_crossbow']+items.simple_weapons,
				'cleric pack': ['priests_pack', 'explorers_pack'],
				'cleric alternate gp': '5d4*10',
			}, base.dict_add)
			self.wearing=['shield']

	def spellcasting_ability(self): return self.wisdom

class Wizard:
	@staticmethod
	def init(self, level, **kwargs):
		SpellPreparer.init(self, level, **kwargs)
		base.set_methods(self, Wizard)
		base.add(self, 'hit_dice', '{}d6'.format(level), base.plus_string)
		base.add(self, 'proficiencies', [
			'dagger', 'dart', 'sling', 'quarterstaff', 'light_crossbow',
			'wisdom_saving_throw', 'intelligence_saving_throw',
		], base.union)
		base.add(self, 'features', _Progression([
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
		], level), base.plus)
		if kwargs.get('new', False):
			base.add(self, 'choices', {
				'2 wizard skills': ['arcana', 'history', 'insight', 'investigation', 'medicine', 'religion'],
				'wizard weapon': ['quarterstaff', 'dagger'],
				'wizard junk': ['component_pouch', 'arcane_focus'],
				'wizard pack': ['scholars_pack', 'explorers_pack'],
				'wizard alternate gp': '4d4*10',
			}, base.dict_add)
			self.carrying=['spellbook']

	def spellcasting_ability(self): return self.intelligence

class Rogue:
	@staticmethod
	def init(self, level, **kwargs):
		Standard.init(self, level)
		base.set_methods(self, Rogue)
		base.add(self, 'hit_dice', '{}d8'.format(level), base.plus_string)
		base.add(self, 'proficiencies', [
			'light_armor',
			'hand_crossbow', 'longsword', 'rapier', 'shortsword',
			'thieves_tools',
			'dexterity_saving_throw', 'intelligence_saving_throw',
		]+items.simple_weapons, base.union)
		base.add(self, 'features', _Progression([
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
		], level), base.plus)
		if kwargs.get('new', False):
			base.add(self, 'choices', {
				'4 rogue skills': [
					'acrobatics', 'athletics', 'deception', 'insight',
					'intimidation', 'investigation', 'perception', 'performance',
					'persuasion', 'sleight_of_hand', 'stealth',
				],
				'rogue weapon': ['rapier', 'shortsword'],
				'rogue weapon 2': [['shortbow', 'quiver'], 'shortsword'],
				'rogue pack': ['burglars_pack', 'dungeoneers_pack', 'explorers_pack'],
				'rogue alternate gp': '4d4*10',
			}, base.dict_add)
			self.wearing=['leather_armor', 'dagger', 'dagger']
			self.carrying=['thieves_tools']

	def sneak_attack(self): return '{}d6'.format((self.level-1)//2)

class Fighter:
	@staticmethod
	def init(self, level, **kwargs):
		Standard.init(self, level)
		base.set_methods(self, Fighter)
		base.add(self, 'hit_dice', '{}d10'.format(level), base.plus_string)
		base.add(self, 'proficiencies', [
			'light_armor', 'medium_armor', 'heavy_armor', 'shield',
			'strength_saving_throw', 'constitution_saving_throw',
		]+items.simple_weapons+items.martial_weapons, base.union)
		base.add(self, 'features', _Progression([
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
		], level), base.plus)
		import types
		self.attack=types.MethodType(Fighter.attack, self, Fighter)
		if kwargs.get('new', False):
			base.add(self, 'choices', {
				'2 fighter skills': [
					'acrobatics', 'athletics', 'animal_handling', 'history',
					'insight', 'intimidation', 'perception', 'survival',
				],
				'fighter armor': ['chain_mail', ['leather_armor', 'longbow', 'quiver']],
				'fighter weapon': items.martial_weapons,
				'fighter shield': ['shield']+items.martial_weapons,
				'fighter weapon 2': [['light_crossbow', 'quiver'], {'handaxe': 2}],
				'fighter pack': ['dungeoneers_pack', 'explorers_pack'],
				'fighter alternate gp': '5d4*10',
			}, base.dict_add)

	def attack(self, *args, **kwargs):
		critical_hit=20
		if hasattr(self, 'martial_archetype') and self.martial_archetype=='champion' and self.level>=3:
			critical_hit=19
		return base.Entity.attack(self, *args, **kwargs)

class Druid:
	@staticmethod
	def init(self, level, **kwargs):
		SpellPreparer.init(self, level, **kwargs)
		base.set_methods(self, Druid)
		base.add(self, 'hit_dice', '{}d8'.format(level), base.plus_string)
		base.add(self, 'proficiencies', [
			'light_armor', 'medium_armor', 'shield',
			'club', 'dagger', 'dart', 'javelin', 'mace', 'quarterstaff',
			'scimitar', 'sickle', 'sling', 'spear',
			'herbalism_kit',
			'intelligence_saving_throw', 'wisdom_saving_throw',
		], base.union)
		base.add(self, 'features', _Progression([
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
		], level), base.plus)
		if kwargs.get('new', False):
			base.add(self, 'choices', {
				'2 druid skills': [
					'arcana', 'animal_handling', 'insight', 'medicine',
					'nature', 'perception', 'religion', 'survival',
				],
				'druid shield': ['shield']+items.simple_weapons,
				'druid weapon': ['scimitar']+items.simple_weapons,
				'druid alternate gp': '2d4*10',
			}, base.dict_add)
			self.wearing=['leather_armor']
			self.carrying=items.explorers_pack+['druidic_focus']

	def spellcasting_ability(self): return self.wisdom

class Bard:
	@staticmethod
	def init(self, level, **kwargs):
		Spellcaster.init(self, level, **kwargs)
		base.set_methods(self, Bard)
		base.add(self, 'hit_dice', '{}d8'.format(level), base.plus_string)
		base.add(self, 'proficiencies', [
			'light_armor',
			'hand_crossbow', 'longsword', 'rapier', 'shortsword',
			'dexterity_saving_throw', 'charisma_saving_throw',
		]+items.simple_weapons, base.union)
		base.add(self, 'features', _Progression([
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
		], level), base.plus)
		if kwargs.get('new', False):
			base.add(self, 'choices', {
				'3 bard skills': 'any',
				'3 bard tools': 'musical instruments',
				'bard weapon': ['rapier', 'longsword']+items.simple_weapons,
				'bard pack': ['diplomats_pack', 'entertainers_pack'],
				'bard instrument': 'musical instrument',
				'bard alternate gp': '5d4*10',
			}, base.dict_add)
			self.wearing=['leather_armor', 'dagger']

	def spellcasting_ability(self): return self.charisma

class Sorcerer:
	@staticmethod
	def init(self, level, **kwargs):
		Spellcaster.init(self, level, **kwargs)
		base.set_methods(self, Sorcerer)
		base.add(self, 'hit_dice', '{}d6'.format(level), base.plus_string)
		base.add(self, 'proficiencies', [
			'dagger', 'dart', 'sling', 'quarterstaff', 'light_crossbow',
			'constitution_saving_throw', 'charisma_saving_throw',
		], base.union)
		base.add(self, 'features', _Progression([
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
		], level), base.plus)
		if kwargs.get('new', False):
			base.add(self, 'choices', {
				'2 sorceror skills': [
					'arcana', 'deception', 'insight', 'intimidation',
					'persuasion', 'religion',
				],
				'sorceror weapon': items.simple_weapons,
				'sorceror pack': ['dungeoneers_pack', 'explorers_pack'],
				'sorceror junk': ['component_pouch', 'arcane_focus'],
				'sorceror alternate gp': '3d4*10',
			}, base.dict_add)
			self.wearing=['dagger', 'dagger']

	def spellcasting_ability(self): return self.charisma

class Ranger:
	@staticmethod
	def init(self, level, **kwargs):
		Spellcaster.init(self, level, **kwargs)
		base.set_methods(self, Ranger)
		base.add(self, 'hit_dice', '{}d10'.format(level), base.plus_string)
		base.add(self, 'proficiencies', [
			'light_armor', 'medium_armor', 'shield',
			'dexterity_saving_throw', 'strength_saving_throw',
		]+items.simple_weapons+items.martial_weapons, base.union)
		base.add(self, 'features', _Progression([
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
		], level), base.plus)
		base.add(self, 'slots', [
			[0, 0, 0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0, 0, 0],
			[2, 0, 0, 0, 0, 0, 0, 0, 0],
			[3, 0, 0, 0, 0, 0, 0, 0, 0],
			[3, 0, 0, 0, 0, 0, 0, 0, 0],
			[4, 2, 0, 0, 0, 0, 0, 0, 0],
			[4, 2, 0, 0, 0, 0, 0, 0, 0],
			[4, 3, 0, 0, 0, 0, 0, 0, 0],
			[4, 3, 0, 0, 0, 0, 0, 0, 0],
			[4, 3, 2, 0, 0, 0, 0, 0, 0],
			[4, 3, 2, 0, 0, 0, 0, 0, 0],
			[4, 3, 3, 0, 0, 0, 0, 0, 0],
			[4, 3, 3, 0, 0, 0, 0, 0, 0],
			[4, 3, 3, 1, 0, 0, 0, 0, 0],
			[4, 3, 3, 1, 0, 0, 0, 0, 0],
			[4, 3, 3, 2, 0, 0, 0, 0, 0],
			[4, 3, 3, 2, 0, 0, 0, 0, 0],
			[4, 3, 3, 3, 1, 0, 0, 0, 0],
			[4, 3, 3, 3, 1, 0, 0, 0, 0],
			[4, 3, 3, 3, 2, 0, 0, 0, 0],
			[4, 3, 3, 3, 2, 0, 0, 0, 0],
		][level], lambda old, new: [old[i]+new[i] for i in range(9)])
		if kwargs.get('new', False):
			base.add(self, 'choices', {
				'3 ranger skills': [
					'animal_handling', 'athletics', 'insight', 'investigation',
					'nature', 'perception', 'stealth', 'survival',
				],
				'ranger armor': ['scale_mail', 'leather_armor'],
				'ranger weapon': items.simple_weapons,
				'ranger weapon 2': items.simple_weapons,
				'ranger pack': ['dungeoneers_pack', 'explorers_pack'],
				'ranger alternate gp': '5d4*10',
			}, base.dict_add)
			if level>1: base.add(self, 'choices', {
				'ranger spells': 1+level//2
			}, base.dict_add)
			self.wearing=['longbow']
			self.carrying=['quiver']

	def spellcasting_ability(self): return self.wisdom

class Barbarian:
	@staticmethod
	def init(self, level, **kwargs):
		Standard.init(self, level)
		base.set_methods(self, Barbarian)
		base.add(self, 'hit_dice', '{}d12'.format(level), base.plus_string)
		base.add(self, 'proficiencies', [
			'light_armor', 'medium_armor', 'shield',
			'strength_saving_throw', 'constitution_saving_throw',
		]+items.martial_weapons, base.union)
		base.add(self, 'features', _Progression([
			['rage', 'unarmored_defense'],
			['reckless_attack', 'danger_sense'],
			['primal_path'],
			['ability_score_improvement'],
			['extra_attack', 'fast_movement'],
			['primal_path'],
			['feral_instinct'],
			['ability_score_improvement'],
			['brutal_critical'],
			['primal_path'],
			['relentless'],
			['ability_score_improvement'],
			['brutal_critical'],
			['primal_path'],
			['persistent_rage'],
			['ability_score_improvement'],
			['brutal_critical'],
			['indomitable_might'],
			['ability_score_improvement'],
			['primal_champion'],
		], level), base.plus)
		self.rages=2
		if level>=3: self.rages+=1
		if level>=6: self.rages+=1
		if level>=12: self.rages+=1
		if level>=17: self.rages+=1
		if level>=20: self.rages=float('inf')
		self.rage_damage=2
		if level>=9: self.rage_damage+=1
		if level>=16: self.rage_damage+=1
		if kwargs.get('new', False):
			base.add(self, 'choices', {
				'2 barbarian skills': [
					'animal_handling', 'athletics', 'intimidation', 'nature',
					'perception', 'survival',
				],
				'barbarian weapon': [i for i in items.martial_weapons if 'melee' in items.items[i]['type']],
				'barbarian weapon 2': [{'handaxe': 2}]+items.simple_weapons,
			}, base.dict_add)
			self.carrying=items.explorers_pack+[{'javelins': 4}]

class Monk:
	@staticmethod
	def init(self, level, **kwargs):
		Standard.init(self, level)
		base.set_methods(self, Monk)
		base.add(self, 'hit_dice', '{}d8'.format(level), base.plus_string)
		base.add(self, 'proficiencies', [
			'shortsword',
			'strength_saving_throw', 'dexterity_saving_throw',
		]+items.simple_weapons, base.union)
		base.add(self, 'features', _Progression([
			['martial_arts', 'unarmored_defense'],
			['ki', 'unarmored_movement'],
			['monastic_tradition', 'deflect_missiles'],
			['ability_score_improvement', 'slow_fall'],
			['extra_attack', 'stunning_strike'],
			['ki_empowered_strikes', 'monastic_tradition'],
			['evasion', 'stillness_of_mind'],
			['ability_score_improvement'],
			['unarmored_movement'],
			['purity_of_body'],
			['monastic_tradition'],
			['ability_score_improvement'],
			['tongue_of_sun_and_moon'],
			['diamond_soul'],
			['timeless_body'],
			['ability_score_improvement'],
			['monastic_tradition'],
			['empty_body'],
			['ability_score_improvement'],
			['perfect_self'],
		], level), base.plus)
		self.martial_arts='d4'
		if level>=5: self.martial_arts='d6'
		if level>=11: self.martial_arts='d8'
		if level>=17: self.martial_arts='d10'
		self.ki_points=0
		if level>=2: self.ki_points=level
		self.unarmored_movement=0
		if level>=2: self.unarmored_movement=10
		if level>=6: self.unarmored_movement=15
		if level>=10: self.unarmored_movement=20
		if level>=14: self.unarmored_movement=25
		if level>=18: self.unarmored_movement=30
		if kwargs.get('new', False):
			base.add(self, 'choices', {
				'2 monk skills': [
					'acrobatics', 'athletics', 'history', 'insight', 'religion',
					'stealth',
				],
				'monk tools': "any artisan's tools or musical instrument",
				'monk weapon': ['shortsword']+items.simple_weapons,
				'monk pack': ['dungeoneers_pack', 'explorers_pack'],
				'monk alternate gp': '5d4',
			}, base.dict_add)
			self.carrying=[{'darts': 10}]

class Paladin:
	@staticmethod
	def init(self, level, **kwargs):
		Standard.init(self, level)
		base.set_methods(self, Paladin)
		base.add(self, 'hit_dice', '{}d10'.format(level), base.plus_string)
		base.add(self, 'proficiencies', [
			'light_armor', 'medium_armor', 'heavy_armor', 'shield',
			'wisdom_saving_throw', 'charisma_saving_throw',
		]+items.simple_weapons+items.martial_weapons, base.union)
		base.add(self, 'features', _Progression([
			['divine_sense', 'lay_on_hands'],
			['fighting_style', 'spellcasting', 'divine_smite'],
			['divine_health', 'sacred_oath'],
			['ability_score_improvement'],
			['extra_attack'],
			['aura_of_protection'],
			['sacred_oath'],
			['ability_score_improvement'],
			[],
			['aura_of_courage'],
			['divine_smite'],
			['ability_score_improvement'],
			[],
			['cleansing_touch'],
			['sacred_oath'],
			['ability_score_improvement'],
			[],
			['aura_improvements'],
			['ability_score_improvement'],
			['sacred_oath'],
		], level), base.plus)
		base.add(self, 'slots', [
			[0, 0, 0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0, 0, 0],
			[2, 0, 0, 0, 0, 0, 0, 0, 0],
			[3, 0, 0, 0, 0, 0, 0, 0, 0],
			[3, 0, 0, 0, 0, 0, 0, 0, 0],
			[4, 2, 0, 0, 0, 0, 0, 0, 0],
			[4, 2, 0, 0, 0, 0, 0, 0, 0],
			[4, 3, 0, 0, 0, 0, 0, 0, 0],
			[4, 3, 0, 0, 0, 0, 0, 0, 0],
			[4, 3, 2, 0, 0, 0, 0, 0, 0],
			[4, 3, 2, 0, 0, 0, 0, 0, 0],
			[4, 3, 3, 0, 0, 0, 0, 0, 0],
			[4, 3, 3, 0, 0, 0, 0, 0, 0],
			[4, 3, 3, 1, 0, 0, 0, 0, 0],
			[4, 3, 3, 1, 0, 0, 0, 0, 0],
			[4, 3, 3, 2, 0, 0, 0, 0, 0],
			[4, 3, 3, 2, 0, 0, 0, 0, 0],
			[4, 3, 3, 3, 1, 0, 0, 0, 0],
			[4, 3, 3, 3, 1, 0, 0, 0, 0],
			[4, 3, 3, 3, 2, 0, 0, 0, 0],
			[4, 3, 3, 3, 2, 0, 0, 0, 0],
		][level], lambda old, new: [old[i]+new[i] for i in range(9)])
		if kwargs.get('new', False):
			base.add(self, 'choices', {
				'2 paladin skills': [
					'athletics', 'insight', 'intimidation', 'medicine',
					'persuasion', 'religion',
				],
				'paladin weapon': items.martial_weapons,
				'paladin shield': ['shield']+items.martial_weapons,
				'paladin weapon 2': [{'javelin': 5}]+[i for i in items.simple_weapons if 'melee' in items.items[i]['type']],
				'paladin pack': ['priests_pack', 'explorers_pack'],
				'paladin alternate gp': '5d4',
			}, base.dict_add)
			self.wearing=['chain_mail']
			self.carrying=['holy_symbol']

	def spellcasting_ability(self): return self.charisma

class Warlock:
	@staticmethod
	def init(self, level, **kwargs):
		Standard.init(self, level)
		base.set_methods(self, Warlock)
		base.add(self, 'hit_dice', '{}d8'.format(level), base.plus_string)
		base.add(self, 'proficiencies', [
			'light_armor',
			'wisdom_saving_throw', 'charisma_saving_throw',
		]+items.simple_weapons, base.union)
		base.add(self, 'features', _Progression([
			['otherworldly_patron', 'pact_magic'],
			['eldritch_invocations'],
			['pact_boon'],
			['ability_score_improvement'],
			[],
			['otherworldly_patron'],
			[],
			['ability_score_improvement'],
			[],
			['otherworldly_patron'],
			['mystic_arcanum'],
			['ability_score_improvement'],
			['mystic_arcanum'],
			['otherworldly_patron'],
			['mystic_arcanum'],
			['ability_score_improvement'],
			['mystic_arcanum'],
			[],
			['ability_score_improvement'],
			['eldritch_master'],
		], level), base.plus)
		base.add(self, 'slots', [
			[0, 0, 0, 0, 0, 0, 0, 0, 0],
			[1, 0, 0, 0, 0, 0, 0, 0, 0],
			[2, 0, 0, 0, 0, 0, 0, 0, 0],
			[0, 2, 0, 0, 0, 0, 0, 0, 0],
			[0, 2, 0, 0, 0, 0, 0, 0, 0],
			[0, 0, 2, 0, 0, 0, 0, 0, 0],
			[0, 0, 2, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 2, 0, 0, 0, 0, 0],
			[0, 0, 0, 2, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 2, 0, 0, 0, 0],
			[0, 0, 0, 0, 2, 0, 0, 0, 0],
			[0, 0, 0, 0, 3, 0, 0, 0, 0],
			[0, 0, 0, 0, 3, 0, 0, 0, 0],
			[0, 0, 0, 0, 3, 0, 0, 0, 0],
			[0, 0, 0, 0, 3, 0, 0, 0, 0],
			[0, 0, 0, 0, 3, 0, 0, 0, 0],
			[0, 0, 0, 0, 3, 0, 0, 0, 0],
			[0, 0, 0, 0, 4, 0, 0, 0, 0],
			[0, 0, 0, 0, 4, 0, 0, 0, 0],
			[0, 0, 0, 0, 4, 0, 0, 0, 0],
			[0, 0, 0, 0, 4, 0, 0, 0, 0],
		][level], lambda old, new: [old[i]+new[i] for i in range(9)])
		self.cantrips=2
		if level>=4: self.cantrips+=1
		if level>=10: self.cantrips+=1
		self.spells=[0, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15][level]
		self.invocations=[0, 0, 2, 2, 2, 3, 3, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8][level]
		if kwargs.get('new', False):
			base.add(self, 'choices', {
				'2 warlock skills': [
					'arcana', 'deception', 'history', 'intimidation',
					'investigation', 'nature', 'religion',
				],
				'warlock weapon': [['light_crossbow', 'quiver']]+items.simple_weapons,
				'warlock weapon 2': items.simple_weapons,
				'warlock junk': ['component_pouch', 'arcane_focus'],
				'warlock pack': ['scholars_pack', 'dungeoneers_pack'],
				'warlock alternate gp': '4d4*10',
			}, base.dict_add)
			self.wearing=['leather_armor', 'dagger', 'dagger']

	def spellcasting_ability(self): return self.charisma
