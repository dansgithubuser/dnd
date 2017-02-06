from items import items
from skills import skills

def split_roll_request(request): return request.split('+')

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
		import random
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
	return total(a)

def modifier(stat): return (stat-10)//2

class Entity:
	def __getattr__(self, attr):
		aliases={
			'str': self.strength,
			'dex': self.dexterity,
			'con': self.constitution,
			'int': self.intelligence,
			'wis': self.wisdom,
			'cha': self.charisma,
			'ac': self.armor_class,
		}
		if attr in aliases:
			x=aliases[attr]
			return x() if callable(x) else x
		raise AttributeError

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

	def attack(self, method=None, vantage=0, critical_hit=20):
		#method
		attack='d20'
		stat_mod=modifier(self.strength)
		if method=='unarmed': damage='1'
		elif method in items:
			if method not in self.wearing: print('not wearing')
			damage=items[method]['damage']
			if 'finesse' in items[method]['properties']:
				stat_mod=max(stat_mod, modifier(self.dexterity))
			elif items[method]['type']=='ranged_weapon':
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
		p=0
		if hasattr(self, 'proficiencies') and method in self.proficiencies: p=self.proficiency_bonus
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
		#
		self.print_notes('attack')
		return (a, d)

	def full_attack(self, vantage=0):
		if hasattr(self, 'attacks'):
			for i in self.attacks:
				print(i[0])
				print('----> {}'.format(self.attack(i[0], vantage)))
		if hasattr(self, 'wearing'):
			for i in self.wearing:
				if i in items and 'weapon' in items[i]['type']:
					print(i)
					print('-----> {}'.format(self.attack(i)))

	def proficiency(self, what):
		if not hasattr(self, 'proficiencies'): return 0
		if what not in self.proficiencies: return 0
		if not hasattr(self, 'proficiency_bonus'): return 2
		return self.proficiency_bonus

	def disadvantages(self):
		result=[]
		if hasattr(self, 'wearing'):
			for i in self.wearing:
				result+=items[i].get('disadvantages', [])
				if 'armor' in i or 'shield' in i and i not in self.proficiencies:
					result+=['unproficient_armor']
		return result

	def armor_class(self):
		result=0
		armor_type=''
		shield=False
		if hasattr(self, 'wearing'):
			for i in self.wearing:
				result+=items[i].get('armor_class', 0)
				x=items[i].get('type', '')
				if 'armor' in x: armor_type=x
				if 'shield' in x: shield=True
		if not shield and not armor_type: result=10
		if 'heavy' in armor_type: pass
		elif 'medium' in armor_type: result+=min(modifier(self.dexterity), 2)
		else: result+=modifier(self.dexterity)
		if hasattr(self, 'natural_armor'): result+=self.natural_armor
		self.print_notes('armor_class')
		return result

	def damage(self, amount):
		old_hp==self.hp
		self.hp-=amount
		if old_hp>=max_hp>self.hp: print('bloodied')
		if self.hp<0: print('unconscious')

	def saving_throw(self, type, vantage=0):
		return roll('d20+{}+{}'.format(
			modifier(getattr(self, type)),
			self.proficiency(type+'_saving_throw'),
		), vantage)

	def check(self, skill, vantage=0):
		if skill in self.disadvantages(): vantage-=1
		return roll('d20+{}+{}'.format(
			modifier(getattr(self, skills[skill])),
			self.proficiency(skill),
		), vantage)

	def passive_perception(self):
		x=0
		if 'perception' in self.proficiencies: x=self.proficiency_bonus
		return 10+modifier(self.wisdom)+x

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
