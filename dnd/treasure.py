from .base import roll
from .spells import spells_by_level

from random import choice

def r(request): return roll(request, quiet=True)

def individual_0_4():
    p = r('d100')
    if p <= 30:
        return [
            ('cp', r('5d6')),
        ]
    elif p <= 60:
        return [
            ('sp', r('4d6')),
        ]
    elif p <= 70:
        return [
            ('ep', r('3d6')),
        ]
    elif p <= 95:
        return [
            ('gp', r('3d6')),
        ]
    else:
        return [
            ('pp', r('1d6')),
        ]

def individual_5_10():
    p = r('d100')
    if p <= 30:
        return [
            ('cp', r('4d6') * 100),
            ('ep', r('1d6') * 10),
        ]
    elif p <= 60:
        return [
            ('sp', r('6d6') * 10),
            ('gp', r('2d6') * 10),
        ]
    elif p <= 70:
        return [
            ('ep', r('3d6') * 10),
            ('gp', r('2d6') * 10),
        ]
    elif p <= 95:
        return [
            ('gp', r('4d6') * 10),
        ]
    else:
        return [
            ('gp', r('2d6') * 10),
            ('pp', r('3d6') * 10),
        ]

def individual_11_16():
    p = r('d100')
    if p <= 20:
        return [
            ('sp', r('4d6') * 100),
            ('gp', r('1d6') * 100),
        ]
    elif p <= 35:
        return [
            ('ep', r('1d6') * 100),
            ('gp', r('1d6') * 100),
        ]
    elif p <= 75:
        return [
            ('gp', r('2d6') * 100),
            ('pp', r('1d6') * 10),
        ]
    else:
        return [
            ('gp', r('2d6') * 100),
            ('pp', r('2d6') * 10),
        ]

def individual_17():
    p = r('d100')
    if p <= 15:
        return [
            ('ep', r('2d6') * 1000),
            ('gp', r('8d6') * 100),
        ]
    elif p <= 55:
        return [
            ('gp', r('1d6') * 1000),
            ('pp', r('1d6') * 100),
        ]
    else:
        return [
            ('gp', r('1d6') * 100),
            ('pp', r('2d6') * 100),
        ]

def hoard_0_4():
    hoard = [
        ('cp', r('6d6') * 100),
        ('sp', r('3d6') * 100),
        ('gp', r('2d6') * 10),
    ]
    p = r('d100')
    if p <= 6:
        pass
    elif p <= 16:
        hoard.append(('10 gp gem', r('2d6')))
    elif p <= 26:
        hoard.append(('25 gp art', r('2d4')))
    elif p <= 36:
        hoard.append(('50 gp gem', r('2d6')))
    elif p <= 44:
        hoard.append(('10 gp gem', r('2d6')))
        for i in range(r('1d6')):
            hoard.append(magic_item_table_a())
    elif p <= 52:
        hoard.append(('25 gp art', r('2d4')))
        for i in range(r('1d6')):
            hoard.append(magic_item_table_a())
    elif p <= 60:
        hoard.append(('50 gp gem', r('2d6')))
        for i in range(r('1d6')):
            hoard.append(magic_item_table_a())
    elif p <= 65:
        hoard.append(('10 gp gem', r('2d6')))
        for i in range(r('1d4')):
            hoard.append(magic_item_table_b())
    elif p <= 70:
        hoard.append(('25 gp art', r('2d4')))
        for i in range(r('1d4')):
            hoard.append(magic_item_table_b())
    elif p <= 75:
        hoard.append(('50 gp gem', r('2d6')))
        for i in range(r('1d4')):
            hoard.append(magic_item_table_b())
    elif p <= 78:
        hoard.append(('10 gp gem', r('2d6')))
        for i in range(r('1d4')):
            hoard.append(magic_item_table_c())
    elif p <= 80:
        hoard.append(('25 gp art', r('2d4')))
        for i in range(r('1d4')):
            hoard.append(magic_item_table_c())
    elif p <= 85:
        hoard.append(('50 gp gem', r('2d6')))
        for i in range(r('1d4')):
            hoard.append(magic_item_table_c())
    elif p <= 92:
        hoard.append(('25 gp art', r('2d4')))
        for i in range(r('1d4')):
            hoard.append(magic_item_table_f())
    elif p <= 97:
        hoard.append(('50 gp gem', r('2d6')))
        for i in range(r('1d4')):
            hoard.append(magic_item_table_f())
    elif p <= 99:
        hoard.append(('25 gp art', r('2d4')))
        for i in range(r('1d4')):
            hoard.append(magic_item_table_g())
    elif p <= 100:
        hoard.append(('50 gp gem', r('2d6')))
        for i in range(r('1d4')):
            hoard.append(magic_item_table_g())
    return hoard

