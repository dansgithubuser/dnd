import base, creatures, spells

def test():
	print('dice')
	assert(base.split_roll_request('1d10 FIRE+2 LIGHTNING+d10 POISON+1d8+3+d12')==[
		'1d10 FIRE',
		'2 LIGHTNING',
		'd10 POISON',
		'1d8',
		'3',
		'd12',
	])
	assert(base.number_and_type('8 FIRE')==(8, 'FIRE'))
	assert(base.dice_sides_type('3d4 FIRE')==(3, 4, 'FIRE'))
	assert(base.dice_sides_type( 'd4 FIRE')==(1, 4, 'FIRE'))
	print('spells')
	g=base.Group([creatures.TypicalHumanArcher() for i in range(8)])
	g.move(0, 0)
	[i.move(80, 0) for i in g[0:4]]
	w=creatures.Witherweed()
	w.move(0, 0)
	w.cast('witherweed_fumes')
	print('creatures')
	import inspect
	for i in [i[1] for i in inspect.getmembers(creatures) if inspect.isclass(i[1])]:
		i().test()
