import base

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
