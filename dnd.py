try: input=raw_input
except: pass

def roll(request):
	import random, re
	match=re.match(r'([0-9]+)?d([0-9]+)([+-][0-9]+)?', request)
	if match:
		dice, sides, bonus=[int(match.groups()[i] or [1, None, 0][i]) for i in range(3)]
		rolls=[random.randint(1, sides) for i in range(dice)]
		return (sum(rolls)+bonus, rolls)
	return None

def interact():
	while(True):
		request=input()
		if request=='q': break
		r=roll(request)
		if r: print(r)
