#!/usr/bin/env python

import glob, json, os, re

spells={}

for spell_file_name in glob.glob(os.path.join('open5e', 'source', 'Spellcasting', 'spells_a-z', '*', '*')):
	if spell_file_name.endswith('index.rst'): continue
	with open(spell_file_name) as spell_file: lines=spell_file.readlines()
	spell={}
	spell_name=None
	category_name=None
	category_contents=''
	def add_category():
		spell[category_name]=re.sub(r'(?<!\n)\n(?!(\n|-  ))', ' ', category_contents.strip())
	for i in range(len(lines)):
		if not spell_name and lines[i].startswith('.'): spell_name=re.search(':(.*):', lines[i]).group(1)
		elif lines[i].startswith('^'):
			x=lines[i-1]
			if 'cantrip' in x:
				level=0
				school=x.split()[0].lower()
				other=[]
			else:
				level=int(x.split()[0][0])
				school=x.split()[1]
				other=x.split()[2:]
			assert 0<=level<=9
			assert school in ['abjuration', 'conjuration', 'divination', 'enchantment', 'evocation', 'illusion', 'necromancy', 'transmutation']
			spell['level']=level
			spell['school']=' '.join([school]+other)
		elif lines[i].startswith('*'):
			if category_name: add_category()
			x, _, y=re.match(r'\*\*(.*).\*\*( (.*))?', lines[i], re.DOTALL).groups()
			category_name=x.lower()
			category_contents=y if y else ''
		elif category_name=='duration' and not lines[i].strip():
			add_category()
			category_name='description'
			category_contents=''
		elif category_name:
			category_contents+=lines[i]
	add_category()
	spells[spell_name]=spell
for class_file_name in glob.glob(os.path.join('open5e', 'source', 'Spellcasting', 'by-class', '*')):
	with open(class_file_name) as class_file: lines=class_file.readlines()
	for line in lines:
		m=re.match(r'- :ref:`(.*)`', line)
		if not m: continue
		g=m.group(1)
		if g.startswith('srd:'):
			spell_name=g[4:]
			if spell_name not in spells: raise Exception('no such spell "{}"'.format(spell_name))
			spell=spells[spell_name]
			if 'classes' not in spell: spell['classes']=[]
			spell['classes'].append(os.path.split(class_file_name)[-1].split('.')[0])
		else: raise Exception('unknown spell book')

with open('spells.json', 'w') as file: file.write(json.dumps(spells))

