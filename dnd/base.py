import backgrounds, classes, items, skills, spells

import math, random

log=False
placed_entities=set()

def rn(m): return random.randint(0, m-1)
def maybe(unlikeliness=2): return not rn(unlikeliness)
def swap(list, i, j): x=list[i]; list[i]=list[j]; list[j]=x

def pick(list, n=1):
	if n==1: return list[rn(len(list))]
	import copy
	list=copy.deepcopy(list)
	result=[]
	for i in range(n):
		j=rn(len(list))
		result.append(list[j])
		del list[j]
	return result

def timestamp(ambiguous=True):
	import datetime
	format='{:%Y-%m'
	if not ambiguous: format+='-%b'
	format+='-%d %H:%M:%S.%f}'
	return format.format(datetime.datetime.now()).lower()

def key(x, default, *indices):
	for i in indices:
		if type(x)==dict and i in x: x=x[i]
		elif type(i)==str and hasattr(x, i): x=getattr(x, i)
		else: return default
	return x

def get(x, condition):
	for i in x:
		if condition(i): return i
	return None

def split_roll_request(request): return request.split('+')

def split_type(request):
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
	def __init__(self, critical_hit=20, critical_miss=1):
		self.critical=0
		self.critical_hit=critical_hit
		self.critical_miss=critical_miss

	def __call__(self, sides, roll):
		if roll[0]<=self.critical_miss: self.critical=-1
		if roll[0]>=self.critical_hit : self.critical= 1
		return typical_roll(sides, roll, self.critical_hit, self.critical_miss)

def roll(request, vantage=0, on_roll=typical_roll):
	print(request)
	if vantage>0: print('with advantage')
	if vantage<0: print('with disadvantage')
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
		print(x)
		return x
	def total(x): return sum([sum(i[1]) for i in x])
	a=inner(request, vantage)
	if vantage:
		b=inner(request, vantage)
		if vantage<0 and total(b)<total(a): a=b
		if vantage>0 and total(b)>total(a): a=b
	for i in a:
		if 'd' in i[0]: i[1]=on_roll(dice_sides_type(i[0])[1], i[1])
	import collections
	x=collections.defaultdict(int)
	t=''
	for i in range(len(a)-1, -1, -1):
		y=split_type(a[i][0])
		if y: t=y
		x[t]+=sum(a[i][1])
	if len(x)==1 and not x.items()[0][0]: return x.items()[0][1]
	return x

def modifier(stat): return (stat-10)//2

class Entity:
	def __getattr__(self, attr):
		if attr=='str': return self.strength
		if attr=='dex': return self.dexterity
		if attr=='con': return self.constitution
		if attr=='int': return self.intelligence
		if attr=='wis': return self.wisdom
		if attr=='cha': return self.charisma
		if attr=='ac': return self.armor_class()
		raise AttributeError

	def __setattr__(self, attr, value):
		if log:
			with open('log.txt', 'a') as file: file.write('{} {} {}={}\n'.format(
				timestamp(),
				key(self, '{} {}'.format(self.__class__, hex(id(self))), 'name'),
				attr,
				value
			))
		self.__dict__[attr]=value

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
		x=pprint.pformat(sorted(vars(self).items()+separators+derived, key=divine_key))
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
			method=key(self, '', 'attacks', 0)
			method=[i for i in key(self, [], 'wearing') if 'weapon' in key(items.items, '', i, 'type')][0]
		print(method)
		if method=='unarmed': damage='1 BLUDGEONING'
		elif method in items.items:
			if method not in self.wearing: print('not wearing')
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

	def cast(self, spell, origin=None):
		if spell not in spells.spells:
			raise Exception('no such spell "{}"'.format(spell))
		if origin==None: origin=(self.x, self.y, self.z)
		entities=spells.get_affected(spell, origin, placed_entities)
		spell=spells.spells[spell]
		damage=roll(spell['damage'])
		if 'save' in spell: dc, type=number_and_type(spell['save'])
		for i in entities:
			x=damage
			if 'save' in spell and i.check(type.lower())>=dc: x=spell['save_effect'](damage)
			i.damage(x)

	def proficiency(self, what):
		if what not in key(self, [], 'proficiencies'): return 0
		return key(self, 2, 'proficiency_bonus')

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
			result+=items.items[i].get('armor_class', 0)
			x=items.items[i].get('type', '')
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
		old_hp=self.hp
		if type(points)==int: self.hp-=points
		else:
			for t, p in points.items():
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
			if   type(i)==dict: s, m=i.items()[0]
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

class Group:
	def __init__(self, entities): self.entities=entities

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

def create_character(stats, race, classes_, background=backgrounds.Generic):
	x='''class Character(race, {}, background):
		def __init__(self):
			self.strength={strength}
			self.dexterity={dexterity}
			self.constitution={constitution}
			self.intelligence={intelligence}
			self.wisdom={wisdom}
			self.charisma={charisma}
			race.__init__(self, new=True)
			for c, l in classes_.items(): getattr(classes, c).__init__(self, l, new=True)
			background.__init__(self, new=True)'''
	g={'race': race, 'classes_': classes_, 'classes': classes, 'background': background}
	exec(
		x.format(','.join(['classes.'+i for i in classes_.keys()]), **stats),
		g
	)
	return g['Character']()

def random_heroic_stats():
	s=['strength', 'dexterity', 'constitution', 'intelligence', 'wisdom', 'charisma']
	while True:
		r={j: sum(sorted([roll('d6') for i in range(4)])[1:]) for j in s}
		if sum([v for k, v in r.items()])>=72: break
	return r
