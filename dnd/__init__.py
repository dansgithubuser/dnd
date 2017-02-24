from base import *
import backgrounds, classes, creatures, items, languages, names, races, skills
import special_qualities, test, tools

traveling={
	'slow'  : ['200 ft/min', '2 mi/h', '18 mi/day', 'may stealth'],
	'normal': ['300 ft/min', '3 mi/h', '24 mi/day'],
	'fast'  : ['400 ft/min', '4 mi/h', '30 mi/day', '-5 passive perception'],
}

cover={
	'half' : '+2 to ac and dex saving throws',
	'3/4'  : '+5 to ac and dex saving throws',
	'total': 'cannot be targeted by attacks or spells',
}

donning_and_doffing_armor={
	'light' : {'don': '1 min'   , 'doff': '1 min'},
	'medium': {'don': '5 min'   , 'doff': '1 min'},
	'heavy' : {'don': '10 min'  , 'doff': '5 min'},
	'shield': {'don': '1 action', 'doff': '1 action'},
}

exhaustion=[
	'disadvantage on ability checks',
	'speed halved',
	'disadvantage on attack rolls and saving throws',
	'max hp halved',
	'speed 0',
	'dead',
]

def fall_damage(height): return '{}d6'.format(height//10)