def hoard_5_10():
    hoard = [
        ('cp', r('2d6') * 100),
        ('sp', r('2d6') * 1000),
        ('gp', r('6d6') * 100),
        ('pp', r('3d6') * 10),
    ]
    p = r('d100')
    if p <= 4:
        pass
    elif p <= 10:
        hoard.append(('25 gp art', r('2d4')))
    elif p <= 16:
        hoard.append(('50 gp gem', r('3d6')))
    elif p <= 22:
        hoard.append(('100 gp gem', r('3d6')))
    elif p <= 28:
        hoard.append(('250 gp art', r('2d4')))
    elif p <= 32:
        hoard.append(('25 gp art', r('2d4')))
        for i in range(r('1d6')):
            hoard.append(magic_item_table_a())
    elif p <= 36:
        hoard.append(('50 gp gem', r('3d6')))
        for i in range(r('1d6')):
            hoard.append(magic_item_table_a())
    elif p <= 40:
        hoard.append(('100 gp gem', r('3d6')))
        for i in range(r('1d6')):
            hoard.append(magic_item_table_a())
    elif p <= 44:
        hoard.append(('250 gp art', r('2d4')))
        for i in range(r('1d6')):
            hoard.append(magic_item_table_a())
    elif p <= 49:
        hoard.append(('25 gp art', r('2d4')))
        for i in range(r('1d4')):
            hoard.append(magic_item_table_b())
    elif p <= 54:
        hoard.append(('50 gp gem', r('3d6')))
        for i in range(r('1d4')):
            hoard.append(magic_item_table_b())
    elif p <= 59:
        hoard.append(('100 gp gem', r('3d6')))
        for i in range(r('1d4')):
            hoard.append(magic_item_table_b())
    elif p <= 63:
        hoard.append(('250 gp art', r('2d4')))
        for i in range(r('1d4')):
            hoard.append(magic_item_table_b())
    elif p <= 66:
        hoard.append(('25 gp art', r('2d4')))
        for i in range(r('1d4')):
            hoard.append(magic_item_table_c())
    elif p <= 69:
        hoard.append(('50 gp gem', r('3d6')))
        for i in range(r('1d4')):
            hoard.append(magic_item_table_c())
    elif p <= 72:
        hoard.append(('100 gp gem', r('3d6')))
        for i in range(r('1d4')):
            hoard.append(magic_item_table_c())
    elif p <= 74:
        hoard.append(('250 gp art', r('2d4')))
        for i in range(r('1d4')):
            hoard.append(magic_item_table_c())
    elif p <= 76:
        hoard.append(('25 gp art', r('2d4')))
        hoard.append(magic_item_table_d())
    elif p <= 78:
        hoard.append(('50 gp gem', r('3d6')))
        hoard.append(magic_item_table_d())
    elif p <= 79:
        hoard.append(('100 gp gem', r('3d6')))
        hoard.append(magic_item_table_d())
    elif p <= 80:
        hoard.append(('250 gp art', r('2d4')))
        hoard.append(magic_item_table_d())
    elif p <= 84:
        hoard.append(('25 gp art', r('2d4')))
        for i in range(r('1d4')):
            hoard.append(magic_item_table_f())
    elif p <= 88:
        hoard.append(('50 gp gem', r('3d6')))
        for i in range(r('1d4')):
            hoard.append(magic_item_table_f())
    elif p <= 91:
        hoard.append(('100 gp gem', r('3d6')))
        for i in range(r('1d4')):
            hoard.append(magic_item_table_f())
    elif p <= 94:
        hoard.append(('250 gp art', r('2d4')))
        for i in range(r('1d4')):
            hoard.append(magic_item_table_f())
    elif p <= 96:
        hoard.append(('100 gp gem', r('3d6')))
        for i in range(r('1d4')):
            hoard.append(magic_item_table_g())
    elif p <= 98:
        hoard.append(('250 gp art', r('2d4')))
        for i in range(r('1d4')):
            hoard.append(magic_item_table_g())
    elif p <= 99:
        hoard.append(('100 gp gem', r('3d6')))
        hoard.append(magic_item_table_h())
    elif p <= 100:
        hoard.append(('250 gp art', r('2d4')))
        hoard.append(magic_item_table_h())
    return hoard

