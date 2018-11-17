from . import base

class Gendered(base.Entity):
	def __init__(self, gender='mf', **kwargs):
		if len(gender)>1: gender=base.pick(gender)
		self.gender=gender

class Human(Gendered):
	def __init__(self, **kwargs):
		Gendered.__init__(self, **kwargs)
		self.type='human'
		self.size='medium'
		self.speed=30
		self.strength+=1
		self.dexterity+=1
		self.constitution+=1
		self.intelligence+=1
		self.wisdom+=1
		self.charisma+=1
		self.languages=['common']
		if kwargs.get('new', False): self.choices={
			'age': (18, 80),
			'height': (5, 6),
			'weight': (100, 180),
			'language': 'one extra language',
		}

class Elf(Gendered):
	def __init__(self, **kwargs):
		Gendered.__init__(self, **kwargs)
		self.type='elf'
		self.size='medium'
		self.speed=30
		self.dexterity+=2
		self.special_qualities=['darkvision', 'fey_ancestry', 'trance']
		self.proficiencies=['perception']
		self.languages=['common', 'elvish']
		if kwargs.get('new', False): self.choices={
			'age': (100, 750),
			'height': (5, 6),
			'weight': (100, 145),
		}

class HighElf(Elf):
	def __init__(self, **kwargs):
		Elf.__init__(self, **kwargs)
		self.intelligence+=1
		self.proficiencies+=['longsword', 'shortsword', 'shortbow', 'longbow']
		if kwargs.get('new', False): self.choices.update({
			'cantrip': 'one wizard cantrip',
			'language': 'one extra language',
		})

class WoodElf(Elf):
	def __init__(self, **kwargs):
		Elf.__init__(self, **kwargs)
		self.proficiencies+=['longsword', 'shortsword', 'shortbow', 'longbow']
		self.speed+=5
		self.wisdom+=1
		self.special_qualities+=['mask_of_the_wild']

class Dwarf(Gendered):
	def __init__(self, **kwargs):
		Gendered.__init__(self, **kwargs)
		self.type='dwarf'
		self.size='medium'
		self.speed=25
		self.constitution+=2
		self.special_qualities=['darkvision', 'dwarven_resilience', 'stonecunning', 'dwarf_speed']
		self.proficiencies=['battleaxe', 'handaxe', 'light_hammer', 'warhammer']
		self.languages=['common', 'dwarvish']
		if kwargs.get('new', False): self.choices={
			'age': (50, 350),
			'height': (4, 5),
			'weight': (130, 170),
			'tool proficiency': ['smiths_tools', 'brewers_supplies', 'masons_tools'],
		}

class HillDwarf(Dwarf):
	def __init__(self, **kwargs):
		Dwarf.__init__(self, **kwargs)
		self.wisdom+=1
		self.special_qualities+=['dwarven_toughness']

class MountainDwarf(Dwarf):
	def __init__(self, **kwargs):
		Dwarf.__init__(self, **kwargs)
		self.strength+=2
		self.proficiencies+=['light_armor', 'medium_armor']

class Dragonborn(Gendered):
	def __init__(self, **kwargs):
		Gendered.__init__(self, **kwargs)
		self.type='dragonborn'
		self.size='medium'
		self.speed=30
		self.strength+=2
		self.charisma+=1
		self.languages=['common', 'draconic']
		if kwargs.get('new', False): self.choices={
			'age': (15, 80),
			'height': (6, 8),
			'weight': (175, 325),
			'draconic ancestry': [
				'black', 'blue', 'brass', 'bronze', 'copper', 'gold', 'green',
				'red', 'silver', 'white',
			],
		}

class Gnome(Gendered):
	def __init__(self, **kwargs):
		Gendered.__init__(self, **kwargs)
		self.type='gnome'
		self.size='small'
		self.speed=25
		self.intelligence+=2
		self.special_qualities=['darkvision', 'gnome_cunning']
		self.languages=['common', 'gnomish']
		if kwargs.get('new', False): self.choices={
			'age': (40, 350),
			'height': (3, 4),
			'weight': (35, 45),
		}

class RockGnome(Gnome):
	def __init__(self, **kwargs):
		Gnome.__init__(self, **kwargs)
		self.proficiencies=['tinkers_tools']
		self.constitution+=1
		self.special_qualities+=['artificers_lore']

class ForestGnome(Gnome):
	def __init__(self, **kwargs):
		Gnome.__init__(self, **kwargs)
		self.dexterity+=1
		self.spells=[[] for i in range(9)]
		self.spells[0].append('minor_illusion')
		self.special_qualities+=['speak_with_small_beasts']

class Tiefling(Gendered):
	def __init__(self, **kwargs):
		Gendered.__init__(self, **kwargs)
		self.type='tiefling'
		self.size='medium'
		self.speed=30
		self.charisma+=2
		self.intelligence+=1
		self.special_qualities=['darkvision']
		self.resistances=['fire']
		self.spells=[[] for i in range(9)]
		self.spells[0].append('thaumaturgy')
		l=kwargs.get('level', 1)
		if l>=2: self.spells[2].append('hellish_rebuke')
		if l>=5: self.spells[2].append('darkness')
		self.languages=['common', 'infernal']
		if kwargs.get('new', False): self.choices={
			'age': (18, 85),
			'height': (5, 6),
			'weight': (100, 180),
		}
