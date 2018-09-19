from . import base

class Generic:
	@staticmethod
	def init(self, **kwargs):
		if kwargs.get('new', False):
			base.add(self, 'choices', {
				'background skills': 'any 2',
				'background languages or tools': 'any 2',
			}, base.dict_add)

class FolkHero:
	@staticmethod
	def init(self, **kwargs):
		base.add(self, 'proficiencies',
			['animal_handling', 'survival', 'land_vehicles'],
			base.union
		)
		if kwargs.get('new', False):
			base.add(self, 'choices', {
				'background language': 'any 1',
			}, base.dict_add)

class Sage:
	@staticmethod
	def init(self, **kwargs):
		base.add(self, 'proficiencies',
			['arcana', 'history'],
			base.union
		)
		if kwargs.get('new', False):
			base.add(self, 'choices', {
				'background languages': 'any 2',
			}, base.dict_add)
		

class Soldier:
	@staticmethod
	def init(self, **kwargs):
		base.add(self, 'proficiencies',
			['athletics', 'intimidation', 'land_vehicles'],
			base.union
		)
		if kwargs.get('new', False):
			base.add(self, 'choices', {
				'background language': 'any 1',
			}, base.dict_add)