def hoard_11_16():
    hoard = [
        ('gp', r('4d6') * 1000),
        ('pp', r('5d6') * 100),
    ]
    p = r('d100')
    if p <= 3:
        pass
    elif p <= 6:
        hoard.append(('250 gp art', r('2d4')))
    elif p <= 9:
        hoard.append(('750 gp art', r('2d4')))
    elif p <= 12:
        hoard.append(('500 gp gem', r('3d6')))
    elif p <= 15:
        hoard.append(('1000 gp gem', r('3d6')))
    elif p <= 19:
        hoard.append(('250 gp art', r('2d4')))
        for i in range(r('1d4')):
            hoard.append(magic_item_table_a())
        for i in range(r('1d6')):
            hoard.append(magic_item_table_b())
    elif p <= 23:
        hoard.append(('750 gp art', r('2d4')))
        for i in range(r('1d4')):
            hoard.append(magic_item_table_a())
        for i in range(r('1d6')):
            hoard.append(magic_item_table_b())
    elif p <= 26:
        hoard.append(('500 gp gem', r('3d6')))
        for i in range(r('1d4')):
            hoard.append(magic_item_table_a())
        for i in range(r('1d6')):
            hoard.append(magic_item_table_b())
    elif p <= 29:
        hoard.append(('1000 gp gem', r('3d6')))
        for i in range(r('1d4')):
            hoard.append(magic_item_table_a())
        for i in range(r('1d6')):
            hoard.append(magic_item_table_b())
    elif p <= 35:
        hoard.append(('250 gp art', r('2d4')))
        for i in range(r('1d6')):
            hoard.append(magic_item_table_c())
    elif p <= 40:
        hoard.append(('750 gp art', r('2d4')))
        for i in range(r('1d6')):
            hoard.append(magic_item_table_c())
    elif p <= 45:
        hoard.append(('500 gp gem', r('3d6')))
        for i in range(r('1d6')):
            hoard.append(magic_item_table_c())
    elif p <= 50:
        hoard.append(('1000 gp gem', r('3d6')))
        for i in range(r('1d6')):
            hoard.append(magic_item_table_c())
    elif p <= 54:
        hoard.append(('250 gp art', r('2d4')))
        for i in range(r('1d4')):
            hoard.append(magic_item_table_d())
    elif p <= 58:
        hoard.append(('750 gp art', r('2d4')))
        for i in range(r('1d4')):
            hoard.append(magic_item_table_d())
    elif p <= 62:
        hoard.append(('500 gp gem', r('3d6')))
        for i in range(r('1d4')):
            hoard.append(magic_item_table_d())
    elif p <= 66:
        hoard.append(('1000 gp gem', r('3d6')))
        for i in range(r('1d4')):
            hoard.append(magic_item_table_d())
    elif p <= 68:
        hoard.append(('250 gp art', r('2d4')))
        hoard.append(magic_item_table_e())
    elif p <= 70:
        hoard.append(('750 gp art', r('2d4')))
        hoard.append(magic_item_table_e())
    elif p <= 72:
        hoard.append(('500 gp gem', r('3d6')))
        hoard.append(magic_item_table_e())
    elif p <= 74:
        hoard.append(('1000 gp gem', r('3d6')))
        hoard.append(magic_item_table_e())
    elif p <= 76:
        hoard.append(('250 gp art', r('2d4')))
        hoard.append(magic_item_table_f())
        for i in range(r('1d4')):
            hoard.append(magic_item_table_g())
    elif p <= 78:
        hoard.append(('750 gp art', r('2d4')))
        hoard.append(magic_item_table_f())
        for i in range(r('1d4')):
            hoard.append(magic_item_table_g())
    elif p <= 80:
        hoard.append(('500 gp gem', r('3d6')))
        hoard.append(magic_item_table_f())
        for i in range(r('1d4')):
            hoard.append(magic_item_table_g())
    elif p <= 82:
        hoard.append(('1000 gp gem', r('3d6')))
        hoard.append(magic_item_table_f())
        for i in range(r('1d4')):
            hoard.append(magic_item_table_g())
    elif p <= 85:
        hoard.append(('1000 gp gem', r('3d6')))
        for i in range(r('1d6')):
            hoard.append(magic_item_table_h())
    elif p <= 88:
        hoard.append(('250 gp art', r('2d4')))
        for i in range(r('1d4')):
            hoard.append(magic_item_table_h())
    elif p <= 90:
        hoard.append(('750 gp art', r('2d4')))
        for i in range(r('1d4')):
            hoard.append(magic_item_table_h())
    elif p <= 92:
        hoard.append(('500 gp gem', r('3d6')))
        for i in range(r('1d4')):
            hoard.append(magic_item_table_h())
    elif p <= 94:
        hoard.append(('250 gp art', r('2d4')))
        hoard.append(magic_item_table_i())
    elif p <= 96:
        hoard.append(('750 gp art', r('2d4')))
        hoard.append(magic_item_table_i())
    elif p <= 98:
        hoard.append(('500 gp gem', r('3d6')))
        hoard.append(magic_item_table_i())
    elif p <= 100:
        hoard.append(('1000 gp gem', r('3d6')))
        hoard.append(magic_item_table_i())
    return hoard

