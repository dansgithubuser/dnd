import base

class Human(base.Entity):
	def __init__(self):
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

class Elf(base.Entity):
	def __init__(self):
		self.type='elf'
		self.size='medium'
		self.speed=30
		self.dexterity+=2
		self.special_qualities=['darkvision', 'fey_ancestry', 'trance']
		self.proficiencies=['perception']
		self.languages=['common', 'elvish']

class HighElf(Elf):
	def __init__(self):
		Elf.__init__(self)
		self.intelligence+=1
		self.proficiencies+=['longsword', 'shortsword', 'shortbow', 'longbow']

class WoodElf(Elf):
	def __init__(self):
		Elf.__init__(self)
		self.proficiencies+=['longsword', 'shortsword', 'shortbow', 'longbow']
		self.speed+=5
		self.wisdom+=1
		self.special_qualities+=['mask_of_the_wild']
