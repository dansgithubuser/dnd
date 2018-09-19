from . import base

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

def random_tone():
	return base.pick([
		'excitable', 'calm', 'cranky', 'condescending',
	])

def random_vocalization():
	return base.pick([
		'crusty', 'stage_whisper', 'wheezy',
	])

def random_misc():
	result=[]
	if base.maybe(4): result.append('high_pitch')
	if base.maybe(2): result.append(base.pick(['verbose', 'unvocal']))
	if base.maybe(4): result.append(base.pick(['softspoken', 'loud']))
	if base.maybe(4): result.append(base.pick(['shy', 'curious']))
	return result

def random_common_accent():
	return base.pick([
		'lisp', 'russian', 'american', 'swedish', 'scottish', 'french', 'rich',
		'nerd', 'pinky',
	])

def random_human_voice():
	result=[]
	if base.maybe(2): result.append(random_common_accent())
	if base.maybe(8): result.append(random_vocalization())
	if base.maybe(4): result.append(random_tone())
	result.extend(random_misc())
	return result