def hoard_17():
    hoard = [
        ('gp', r('12d6') * 1000),
        ('pp', r('8d6') * 1000),
    ]
    p = r('d100')
    if p <= 2:
        pass
    elif p <= 5:
        hoard.append(('1000 gp gem', r('3d6')))
        for i in range(r('1d8')):
            hoard.append(magic_item_table_c())
    elif p <= 8:
        hoard.append(('2500 gp art', r('1d10')))
        for i in range(r('1d8')):
            hoard.append(magic_item_table_c())
    elif p <= 11:
        hoard.append(('7500 gp art', r('1d4')))
        for i in range(r('1d8')):
            hoard.append(magic_item_table_c())
    elif p <= 14:
        hoard.append(('5000 gp gem', r('1d8')))
        for i in range(r('1d8')):
            hoard.append(magic_item_table_c())
    elif p <= 22:
        hoard.append(('1000 gp gem', r('3d6')))
        for i in range(r('1d6')):
            hoard.append(magic_item_table_d())
    elif p <= 30:
        hoard.append(('2500 gp art', r('1d10')))
        for i in range(r('1d6')):
            hoard.append(magic_item_table_d())
    elif p <= 38:
        hoard.append(('7500 gp art', r('1d4')))
        for i in range(r('1d6')):
            hoard.append(magic_item_table_d())
    elif p <= 46:
        hoard.append(('5000 gp gem', r('1d8')))
        for i in range(r('1d6')):
            hoard.append(magic_item_table_d())
    elif p <= 52:
        hoard.append(('1000 gp gem', r('3d6')))
        for i in range(r('1d6')):
            hoard.append(magic_item_table_e())
    elif p <= 58:
        hoard.append(('2500 gp art', r('1d10')))
        for i in range(r('1d6')):
            hoard.append(magic_item_table_e())
    elif p <= 63:
        hoard.append(('7500 gp art', r('1d4')))
        for i in range(r('1d6')):
            hoard.append(magic_item_table_e())
    elif p <= 68:
        hoard.append(('5000 gp gem', r('1d8')))
        for i in range(r('1d6')):
            hoard.append(magic_item_table_e())
    elif p <= 69:
        hoard.append(('1000 gp gem', r('3d6')))
        for i in range(r('1d4')):
            hoard.append(magic_item_table_g())
    elif p <= 70:
        hoard.append(('2500 gp art', r('1d10')))
        for i in range(r('1d4')):
            hoard.append(magic_item_table_g())
    elif p <= 71:
        hoard.append(('7500 gp art', r('1d4')))
        for i in range(r('1d4')):
            hoard.append(magic_item_table_g())
    elif p <= 72:
        hoard.append(('5000 gp gem', r('1d8')))
        for i in range(r('1d4')):
            hoard.append(magic_item_table_g())
    elif p <= 74:
        hoard.append(('1000 gp gem', r('3d6')))
        for i in range(r('1d4')):
            hoard.append(magic_item_table_h())
    elif p <= 76:
        hoard.append(('2500 gp art', r('1d10')))
        for i in range(r('1d4')):
            hoard.append(magic_item_table_h())
    elif p <= 78:
        hoard.append(('7500 gp art', r('1d4')))
        for i in range(r('1d4')):
            hoard.append(magic_item_table_h())
    elif p <= 80:
        hoard.append(('5000 gp gem', r('1d8')))
        for i in range(r('1d4')):
            hoard.append(magic_item_table_h())
    elif p <= 85:
        hoard.append(('1000 gp gem', r('3d6')))
        for i in range(r('1d4')):
            hoard.append(magic_item_table_i())
    elif p <= 90:
        hoard.append(('2500 gp art', r('1d10')))
        for i in range(r('1d4')):
            hoard.append(magic_item_table_i())
    elif p <= 95:
        hoard.append(('7500 gp art', r('1d4')))
        for i in range(r('1d4')):
            hoard.append(magic_item_table_i())
    elif p <= 100:
        hoard.append(('5000 gp gem', r('1d8')))
        for i in range(r('1d4')):
            hoard.append(magic_item_table_i())
    return hoard

def scroll_spell(level):
    if level == 0:
        return choice(spells_by_level[0])
    return choice([spell for level in range(1, level+1) for spell in spells_by_level[level]])

def magic_item_table_a():
    p = r('d100')
    if p <= 50: return 'potion of healing'
    elif p <= 60: return 'spell scroll (cantrip): ' + scroll_spell(0)
    elif p <= 70: return 'potion of climbing'
    elif p <= 90: return 'spell scroll (1st level): ' + scroll_spell(1)
    elif p <= 94: return 'spell scroll (2nd level): ' + scroll_spell(2)
    elif p <= 98: return 'potion of healing (greater)'
    elif p <= 99: return 'bag of holding'
    elif p <= 100: return 'driftglobe'

