class Traits:
	def __init__(self, typical_speakers, script):
		self.typical_speakers=typical_speakers
		self.script=script

standard={
	'common': Traits(['humans'], 'common'),
	'dwarvish': Traits(['dwarves'], 'dwarvish'),
	'elvish': Traits(['elves'], 'elvish'),
	'giant': Traits(['ogres', 'giants'], 'common'),
	'gnomish': Traits(['gnomes'], 'dwarvish'),
	'goblin': Traits(['goblinoids'], 'dwarvish'),
	'orc': Traits(['orcs'], 'dwarvish'),
}

exotic={
	'abyssal': Traits(['demons'], 'infernal'),
	'celestial': Traits(['celestials'], 'celestial'),
	'draconic': Traits(['dragons', 'dragonborn'], 'draconic'),
	'deep_speech': Traits(['mind_flayers', 'beholders'], None),
	'infernal': Traits(['devils'], 'infernal'),
	'primordial': Traits(['elementals'], 'dwarvish'),
	'sylvan': Traits(['fey_creatures'], 'elvish'),
	'undercommon': Traits(['underdark_traders'], 'elvish'),
}
