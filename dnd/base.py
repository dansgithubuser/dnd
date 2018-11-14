from __future__ import print_function

from . import backgrounds, classes, items, skills, spells

import inspect, random, os

log=False
placed_entities=set()

def rn(m):
	'''\
if m is an integer, random number in [0, m)
if m is a tuple, random number in [m[0], m[1]]'''
	if type(m)==int: return random.randint(0, m-1)
	elif type(m)==tuple: return random.randint(m[0], m[1])

def maybe(unlikeliness=2): return not rn(unlikeliness)

def swap(list, i, j): x=list[i]; list[i]=list[j]; list[j]=x

def pick_n(list, n):
	import copy
	list=copy.deepcopy(list)
	result=[]
	for i in range(n):
		j=rn(len(list))
		result.append(list[j])
		del list[j]
	return result

def pick(list, n=1):
	'return a pick from list, or a list of picks from list if n is not 1'
	if n==1: return list[rn(len(list))]
	return pick_n(list, n)

def pick_weighted(item_to_weight):
	items=list(item_to_weight.items())
	pick=rn(sum([v for k, v in items]))
	i=0
	while True:
		pick-=items[i][1]
		if pick<=0: break
		i+=1
	return items[i][0]

def flatten(list):
	r=[]
	for i in list:
		if type(i)==list: r.extend(i)
		else: r.append(i)
	return r

def timestamp(ambiguous=True):
	import datetime
	format='{:%Y-%m'
	if not ambiguous: format+='-%b'
	format+='-%d %H:%M:%S.%f}'
	return format.format(datetime.datetime.now()).lower()

def key(x, default, *indices):
	try:
		for i in indices:
			if type(x)==dict and i in x: x=x[i]
			elif type(i)==int: x=x[i]
			elif type(i)==str and hasattr(x, i): x=getattr(x, i)
			else: return default
		return x
	except: return default

def log_attr_set(self, attr, value):
	name=key(self, '{} {}'.format(self.__class__, hex(id(self))), 'name')
	self.__dict__[attr]=value
	if log and not callable(value):
		if type(value)==str: value="'"+value+"'"
		with open('log.txt', 'a') as file: file.write("- {} '{}' {}={}\n".format(
			timestamp(), name, attr, value
		))

def add(object, member, value, method):
	'''\
object.member=method(object.member, value)
useful for accumulating a value in a member you aren't sure exists yet
'''
	if hasattr(object, member): value=method(getattr(object, member), value)
	setattr(object, member, value)

def union(x, y): return x+[i for i in y if i not in x]
def plus(x, y): return x+y
def plus_string(x, y): return x+'+'+y
def dict_add(x, y): return dict(x, **y)
def spell_add(x, y):
	'add two spell lists together, spell lists are like spell_list[level][i]'
	r=[[] for i in range(9)]
	for i in range(9):
		if i<len(x): r[i]=x[i]
		if i<len(y): r[i]=union(r[i], y[i])
	return r

def set_methods(e, c):
	'copy methods of c onto e'
	for name, member in inspect.getmembers(c):
		if inspect.ismethod(member): setattr(e, name, member)

def get(x, condition):
	'get the first element in x that fulfills condition'
	for i in x:
		if condition(i): return i
	return None

def split_roll_request(request):
	'split by +'
	return request.split('+')

def split_type(request):
	'get damage type if it exists, else return empty string'
	x=request.split()
	if len(x)>1: return x[1]
	return ''

def number_and_type(request):
	x=request.split()
	number=int(x[0])
	type=''
	if len(x)==2: type=x[1]
	return number, type

def dice_sides_type(request):
	'split roll request into dice, sides, and type'
	dice=1
	type=''
	x=request.split('d')
	dice=int(x[0]) if x[0] else 1
	sides, type=number_and_type(x[1])
	return dice, sides, type