def magic_item_table_b():
    p = r('d100')
    if p <= 15: return 'potion of healing (greater)'
    elif p <= 22: return 'potion of fire breath'
    elif p <= 29: return 'potion of resistance'
    elif p <= 34: return 'ammunition, +1'
    elif p <= 39: return 'potion of animal friendship'
    elif p <= 44: return 'potion of hill giant strength'
    elif p <= 49: return 'potion of growth'
    elif p <= 54: return 'potion of water breathing'
    elif p <= 59: return 'spell scroll (2nd level): ' + scroll_spell(2)
    elif p <= 64: return 'spell scroll (3rd level): ' + scroll_spell(3)
    elif p <= 67: return 'bag of holding'
    elif p <= 70: return "Keoghtom's ointment"
    elif p <= 73: return 'oil of slipperiness'
    elif p <= 75: return 'dust of disappearance'
    elif p <= 77: return 'dust of dryness'
    elif p <= 79: return 'dust of sneezing and choking'
    elif p <= 81: return 'elemental gem'
    elif p <= 83: return 'philter of love'
    elif p <= 84: return 'alchemy jub'
    elif p <= 85: return 'cap of water breathing'
    elif p <= 86: return 'cloak of the manta ray'
    elif p <= 87: return 'driftglobe'
    elif p <= 88: return 'goggles of night'
    elif p <= 89: return 'helm of comprehending languages'
    elif p <= 90: return 'immovable rod'
    elif p <= 91: return 'lantern of revealing'
    elif p <= 92: return "mariner's armor"
    elif p <= 93: return 'mithral armor'
    elif p <= 94: return 'potion of poison'
    elif p <= 95: return 'ring of swimming'
    elif p <= 96: return 'robe of useful items'
    elif p <= 97: return 'rope of climbing'
    elif p <= 98: return 'saddle of the cavalier'
    elif p <= 99: return 'wand of magic detection'
    elif p <= 100: return 'wand of secrets'

def magic_item_table_c():
    p = r('d100')
    if p <= 15: return 'potion of healing (superior)'
    elif p <= 22: return 'spell scroll (4th level): ' + scroll_spell(4)
    elif p <= 27: return 'ammunition, +2'
    elif p <= 32: return 'potion of clairvoyance'
    elif p <= 37: return 'potion of diminution'
    elif p <= 42: return 'potion of gaseous form'
    elif p <= 47: return 'potion of frost giant strength'
    elif p <= 52: return 'potion of stone giant strength'
    elif p <= 57: return 'potion of heroism'
    elif p <= 62: return 'potion of invulnerability'
    elif p <= 67: return 'potion of mind reading'
    elif p <= 72: return 'spell scroll (5th level): ' + scroll_spell(5)
    elif p <= 75: return 'elixir of health'
    elif p <= 78: return 'oil of etherealness'
    elif p <= 81: return 'potion of fire giant strength'
    elif p <= 84: return "Quaal's feather token"
    elif p <= 87: return 'scroll of protection'
    elif p <= 89: return 'bag of beans'
    elif p <= 91: return 'bead of force'
    elif p <= 92: return 'chime of opening'
    elif p <= 93: return 'decanter of endless water'
    elif p <= 94: return 'eyes of minute seeing'
    elif p <= 95: return 'folding boat'
    elif p <= 96: return "Heward's handy haversack"
    elif p <= 97: return 'horseshoes of speed'
    elif p <= 98: return 'necklace of fireballs'
    elif p <= 99: return 'periapt of health'
    elif p <= 100: return 'sending stones'

def magic_item_table_d():
    p = r('d100')
    if p <= 20: return 'potion of healing (supreme)'
    elif p <= 30: return 'potion of invisibility'
    elif p <= 40: return 'potion of speed'
    elif p <= 50: return 'spell scroll (6th level): ' + scroll_spell(6)
    elif p <= 57: return 'spell scroll (7th level): ' + scroll_spell(7)
    elif p <= 62: return 'ammunition, +3'
    elif p <= 67: return 'oil of sharpness'
    elif p <= 72: return 'potion of flying'
    elif p <= 77: return 'potion of cloud giant strength'
    elif p <= 82: return 'potion of longevity'
    elif p <= 87: return 'potion of vitality'
    elif p <= 92: return 'spell scroll (8th level): ' + scroll_spell(8)
    elif p <= 95: return 'horseshoes of a zephyr'
    elif p <= 98: return "Nolzur's marvelous pigments"
    elif p <= 99: return 'bag of devouring'
    elif p <= 100: return 'portable hole'

def magic_item_table_e():
    p = r('d100')
    if p <= 30: return 'spell scroll (8th level): ' + scroll_spell(8)
    elif p <= 55: return 'potion of storm giant strength'
    elif p <= 70: return 'potion of healing (supreme)'
    elif p <= 85: return 'spell scroll (9th level): ' + scroll_spell(9)
    elif p <= 93: return 'universal solvent'
    elif p <= 98: return 'arrow of slaying'
    elif p <= 100: return 'sovereign glue'

