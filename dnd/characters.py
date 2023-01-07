from . import base, classes, races, names

def create_random_character():
    #stats
    stats=base.random_heroic_stats()
    #race
    race=base.pick_weighted({
        races.Human: 7,
        races.HighElf: 2,
        races.WoodElf: 3,
        races.HillDwarf: 3,
        races.MountainDwarf: 4,
        races.Dragonborn: 2,
        races.RockGnome: 2,
        races.ForestGnome: 3,
        races.Tiefling: 1,
        races.HalfOrc: 1,
    })
    #class
    stat_to_class={
        'strength': {
            classes.Fighter: 6,
            classes.Ranger: 2,
            classes.Paladin: 2,
            classes.Barbarian: 1,
        },
        'dexterity': {
            classes.Rogue: 7,
            classes.Ranger: 2,
            classes.Fighter: 1,
        },
        'intelligence': {
            classes.Wizard: 10,
        },
        'wisdom': {
            classes.Cleric: 5,
            classes.Druid: 3,
            classes.Ranger: 2,
        },
        'charisma': {
            classes.Sorcerer: 4,
            classes.Bard: 3,
            classes.Paladin: 2,
            classes.Warlock: 1,
        },
    }
    max_stat=max(
        [
            (k, v)
            for k, v
            in stats.items()
            if k!='constitution'
        ],
        key=lambda x: x[1]
    )[0]
    c=base.pick_weighted(stat_to_class[max_stat])
    #create
    result=base.create_character(stats, race, {c: 1})
    #physical
    result.gender=base.pick('mf')
    result.age=base.rn(result.choices['age'])
    result.height=base.rn(tuple(i*12 for i in result.choices['height']))/12
    result.weight=base.rn(result.choices['weight'])
    #skin
    if isinstance(result, races.Dragonborn):
        result.skin_color=base.pick([
            'black', 'blue', 'brass', 'bronze', 'copper', 'gold', 'green',
            'red', 'silver', 'white',
        ])
    elif isinstance(result, races.Tiefling):
        result.skin_color=base.pick([
            'red', 'orange', 'yellow', 'green', 'blue', 'purple',
            'black', 'brown', 'tan', 'white',
        ])
    elif isinstance(result, races.HalfOrc):
        result.skin_color = base.pick(['grey', 'green'])
    else:
        result.skin_color=base.pick([
            'black', 'brown', 'tan', 'white',
        ])
    #hair
    if isinstance(result, races.Dragonborn): result.hair_color=None
    elif isinstance(result, races.Tiefling):
        if base.maybe():
            result.hair_color=base.pick([
                'black', 'brown', 'blonde', 'auburn', 'grey', 'white'
            ])
        elif base.maybe():
            result.hair_color=result.skin_color
        else:
            result.hair_color=base.pick([
                'red', 'orange', 'yellow', 'green', 'blue', 'purple',
            ])
    elif isinstance(result, classes.Druid) and base.maybe():
        result.hair_color=base.pick(['green', 'brown', 'auburn'])
    else:
        result.hair_color=base.pick([
            'black', 'brown', 'blonde', 'auburn', 'grey', 'white'
        ])
    #eye
    def is_a(x, cs): return any(isinstance(x, i) for i in cs)
    if isinstance(result, classes.Druid) and base.maybe():
        result.eye_color=base.pick(['green', 'brown'])
    elif is_a(result, [races.Dragonborn, races.Tiefling, classes.Warlock]) or base.maybe(10):
        result.eye_color=base.pick([
            'red', 'orange', 'yellow', 'green', 'blue', 'purple',
            'brown',
        ])
    else:
        result.eye_color=base.pick_weighted({
            'brown': 30, 'blue': 10, 'green': 5
        })
    #name
    if isinstance(result, races.Human): result.name=names.human(result.gender)
    elif isinstance(result, races.Elf): result.name=names.elf()
    elif isinstance(result, races.Dwarf): result.name=names.dwarf(result.gender)
    elif isinstance(result, races.Dragonborn): result.name=names.dragonborn()
    elif isinstance(result, races.Gnome): result.name=names.gnome()
    elif isinstance(result, races.Tiefling): result.name=names.tiefling(result.gender)
    elif isinstance(result, races.HalfOrc): result.name=names.half_orc(result.gender)
    #return
    return result

def create_random_character_with_constraints(constraints):
    while True:
        c = create_random_character()
        if all(i(c) for i in constraints):
            return c

class constraints:
    def has_class(class_):
        return lambda character: class_.lower() in [name.lower() for name, lvl in character.classes]

    def class_isnt(classes):
        def cond(character):
            for i in classes:
                if i in [name.lower() for name, lvl in character.classes]:
                    return False
            return True
        return cond

    def race(race):
        return lambda character: isinstance(character, race)

    def race_isnt(races):
        def cond(character):
            for i in races:
                if isinstance(character, i):
                    return False
            return True
        return cond
