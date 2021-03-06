from . import base

spells={}

def half(damage):
	return {i: j//2 for i, j in damage.items()}

def get_affected(spell, origin, entities):
	shape, size=base.key(spells, (None, None), spell, 'area')
	if shape=='sphere': return [i for i in entities if i.distance(*origin)<size]
	else: raise Exception('bad shape {}'.format(shape))