def magic_item_table_f():
    p = r('d100')
    if p <= 15: return 'weapon, +1'
    elif p <= 18: return 'shield, +1'
    elif p <= 21: return 'sentinel shield'
    elif p <= 23: return 'amulet of proof against detection and location'
    elif p <= 25: return 'boots of elvenkind'
    elif p <= 27: return 'boots of striding and springing'
    elif p <= 29: return 'bracers of archery'
    elif p <= 31: return 'brooch of shielding'
    elif p <= 33: return 'broom of flying'
    elif p <= 35: return 'cloak of elvenkind'
    elif p <= 37: return 'cloak of protection'
    elif p <= 39: return 'gauntlets of ogre power'
    elif p <= 41: return 'hat of disguise'
    elif p <= 43: return 'javelin of lightning'
    elif p <= 45: return 'pearl of power'
    elif p <= 47: return 'rod of the pact keeper +1'
    elif p <= 49: return 'slippers of spider climbing'
    elif p <= 51: return 'staff of the adder'
    elif p <= 53: return 'staff of the python'
    elif p <= 55: return 'sword of vengeance'
    elif p <= 57: return 'trident of fish command'
    elif p <= 59: return 'wand of magic missiles'
    elif p <= 61: return 'wand of the war mage +1'
    elif p <= 63: return 'wand of web'
    elif p <= 65: return 'weapon of warning'
    elif p <= 66: return 'adamantine armor (chain mail)'
    elif p <= 67: return 'adamantine armor (chain shirt)'
    elif p <= 68: return 'adamantine armor (scale mail)'
    elif p <= 69: return 'bag of tricks (gray)'
    elif p <= 70: return 'bag of tricks (rust)'
    elif p <= 71: return 'bag of tricks (tan)'
    elif p <= 72: return 'boots of winterlands'
    elif p <= 73: return 'circlet of blasting'
    elif p <= 74: return 'deck of illusions'
    elif p <= 75: return 'eversmoking bottle'
    elif p <= 76: return 'eyes of charming'
    elif p <= 77: return 'eyes of the eagle'
    elif p <= 78: return 'figurine of wondrous power (silver raven)'
    elif p <= 79: return 'gem of brightness'
    elif p <= 80: return 'gloves of missile snaring'
    elif p <= 81: return 'gloves of swimming and climbing'
    elif p <= 82: return 'gloves of thievery'
    elif p <= 83: return 'headband of intellect'
    elif p <= 84: return 'helm of telepathy'
    elif p <= 85: return 'instrument of the bards (Doss lute)'
    elif p <= 86: return 'instrument of the bards (Fochlucan bandore)'
    elif p <= 87: return 'instrument of the bards (Mac-Fuimidh cittern)'
    elif p <= 88: return 'medallion of thoughts'
    elif p <= 89: return 'necklace of adaptation'
    elif p <= 90: return 'periapt of wound closure'
    elif p <= 91: return 'pipes of haunting'
    elif p <= 92: return 'pipes of the sewers'
    elif p <= 93: return 'ring of jumping'
    elif p <= 94: return 'ring of mind shielding'
    elif p <= 95: return 'ring of warmth'
    elif p <= 96: return 'ring of water walking'
    elif p <= 97: return 'quiver of Ehlonna'
    elif p <= 98: return 'stone of good luck (luckstone)'
    elif p <= 99: return 'wind fan'
    elif p <= 100: return 'winged boots'

