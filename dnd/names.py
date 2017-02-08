import base

vowels='aeiouy'
friendly_consonants='bcdfghjklmnprstvwz'

def is_vowel(l):
	try: return l in vowels
	except: return False

def transform(name, kernel):
	import inspect
	result=''
	for i in range(len(name)):
		a=len(inspect.getargspec(kernel).args)
		if   a==1: result+=kernel(name[i])
		elif a==2: result+=kernel(name, i)
		elif a==3: result+=kernel(
			None if i==0 else name[i-1],
			name[i],
			None if i==len(name)-1 else name[i+1]
		)
	return result

def remove_weird_vowels(name):
	def kernel_triplets(last, current, next):
		if all(is_vowel(i) for i in [last, current, next]): return ''
		return current
	def kernel_repeats(last, current, next):
		if '{}{}'.format(last, current) in [
			'aa', 'ae', 'ao', 'ee', 'ii', 'iu', 'oa', 'ue', 'uo', 'uu',
			'iw', 'uw',
		]: return ''
		return current
	while True:
		old=name
		name=transform(name, kernel_triplets)
		name=transform(name, kernel_repeats)
		if old==name: return name

def vowelify(name, vowel):
	def kernel(l):
		if is_vowel(l) and base.maybe(): return vowel
		return l
	return transform(name, kernel)

def misspell(name, source):
	def kernel(last, current, next):
		if(not is_vowel(current) and base.maybe(4) and(
			not last and is_vowel(next)
			or
			not next and is_vowel(last)
			or
			is_vowel(last) and is_vowel(next)
		)): return base.pick(source)
		return current
	return transform(name, kernel)

def humanify(name, vowel, misspelling_source):
	if vowel:
		if base.rn(3): name=vowelify(name, vowel)
	if base.rn(3): name=misspell(name, misspelling_source)
	return remove_weird_vowels(name)

human_last=[
	'alpha', 'anton', 'armand', 'alvaro',
	'boyce', 'benton', 'bradford',
	'colton', 'cortez', 'clark',
	'deangelo', 'del', 'delbert',
	'eldridge', 'erasmo',
	'filiberto', 'fausto', 'felton',
	'granville', 'genesis',
	'hobert', 'harland', 'hayden',
	'isidro', 'inez',
	'jared', 'jayne',
	'kendrick', 'kerry',
	'lynwood', 'latonia', 'lizette',
	'marcellus', 'mcmaster',
	'nolan', 'nicola',
	'orville', 'oneida', 'ozella',
	'porter', 'providencia',
	'queen', 'quinn',
	'rey', 'rolf',
	'sherwood', 'salvatore',
	'tyron', 'tomas',
	'un', 'ute',
	'valene', 'valentine',
	'winford', 'warner', 'waltraud',
	'xylmore', 'xebec',
	'yael', 'young',
	'zada', 'zetta', 'zena',
]

def human(gender):
	if gender=='m':
		first=[
			'abner', 'albert', 'alfonso', 'arnold', 'abraham',
			'barney', 'boris', 'benedict', 'bartholomew',
			'constantine', 'cornelius', 'craig', 'cedrick', 'cid', 'claude',
			'clyde', 'cameron', 'chad', 'caleb',
			'dennis', 'dimitri', 'david', 'douglas', 'dexter',
			'edward', 'edmund', 'ezekiel', 'edison', 'elliot', 'emilio',
			'fernando', 'finn', 'frank',
			'gabe', 'gary', 'gregor', 'gaston', 'garth', 'guadalupe',
			'harry', 'herbert', 'hugo',
			'ian', 'indira', 'ivan', 'isaac', 'irving', 'ignacio',
			'john', 'jarret', 'jordan',
			'kenneth', 'kevin', 'kermit',
			'luigi', 'lincoln',
			'marcel', 'malcolm', 'milhous',
			'nathaniel', 'neville', 'nigel',
			'oswald', 'octavio',
			'pierre', 'percy',
			'quentin', 'quincy',
			'robert', 'raymond', 'rudolph',
			'stephen', 'sebastian', 'stuart', 'sylvester',
			'tony', 'terence',
			'ulysses', 'ulrike',
			'virgilio', 'vince',
			'wally', 'william', 'wesley', 'wilhelm',
			'xavier', 'xeno',
			'yuri', 'yolando',
			'zachary',
		]
	else:
		first=[
			'alison', 'anastasia', 'agnes', 'amelia',
			'barbara', 'betty', 'bernice',
			'carol', 'clara', 'carri', 'cecilia',
			'dorothy', 'doris', 'darlene', 'delilah', 'dolores',
			'evelyn', 'emily', 'edna', 'eleanor', 'esther', 'emma', 'eva',
			'felicia', 'faye', 'fannie',
			'genevieve', 'gretchen', 'gwendolyn',
			'heidi', 'helen', 'harriet',
			'ingrid', 'ida', 'irma', 'iris', 'isabelle', 'imogene', 'imelda',
			'joyce', 'judith', 'josephine',
			'katerina', 'kendra', 'kelsey',
			'lisa', 'lillian', 'lucille', 'lorraine',
			'marla', 'margaret', 'martha', 'mildred', 'marjorie', 'mabel', 'meredith',
			'nancy', 'norma',
			'olga', 'olivia', 'olympia', 'omega', 'odelia', 'oretha', 'ouranos',
			'patricia', 'phyllis',
			'ruth', 'regina',
			'sophie', 'sandra', 'sherry', 'sheila',
			'thelma', 'tammy',
			'ursula', 'ultima',
			'veronica', 'virginia', 'violet', 'velma',
			'wendolyn', 'wilma', 'winifred', 'willow', 'winona',
			'xena', 'xenia',
			'yvonne', 'yasmin',
			'zoe', 'zelda',
		]
	if gender=='m':
		first=humanify(base.pick(first), 'o', friendly_consonants)
	else:
		first=humanify(base.pick(first), 'a', 'ai')
	last=humanify(base.pick(human_last), base.pick('aeiou'), friendly_consonants)
	if base.maybe(32): last=base.pick(['van', 'von'])+' '+last
	return first+' '+last
