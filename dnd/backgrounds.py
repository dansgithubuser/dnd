class Generic:
	def __init__(self, **kwargs):
		if kwargs.get('new', False): self.choices.update({
			'background skills': 'any 2',
			'background languages or tools': 'any 2',
		})

class FolkHero:
	def __init__(self):
		self.proficiencies+=['animal_handling', 'survival', 'land_vehicles']

class Sage:
	def __init__(self):
		self.proficiencies+=['arcana', 'history']

class Soldier:
	def __init__(self):
		self.proficiencies+=['athletics', 'intimidation', 'land_vehicles']