def magic_item_table_g():
    p = r('d100')
    if p <= 11: return 'weapon, +2'
    elif p <= 14: return 'figurine of wondrous power'
    elif p <= 15: return 'adamantine armor (breastplate)'
    elif p <= 16: return 'adamantine armor (splint)'
    elif p <= 17: return 'amulet of health'
    elif p <= 18: return 'armor of vulnerability'
    elif p <= 19: return 'arrow-catching shield'
    elif p <= 20: return 'belt of dwarvenkind'
    elif p <= 21: return 'belt of hill giant strength'
    elif p <= 22: return 'berserker axe'
    elif p <= 23: return 'boots of levitation'
    elif p <= 24: return 'boots of speed'
    elif p <= 25: return 'bowl of commanding water elementals'
    elif p <= 26: return 'bracers of defense'
    elif p <= 27: return 'brazier of commanding fire elementals'
    elif p <= 28: return 'cape of the mountebank'
    elif p <= 29: return 'censer of controlling air elementals'
    elif p <= 30: return 'armor, +1 chain mail'
    elif p <= 31: return 'armor of resistance (chain mail)'
    elif p <= 32: return 'armor, +1 chain shirt'
    elif p <= 33: return 'armor of resistance (chain shirt)'
    elif p <= 34: return 'cloak of displacement'
    elif p <= 35: return 'cloak of the bat'
    elif p <= 36: return 'cube of force'
    elif p <= 37: return 'daern’s instant fortress'
    elif p <= 38: return 'dagger of venom'
    elif p <= 39: return 'dimensional shackles'
    elif p <= 40: return 'dragon slayer'
    elif p <= 41: return 'elven chain'
    elif p <= 42: return 'flame tongue'
    elif p <= 43: return 'gem of seeing'
    elif p <= 44: return 'giant slayer'
    elif p <= 45: return 'glamoured studded leather'
    elif p <= 46: return 'helm of teleportation'
    elif p <= 47: return 'horn of blasting'
    elif p <= 48: return 'horn of Valhalla (silver or brass)'
    elif p <= 49: return 'instrument of the bards (Canaith mandolin)'
    elif p <= 50: return 'instrument of the bards (Cli lyre)'
    elif p <= 51: return 'ioun stone (awareness)'
    elif p <= 52: return 'ioun stone (protection)'
    elif p <= 53: return 'ioun stone (reserve)'
    elif p <= 54: return 'ioun stone (sustenance)'
    elif p <= 55: return 'iron bands of Bilarro'
    elif p <= 56: return 'armor, +1 leather'
    elif p <= 57: return 'armor of resistance (leather)'
    elif p <= 58: return 'mace of disruption'
    elif p <= 59: return 'mace of smiting'
    elif p <= 60: return 'mace of terror'
    elif p <= 61: return 'mantle of spell resistance'
    elif p <= 62: return 'necklace of prayer beads'
    elif p <= 63: return 'periapt of proof against poison'
    elif p <= 64: return 'ring of animal influence'
    elif p <= 65: return 'ring of evasion'
    elif p <= 66: return 'ring of feather falling'
    elif p <= 67: return 'ring of free action'
    elif p <= 68: return 'ring of protection'
    elif p <= 69: return 'ring of resistance'
    elif p <= 70: return 'ring of spell storing'
    elif p <= 71: return 'ring of the ram'
    elif p <= 72: return 'ring of X-ray vision'
    elif p <= 73: return 'robe of eyes'
    elif p <= 74: return 'rod of rulership'
    elif p <= 75: return 'rod of the pact keeper, +2'
    elif p <= 76: return 'rope of entanglement'
    elif p <= 77: return 'armor, +1 scale mail'
    elif p <= 78: return 'armor of resistance (scale mail)'
    elif p <= 79: return 'shield, +2'
    elif p <= 80: return 'shield of missile attraction'
    elif p <= 81: return 'staff of charming'
    elif p <= 82: return 'staff of healing'
    elif p <= 83: return 'staff of swarming insects'
    elif p <= 84: return 'staff of the woodlands'
    elif p <= 85: return 'staff of withering'
    elif p <= 86: return 'stone of controlling earth elementals'
    elif p <= 87: return 'sun blade'
    elif p <= 88: return 'sword of life stealing'
    elif p <= 89: return 'sword of wounding'
    elif p <= 90: return 'tentacle rod'
    elif p <= 91: return 'vicious weapon'
    elif p <= 92: return 'wand of binding'
    elif p <= 93: return 'wand of enemy detection'
    elif p <= 94: return 'wand of fear'
    elif p <= 95: return 'wand of fireballs'
    elif p <= 96: return 'wand of lightning bolts'
    elif p <= 97: return 'wand of paralysis'
    elif p <= 98: return 'wand of the war mage, +2'
    elif p <= 99: return 'wand of wonder'
    elif p <= 100: return 'wings of flying'

def magic_item_table_h():
    p = r('d100')
    if p <= 10: return 'weapon, +3'
    elif p <= 12: return 'amulet of the planes'
    elif p <= 14: return 'carpet of flying'
    elif p <= 16: return 'crystal ball (very rare version)'
    elif p <= 18: return 'ring of regeneration'
    elif p <= 20: return 'ring of shooting stars'
    elif p <= 22: return 'ring of telekinesis'
    elif p <= 24: return 'robe of scintillating colors'
    elif p <= 26: return 'robe of stars'
    elif p <= 28: return 'rod of absorption'
    elif p <= 30: return 'rod of alertness'
    elif p <= 32: return 'rod of security'
    elif p <= 34: return 'rod of the pact keeper, +3'
    elif p <= 36: return 'scimitar of speed'
    elif p <= 38: return 'shield, +3'
    elif p <= 40: return 'staff of fire'
    elif p <= 42: return 'staff of frost'
    elif p <= 44: return 'staff of power'
    elif p <= 46: return 'staff of striking'
    elif p <= 48: return 'staff of thunder and lightning'
    elif p <= 50: return 'sword of sharpness'
    elif p <= 52: return 'wand of polymorph'
    elif p <= 54: return 'wand of the war mage, +3'
    elif p <= 55: return 'adamantine armor (half plate)'
    elif p <= 56: return 'adamantine armor (plate)'
    elif p <= 57: return 'animated shield'
    elif p <= 58: return 'belt of fire giant strength'
    elif p <= 59: return 'belt of frost giant strength (or stone)'
    elif p <= 60: return 'armor, +1 breastplate'
    elif p <= 61: return 'armor of resistance (breastplate)'
    elif p <= 62: return 'candle of invocation'
    elif p <= 63: return 'armor, +2 chain mail'
    elif p <= 64: return 'armor, +2 chain shirt'
    elif p <= 65: return 'cloak of arachnida'
    elif p <= 66: return 'dancing sword'
    elif p <= 67: return 'demon armor'
    elif p <= 68: return 'dragon scale mail'
    elif p <= 69: return 'dwarven plate'
    elif p <= 70: return 'dwarven thrower'
    elif p <= 71: return 'efreeti bottle'
    elif p <= 72: return 'figurine of wondrous power (obsidian steed)'
    elif p <= 73: return 'frost brand'
    elif p <= 74: return 'helm of brilliance'
    elif p <= 75: return 'horn of Valhalla (bronze)'
    elif p <= 76: return 'instrument of the bards (Anstruth harp)'
    elif p <= 77: return 'ioun stone (absorption)'
    elif p <= 78: return 'ioun stone (agility)'
    elif p <= 79: return 'ioun stone (fortitude)'
    elif p <= 80: return 'ioun stone (insight)'
    elif p <= 81: return 'ioun stone (intellect)'
    elif p <= 82: return 'ioun stone (leadership)'
    elif p <= 83: return 'ioun stone (strength)'
    elif p <= 84: return 'armor, +2 leather'
    elif p <= 85: return 'manual of bodily health'
    elif p <= 86: return 'manual of gainful exercise'
    elif p <= 87: return 'manual of golems'
    elif p <= 88: return 'manual of quickness of action'
    elif p <= 89: return 'mirror of life trapping'
    elif p <= 90: return 'nine lives stealer'
    elif p <= 91: return 'oathbow'
    elif p <= 92: return 'armor, +2 scale mail'
    elif p <= 93: return 'spellguard shield'
    elif p <= 94: return 'armor, +1 splint'
    elif p <= 95: return 'armor of resistance (splint)'
    elif p <= 96: return 'armor, +1 studded leather'
    elif p <= 97: return 'armor of resistance (studded leather)'
    elif p <= 98: return 'tome of clear thought'
    elif p <= 99: return 'tome of leadership and influence'
    elif p <= 100: return 'tome of understanding'

