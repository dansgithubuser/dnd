import dnd

import collections
import pprint
import random

random.seed(0)

tribes = [
    'Cranberry',
    'Lake-elf',
    'Bowyer',
    'Lightfoot',
    'Sandelf',
    'Moonshadow',
    'Fawncrickets',
    'Mooserider',
]

tribe_names = {
    'Cranberry': 'Cranberry Tribe',
    'Lake-elf': 'Lake Pack',
    'Bowyer': 'Bowyers',
    'Lightfoot': 'Lightfoot',
    'Sandelf': 'Sandelves',
    'Moonshadow': 'Moonshadow',
    'Fawncrickets': 'Fawncrickets',
    'Mooserider': 'Mooserider',
}

jobs = {
    'Cranberry': [
        'gatherer',
        'winemaker',
        'beekeeper',
        'sailor',
        'musician',
    ],
    'Lake-elf': [
        'diver',
        'seaherbalist',
        'sculptor',
    ],
    'Bowyer': [
        'bowyer',
        'fletcher',
        'inkmaker',
        'papermaker',
        'librarian',
        'trader',
        'painter',
        'architect',
    ],
    'Lightfoot': [
        'gatherer',
        'sailor',
        'novelist',
        'dancer',
    ],
    'Sandelf': [
        'shaman',
        'mycologist',
        'gatherer',
        'sculptor',
    ],
    'Moonshadow': [
        'astronomer',
        'glassmaker',
        'trader',
        'musician',
    ],
    'Fawncrickets': [
        'herder',
        'gatherers',
        'musicians',
        'dancers',
    ],
    'Mooserider': [
        'gatherer',
        'musician',
        'dancer',
    ],
}

lineage_kwargs = dict(
    longevity=750,
    reproductive_age_range=range(100, 650),
    reproductive_cooldown=50,
    overpopulation_avoidance=0.99,
    disaster_avoidance=0.99,
    base_death_rate=1e-4,
    max_population=200,
    overpopulated_death_rate=1e-3,
    max_genetic_similarity=0.2,
    inbreediness=0.1,
    disaster_frequency=0.01,
    disaster_severity=0.1,
    disaster_longevity=4,
)

tribes = {
    tribe: dnd.lineage.create(
        initial_population=200,
        years=range(750),
        name_generator=lambda **kwargs: dnd.names.elf() + ' ' + tribe,
        **lineage_kwargs,
    )
    for tribe in tribes
}

year = 750

while year < 2232:
    # progress
    years = random.randint(8, 16)
    if year + years > 2232:
        years = 2232 - year
    tribes = {
        tribe_name: dnd.lineage.create(
            initial_population=tribe_lineage,
            years=range(year, year+years),
            name_generator=lambda **kwargs: dnd.names.elf() + ' ' + tribe_name,
            **lineage_kwargs,
        )
        for tribe_name, tribe_lineage in tribes.items()
    }
    year += years
    # exchange elves
    for _ in range(random.randint(1, 3)):
        a = random.choice(list(tribes.keys()))
        b = random.choice(list(tribes.keys()))
        if a == b: continue
        n = random.randint(1, 10)
        print(f'{n} elves from {a} immigrate to {b}')
        for _ in range(n):
            immigrant = random.choice([i for i in tribes[a] if i.alive()])
            tribes[a].remove(immigrant)
            tribes[b].append(immigrant)
            if not hasattr(immigrant, 'immigrations'):
                immigrant.immigrations = []
            immigrant.immigrations.append({'year': year, 'destination': tribe_names[b]})

total_lineage = []
for tribe in tribes.values():
    total_lineage.extend(tribe)

erenn = total_lineage[4170]
erenn.name = erenn.name.replace('Eal', 'Erenn')

dnd.lineage.plot(total_lineage, 750)
immigration_distribution = collections.defaultdict(int)
for person in total_lineage:
    immigrations = len(getattr(person, 'immigrations', []))
    immigration_distribution[immigrations] += 1
import dansplotcore as dpc
dpc.plot(dict(immigration_distribution), primitive=dpc.p.Line())

infant_deaths = 0
for person in total_lineage:
    if not person.alive():
        if person.death_date - person.birth_date <= 1:
            infant_deaths += 1
print('infant deaths:', infant_deaths)

for person in total_lineage:
    tribe = person.name.split()[-1]
    if 2232 - person.birth_date > 100:
        person.job = random.choice(jobs[tribe])
    else:
        person.job = '-'

person_html_template='''\
{name} ({gender})<br>
vocation: {job}<br>
born: {birth_date}<br>
died: {death_date}<br>
mother: <a href="{mother_i}.html">{mother_name}</a><br>
father: <a href="{father_i}.html">{father_name}</a><br>
<br>
children:<br>
{children}<br>
'''

child_html_template='''\
<a href="{i}.html">{name} ({birth_date})</a><br>
'''

immigration_html_template='''\
immigrated to {destination} in {year}<br>
'''

for i, person in enumerate(total_lineage):
    person.i = i
for person in total_lineage:
    with open(f'../../merennora/lineage/{person.i}.html', 'w') as f:
        children = ''.join([
            child_html_template.format(name=child.name, i=child.i, birth_date=child.birth_date)
            for child in person.children
        ])
        f.write(person_html_template.format(
            name=person.name,
            job=person.job,
            gender=person.gender.upper(),
            birth_date=person.birth_date,
            death_date=person.death_date or '-',
            mother_name=person.mother.name if person.mother else '-',
            mother_i=person.mother.i if person.mother else '-',
            father_name=person.father.name if person.father else '-',
            father_i=person.father.i if person.father else '-',
            children=children or '-',
        ))
        for immigration in getattr(person, 'immigrations', []):
            f.write(immigration_html_template.format(**immigration))

female_partners = collections.defaultdict(list)
male_partners = collections.defaultdict(set)
for person in total_lineage:
    if not person.mother or not person.father:
        continue
    female_partners[person.mother.i].append((person.birth_date, person.father))
    male_partners[person.father.i].add(person.mother.i)
for female, partners in female_partners.items():
    if len(partners) != 2: continue
    if any([not partner.alive() for _, partner in partners]): continue
    if all([len(male_partners[partner.i]) != 1 for _, partner in partners]): continue
    print(total_lineage[female], female)
    for date, partner in partners:
        print('\t', date, partner, partner.i)