def typical_roll(sides, roll, critical_hit=20, critical_miss=1):
	if len(roll)==1 and sides==20:
		if roll[0]<=critical_miss: print('critical miss!')
		if roll[0]>=critical_hit : print('critical hit!')
	return roll

class AttackRoll:
	'Class whose instances can be called roll(on_roll=instance) to store critical hit or miss.'
	def __init__(self, critical_hit=20, critical_miss=1):
		self.critical=0
		self.critical_hit=critical_hit
		self.critical_miss=critical_miss

	def __call__(self, sides, roll):
		if roll[0]<=self.critical_miss: self.critical=-1
		if roll[0]>=self.critical_hit : self.critical= 1
		return typical_roll(sides, roll, self.critical_hit, self.critical_miss)

def roll(request, vantage=0, on_roll=typical_roll):
	'''make a roll (ex: 3d4+4 FIRE)
with advantage (vantage<0) or disadvantage (vantage>0)
and customizable on_roll behavior (default typical_roll)
'''

	#print intent
	print(request, end=': ')
	if vantage>0: print('with advantage')
	if vantage<0: print('with disadvantage')
	#helpers
	def inner(request, vantage):
		x=[]
		for i in split_roll_request(request):
			if 'd' in i:
				dice, sides, type=dice_sides_type(i)
				x.append([
					i,
					[random.randint(1, sides) for i in range(dice)],
				])
			else: x.append((i, [number_and_type(i)[0]]))
		print(x, end=' --> ')
		return x
	def total(x): return sum([sum(i[1]) for i in x])
	#first roll
	a=inner(request, vantage)
	#vantage
	if vantage:
		#second roll
		b=inner(request, vantage)
		if vantage<0 and total(b)<total(a): a=b
		if vantage>0 and total(b)>total(a): a=b
	#on_roll
	for i in a:
		if 'd' in i[0]: i[1]=on_roll(dice_sides_type(i[0])[1], i[1])
	#convert to {type: amount}, show, and return
	import collections
	x=collections.defaultdict(int)
	t=''
	for i in range(len(a)):
		y=split_type(a[i][0])
		if y: t=y
		x[t]+=sum(a[i][1])
	items=list(x.items())
	if len(x)==1 and not items[0][0]: x=items[0][1]
	elif len(x)==2 and '' in x.keys(): x={[i for i in x.keys() if i][0]: sum([i for i in x.values()])}
	else: x=dict(x)
	print(x)
	return x

def d20(): return roll('d20')

def modifier(stat): return (stat-10)//2