def magic_item_table_i():
    p = r('d100')
    if p <= 5: return 'defender'
    elif p <= 10: return 'hammer of thunderbolts'
    elif p <= 15: return 'luck blade'
    elif p <= 20: return 'sword of answering'
    elif p <= 23: return 'holy avenger'
    elif p <= 26: return 'ring of djinni summoning'
    elif p <= 29: return 'ring of invisibility'
    elif p <= 32: return 'ring of spell turning'
    elif p <= 35: return 'rod of lordly might'
    elif p <= 38: return 'staff of the magi'
    elif p <= 41: return 'vorpal sword'
    elif p <= 43: return 'belt of cloud giant strength'
    elif p <= 45: return 'armor, +2 breastplate'
    elif p <= 47: return 'armor, +3 chain mail'
    elif p <= 49: return 'armor, +3 chain shirt'
    elif p <= 51: return 'cloak of invisibility'
    elif p <= 53: return 'crystal ball (legendary version)'
    elif p <= 55: return 'armor, +1 half plate'
    elif p <= 57: return 'iron flask'
    elif p <= 59: return 'armor, +3 leather'
    elif p <= 61: return 'armor, +1 plate'
    elif p <= 63: return 'robe of the archmagi'
    elif p <= 65: return 'rod of resurrection'
    elif p <= 67: return 'armor, +1 scale mail'
    elif p <= 69: return 'scarab of protection'
    elif p <= 71: return 'armor, +2 splint'
    elif p <= 73: return 'armor, +2 studded leather'
    elif p <= 75: return 'well of many worlds'
    elif p <= 76: return 'magic armor (roll d12)'
    elif p <= 77: return 'apparatus of Kwalish'
    elif p <= 78: return 'armor of invulnerability'
    elif p <= 79: return 'belt of storm giant strength'
    elif p <= 80: return 'cubic gate'
    elif p <= 81: return 'deck of many things'
    elif p <= 82: return 'efreeti chain'
    elif p <= 83: return 'armor of resistance (half plate)'
    elif p <= 84: return 'horn of Valhalla (iron)'
    elif p <= 85: return 'instrument of the bards (Ollamh harp)'
    elif p <= 86: return 'ioun stone (greater absorption)'
    elif p <= 87: return 'ioun stone (mastery)'
    elif p <= 88: return 'ioun stone (regeneration)'
    elif p <= 89: return 'plate armor of etherealness'
    elif p <= 90: return 'armor of resistance (plate)'
    elif p <= 91: return 'ring of air elemental command'
    elif p <= 92: return 'ring of earth elemental command'
    elif p <= 93: return 'ring of fire elemental command'
    elif p <= 94: return 'ring of three wishes'
    elif p <= 95: return 'ring of water elemental command'
    elif p <= 96: return 'sphere of annihilation'
    elif p <= 97: return 'talisman of pure good'
    elif p <= 98: return 'talisman of the sphere'
    elif p <= 99: return 'talisman of ultimate evil'
    elif p <= 100: return 'tome of the stilled tongue'
