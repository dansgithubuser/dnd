try: input=raw_input
except: pass

def interact():
	import random, re
	while(True):
		request=input()
		if request=='q': break
		match=re.match(r'([0-9]+)?d([0-9]+)([+-][0-9]+)?', request)
		if match:
			dice, sides, bonus=[int(match.groups()[i] or [1, None, 0][i]) for i in range(3)]
			rolls=[random.randint(1, sides) for i in range(dice)]
			print(sum(rolls)+bonus, rolls)
