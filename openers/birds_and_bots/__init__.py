import dnd

mioldeth_vi = dnd.base.Entity()
mioldeth_vi.name = 'Mioldeth Vi'
mioldeth_vi.set_stats(7, 13, 10, 15, 16, 18)
mioldeth_vi.age = 123
mioldeth_vi.height = '''5'9"'''
mioldeth_vi.weight = 110
dnd.races.WoodElf.__init__(mioldeth_vi, gender='m')
dnd.classes.Sorcerer.init(mioldeth_vi, 3)
dnd.backgrounds.Generic.init(mioldeth_vi)
mioldeth_vi.proficiencies = [
    'deception', 'arcana',  # sorcerer
    'alchemists_supplies', 'herbalism_kit', 'stealth', 'persuasion',  # background
]
mioldeth_vi.spells[0] += ['acid_splash', 'mage_hand', 'mending']
mioldeth_vi.wearing = ['leather_armor']
