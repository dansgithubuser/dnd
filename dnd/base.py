from items import items
from skills import skills

def parse_roll_request(request):
	import re
	match=re.match(r'([0-9]+)?d([0-9]+)([+-][0-9]+)?', request)
	if match: return [int(match.groups()[i] or [1, None, 0][i]) for i in range(3)]
	return [None, None, None]

def roll(request):
	import random
	dice, sides, bonus=parse_roll_request(request)
	if sides:
		rolls=[random.randint(1, sides) for i in range(dice)]
		print(rolls)
		return sum(rolls)+bonus
	return None

def d20(vantage=0):
	r=[roll('d20') for i in range(2)]
	if vantage<0 and r[1]<r[0]: return r[1]
	if vantage>0 and r[1]>r[0]: return r[1]
	return r[0]

def modifier(stat): return (stat-10)//2

class Entity:
	def show(self):
		import pprint
		pprint.pprint(vars(self))

	def roll_stats(self):
		self.max_hp=roll(self.hit_dice)
		self.hp=self.max_hp

	def roll_initiative(self):
		return d20()+modifier(self.dexterity)

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
		return result

	def damage(self, amount):
		old_hp==self.hp
		self.hp-=amount
		if old_hp>=max_hp>self.hp: print('bloodied')
		if self.hp<0: print('unconscious')

	def saving_throw(self, type):
		return d20()+modifier(getattr(self, type))+self.proficiency(type+'_saving_throw')

	def check(self, skill):
		r=d20(-1 if skill in self.disadvantages() else 0)
		return r+modifier(getattr(self, skills[skill]))+self.proficiency(skill)

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
