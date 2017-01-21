try: input=raw_input
except: pass

from base import *
import backgrounds, classes, creatures, items, races, skills

def interact():
	while(True):
		request=input()
		if request=='q': break
		r=roll(request)
		if r: print(r)