class Entity:
	'Base class that creates some aliases for common attributes, logging, and some helper methods.'

	def __getattr__(self, attr):
		if attr=='str': return self.strength
		if attr=='dex': return self.dexterity
		if attr=='con': return self.constitution
		if attr=='int': return self.intelligence
		if attr=='wis': return self.wisdom
		if attr=='cha': return self.charisma
		if attr=='ac': return self.armor_class()
		if attr in ['spell_save_dc', 'ssdc', 'sdc']: return self.spell_save_difficulty_class()
		if attr=='sab': return self.spell_attack_bonus()
		raise AttributeError

	def __setattr__(self, attr, value): log_attr_set(self, attr, value)

	def set_stats(self, strength, dexterity, constitution, intelligence, wisdom, charisma):
		self.strength=strength
		self.dexterity=dexterity
		self.constitution=constitution
		self.intelligence=intelligence
		self.wisdom=wisdom
		self.charisma=charisma

	def add_hit_dice(self, dice, sides):
		add(self, 'hit_dice', '{}d{}'.format(dice, sides), plus_string)
		if hasattr(self, 'constitution'):
			if not hasattr(self, 'max_hp'): self.max_hp=sides+(sides//2+1)*(dice-1)+dice*modifier(self.constitution)
			if not hasattr(self, 'hp'): self.hp=self.max_hp

	def show(self, do_print=True):
		import pprint
		def numbered_section(i): return '{:01}'.format(i)
		def divine_key(attribute):
			name=attribute[0]
			groups=[
				['name', 'level', 'type', 'alignment', 'size', 'hit_dice', 'max_hp', 'speed', 'age', 'height', 'weight'],
				['strength', 'dexterity', 'constitution', 'intelligence', 'wisdom', 'charisma', '1'],
				['proficiency_bonus', 'proficiencies', 'expertise', 'languages', 'slots', 'spells', 'features', 'special_qualities'],
				['natural_armor', 'environment', 'organization'],
				[],
			]
			groups=[[numbered_section(i)]+groups[i] for i in range(len(groups))]
			for i in range(len(groups)):
				if name in groups[i]:
					return '___{:02}.{:02}'.format(i, groups[i].index(name))
			return name
		sections=['overall', 'stats', 'abilities', 'nature', 'other']
		separators=[(numbered_section(i), '-'*20+sections[i]+'-'*20) for i in range(len(sections))]
		derived=[(i, getattr(self, i)()) for i in [
			'armor_class',
		]]
		x=pprint.pformat(sorted(
			[i for i in vars(self).items() if not callable(i[1])]+separators+derived,
			key=divine_key
		))
		if do_print: print(x)
		return x

	def roll_stats(self):
		self.max_hp=roll(self.hit_dice)
		self.hp=self.max_hp

	def roll_initiative(self):
		return roll('d20+{}'.format(modifier(self.dexterity)))

	def attack(self, method=None, vantage=0, critical_hit=20, target=None):
		if self.hp<=0:
			print('unconscious')
			return (0, 0)
		#method
		attack='d20'
		stat_mod=modifier(self.strength)
		if method==None:
			method=(
				key(self, '', 'attacks', 0, 0)
				or
				key([i for i in key(self, [], 'wearing') if 'weapon' in key(items.items, '', i, 'type')], '', 0)
			)
		print(method)
		if method=='unarmed': damage='1 BLUDGEONING'
		elif method in items.items:
			if method not in key(self, [], 'wearing'): print('not wearing')
			damage=items.items[method]['damage']
			if 'finesse' in key(items.items, '', method, 'properties'):
				stat_mod=max(stat_mod, modifier(self.dexterity))
			elif key(items.items, '', method, 'type')=='ranged_weapon':
				stat_mod=modifier(self.dexterity)
		elif hasattr(self, 'attacks'):
			try:
				i=[i[0] for i in self.attacks].index(method)
				attack+='+{}'.format(self.attacks[i][1])
				damage=self.attacks[i][2]
				if 'finesse' in self.attacks[i]:
					stat_mod=max(stat_mod, modifier(self.dexterity))
				elif 'range' in self.attacks[i]:
					stat_mod=modifier(self.dexterity)
			except: pass
		if 'damage' not in locals(): raise Exception('no such attack method "{}"'.format(method))
		#attack
		attack_roll=AttackRoll(critical_hit)
		p=self.proficiency(method)
		a=roll('{}+{}+{}'.format(attack, stat_mod, p), vantage, attack_roll)
		#damage
		if attack_roll.critical:
			critical_damage=[]
			for i in split_roll_request(damage):
				if 'd' in i:
					dice, sides=dice_sides_type(i)[0:2]
					critical_damage.append('{}d{}'.format(2*dice, sides))
				else: critical_damage.append(i)
			damage='+'.join(critical_damage)
		d=roll('{}+{}'.format(damage, stat_mod))
		#target
		if target:
			if target.armor_class()<=a:
				print('hit')
				target.damage(d)
			else: print('miss')
		#
		self.print_notes('attack')
		return (a, d)

	def full_attack(self, vantage=0):
		for i in key(self, [], 'attacks'):
			print('----> {}'.format(self.attack(i[0], vantage)))
		for i in key(self, [], 'wearing'):
			if 'weapon' in key(items.items, '', i, 'type'):
				print('-----> {}'.format(self.attack(i)))

	def cast(self, spell=None, origin=None):
		if spell==None:
			for i in self.spells:
				if len(i): spell=i[0]; break
		if spell not in spells.spells:
			raise Exception('no such spell "{}"'.format(spell))
		print(spell)
		s=spells.spells[spell]
		damage=roll(s['damage'])
		if origin==None:
			if not all([hasattr(self, i) for i in 'xyz']): return
			origin=(self.x, self.y, self.z)
		entities=spells.get_affected(spell, origin, placed_entities)
		if 'save' in s: dc, type=number_and_type(s['save'])
		for i in entities:
			x=damage
			if 'save' in s and i.check(type.lower())>=dc: x=s['save_effect'](damage)
			i.damage(x)

	def proficiency(self, what):
		if what not in key(self, [], 'proficiencies'): return 0
		r=key(self, 2, 'proficiency_bonus')
		if what in key(self, [], 'expertise'): r*=2
		return r

	def disadvantages(self):
		result=[]
		for i in key(self, [], 'wearing'):
			result+=items.items[i].get('disadvantages', [])
			if 'armor' in i or 'shield' in i and i not in self.proficiencies:
				result+=['unproficient_armor']
		return result

	def armor_class(self):
		result=0
		armor_type=''
		shield=False
		for i in key(self, [], 'wearing'):
			result+=key(items.items, 0, i, 'armor_class')
			x=key(items.items, '', i, 'type')
			if 'armor' in x: armor_type=x
			if 'shield' in x: shield=True
		if not shield and not armor_type: result=10
		if 'heavy' in armor_type: pass
		elif 'medium' in armor_type: result+=min(modifier(self.dexterity), 2)
		else: result+=modifier(self.dexterity)
		result+=key(self, 0, 'natural_armor')
		self.print_notes('armor_class')
		return result

	def damage(self, points):
		if not hasattr(self, 'token'): print('warning: token attr not set, logs will not provide full context')
		old_hp=self.hp
		if type(points)==int: self.hp-=points
		else:
			if type(points)==str:
				n, t=number_and_type(points)
				points={t: n}
			for t, p in points.items():
				t=t.lower()
				if t in key(self, [], 'vulnerabilities'): p*=2
				if t in key(self, [], 'resistances'): p/=2
				if t in key(self, [], 'damage_immunities'): p=0
				self.hp-=p
		print('{0}/{2} --> {1}/{2}'.format(old_hp, self.hp, self.max_hp))
		if old_hp>=self.max_hp/2>self.hp: print('bloodied')
		if self.hp<0: print('unconscious')
		self.print_notes('damage')

	def saving_throw(self, type, vantage=0):
		return roll('d20+{}+{}'.format(
			modifier(getattr(self, type)),
			self.proficiency(type+'_saving_throw'),
		), vantage)

	def move(self, x, y, z=0):
		self.x=x
		self.y=y
		self.z=z
		placed_entities.add(self)

	def distance(self, x, y, z=0):
		import math
		return math.sqrt((self.x-x)**2+(self.y-y)**2+(self.z-z)**2)

	def check(self, skill, vantage=0):
		if skill in self.disadvantages(): vantage-=1
		return roll('d20+{}+{}'.format(
			modifier(getattr(self, skills.skills[skill])),
			self.proficiency(skill),
		), vantage)

	def passive_perception(self):
		return 10+modifier(self.wisdom)+self.proficiency('perception')

	def carrying_load(self):
		print('capacity {}'.format(self.carrying_capacity()))
		x=[]
		x+=key(self, [], 'wearing')
		x+=key(self, [], 'carrying')
		r=0
		for i in x:
			m=1
			if   type(i)==dict: s, m=list(i.items())[0]
			elif type(i)==str: s=i
			w=m*key(items.items, 0, s, 'weight')
			print(m, s, w)
			r+=w
		return r

	def carrying_capacity(self):
		r=self.strength*15
		if self.size=='tiny': r//=2
		if self.size=='large': r*=2
		if self.size=='huge': r*=4
		if self.size=='gargantuan': r*=4
		return r

	def push_drag_lift(self): return self.carrying_capacity()*2

	def spell_save_difficulty_class(self):
		return 8+self.proficiency_bonus+modifier(self.spellcasting_ability())

	def spell_attack_bonus(self):
		return self.proficiency_bonus+modifier(self.spellcasting_ability())

	def print_notes(self, topic):
		if hasattr(self, 'notes'):
			if topic in self.notes: print(self.notes[topic])

	def test(self):
		print('===== {} ====='.format(self.__class__))
		print('----- full attack -----')
		self.full_attack()
		print('----- armor class -----')
		print(self.armor_class())
		print('----- passive perception -----')
		print(self.passive_perception())
		print('----- carrying load -----')
		self.carrying_load()

def entities_from_log(file_name, modules={}):
	if not os.path.exists(file_name): return {}
	import creatures, re
	with open(file_name) as file:
		entities={}
		def to_var_name(x): return re.sub('[. ]', '_', x)
		for line in file.readlines():
			m=re.match(r"- \d+-\d+-\d+ \d+:\d+:\d+\.\d+ '([^']+)' ([^=]+)=(.+)", line)
			if not m: continue
			entity, attr, value=m.groups()
			variable=to_var_name(entity)
			value=re.sub(r'<([\S]+) instance at ([^>]+)>', r'entities["\1_\2"]', value)
			while True:
				old=value
				value=re.sub(r'entities\["([^.]+)\.', r'entities["\1_', value)
				if old==value: break
			value=eval(value)
			if variable not in entities:
				class_name=entity.split()[0]
				if class_name.split('.')[0] in modules:
					entities[variable]=key(modules, None, *class_name.split('.'))()
					assert entities[variable]!=None
				else:
					if class_name.startswith('dnd.'): class_name=class_name[4:]
					if class_name.startswith('base.'): class_name=class_name[5:]
					entities[variable]=eval(class_name)()
			setattr(entities[variable], attr, value)
			if attr=='name': entities[to_var_name(value)]=entities[variable]
	return entities

class Group:
	def __init__(self, entities=[]): self.entities=entities

	def __setattr__(self, attr, value): log_attr_set(self, attr, value)

	def __getattr__(self, attr):
		x=[getattr(i, attr) for i in self.entities]
		if callable(x[0]):
			class Caller:
				def __init__(self, entities): self.entities=entities
				def __call__(self, *args, **kwargs): return [i(*args, **kwargs) for i in self.entities]
			return Caller(x)
		else:
			return x

	def __getitem__(self, i): return self.entities[i]

def create_character(stats, race, classes, background=backgrounds.Generic):
	x='''class Character(race, *classes, background):
		def __init__(self):
			self.strength={strength}
			self.dexterity={dexterity}
			self.constitution={constitution}
			self.intelligence={intelligence}
			self.wisdom={wisdom}
			self.charisma={charisma}
			race.__init__(self, new=True)
			for c, l in classes.items(): c.init(self, l, new=True)
			background.init(self, new=True)'''.format(**stats)
	g={'race': race, 'classes': classes, 'background': background}
	exec(x, g)
	return g['Character']()

def random_heroic_stats():
	s=['strength', 'dexterity', 'constitution', 'intelligence', 'wisdom', 'charisma']
	while True:
		r={j: sum(sorted([roll('d6') for i in range(4)])[1:]) for j in s}
		if sum([v for k, v in r.items()])>=72: break
	return r

def random_typical_stats():
	s=['strength', 'dexterity', 'constitution', 'intelligence', 'wisdom', 'charisma']
	while True:
		r={j: sum([roll('d6') for i in range(3)]) for j in s}
		if sum([v for k, v in r.items()])>=60: break
	return r
