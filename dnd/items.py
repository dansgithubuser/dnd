properties={
	'ammunition': 'You can use a weapon that has the ammunition property to make a ranged Attack only if you have ammunition to fire from the weapon. Each time you Attack with the weapon, you expend one piece of ammunition. Drawing the ammunition from a Quiver, case, or other container is part of the Attack (you need a free hand to load a one-handed weapon). At the end of the battle, you can recover half your expended ammunition by taking a minute to Search the battlefield. If you use a weapon that has the ammunition property to make a melee Attack, you treat the weapon as an improvised weapon. A sling must be loaded to deal any damage when used in this way.',
	'finesse': 'When Making an Attack with a finesse weapon, you use your choice of your Strength or Dexterity modifier for the Attack and Damage Rolls. You must use the same modifier for both rolls.',
	'heavy': 'Small creatures have disadvantage on Attack rolls with heavy weapons. A heavy weapon\'s size and bulk make it too large for a Small creature to use effectively.',
	'light': 'A light weapon is small and easy to handle, making it ideal for use when fighting with two weapons.',
	'loading': 'Because of the time required to load this weapon, you can fire only one piece of ammunition from it when you use an action, Bonus Action, or reaction to fire it, regardless of the number of attacks you can normally make.',
	'range': 'A weapon that can be used to make a ranged Attack has a range in parentheses after the ammunition or thrown property. The range lists two numbers. The first is the weapon\'s normal range in feet, and the second indicates the weapon\'s long range. When attacking a target beyond normal range, you have disadvantage on the Attack roll. You can\'t Attack a target beyond the weapon\'s long range.',
	'reach': 'This weapon adds 5 feet to your reach when you Attack with it, as well as when determining your reach for Opportunity Attacks with it.',
	'special': 'A weapon with the special property has unusual rules governing its use, explained in the weapon\'s description.',
	'thrown': 'If a weapon has the thrown property, you can throw the weapon to make a ranged Attack. If the weapon is a melee weapon, you use the same ability modifier for that Attack roll and damage roll that you would use for a melee Attack with the weapon. For example, if you throw a Handaxe, you use your Strength, but if you throw a Dagger, you can use either your Strength or your Dexterity, since the Dagger has the finesse property.',
	'two-handed': 'This weapon requires two hands when you Attack with it.',
	'versatile': 'This weapon can be used with one or two hands. A damage value in parentheses appears with the property -- the damage when the weapon is used with two hands to make a melee Attack.',
	'improvised weapons': '''Sometimes characters don\'t have their weapons and have to Attack with whatever is at hand. An improvised weapon includes any object you can wield in one or two hands, such as broken glass, a table leg, a frying pan, a wagon wheel, or a dead Goblin.

Often, an improvised weapon is similar to an actual weapon and can be treated as such. For example, a table leg is akin to a club. At the GM\'s option, a character proficient with a weapon can use a similar object as if it were that weapon and use his or her proficiency bonus.

An object that bears no resemblance to a weapon deals 1d4 damage (the GM assigns a damage type appropriate to the object). If a character uses a ranged weapon to make a melee Attack, or throws a melee weapon that does not have the thrown property, it also deals 1d4 damage. An improvised thrown weapon has a normal range of 20 feet and a long range of 60 feet.''',
	'silvered weapons': 'Some Monsters that have immunity or Resistance to nonmagical weapons are susceptible to silver weapons, so cautious adventurers invest extra coin to plate their weapons with silver. You can silver a single weapon or ten pieces of ammunition for 100 gp. This cost represents not only the price of the silver, but the time and expertise needed to add silver to the weapon without making it less effective.',
}

items={
	'hide_armor': {'type': 'medium_armor', 'armor_class': 12, 'weight': 12},
	'scale_mail': {'type': 'medium_armor', 'armor_class': 14, 'weight': 45, 'disadvantages': ['stealth']},
	'breastplate': {'type': 'medium_armor', 'armor_class': 14, 'weight': 20},
	'shield': {'type': 'shield', 'armor_class': 2, 'weight': 6},
	'club': {'type': 'melee_weapon', 'damage': 'd4 BLUDGEONING', 'weight': 2, 'properties': ['light']},
	'greatclub': {'type': 'melee_weapon', 'damage': 'd8 BLUDGEONING', 'weight': 10, 'properties': ['two-handed']},
	'mace': {'type': 'melee_weapon', 'damage': 'd6 BLUDGEONING', 'weight': 4},
	'dagger': {'type': 'melee_weapon', 'damage': 'd4 PIERCING', 'range': (20, 60), 'weight': 1, 'properties': ['finesse', 'light', 'range', 'thrown']},
	'sling': {'type': 'ranged_weapon', 'damage': 'd4 BLUDGEONING', 'range': (30, 120), 'properties': ['range']},
	'shortsword': {'type': 'melee_weapon', 'damage': 'd6 PIERCING', 'weight': 2, 'properties': ['finesse', 'light']},
	'chain_mail': {'type': 'heavy_armor', 'armor_class': 16, 'disadvantages': ['stealth'], 'weight': 55},
	'longsword': {'type': 'melee_weapon', 'damage': 'd8 SLASHING', 'secondary_damage': 'd10 SLASHING', 'weight': 3, 'properties': ['versatile']},
	'rapier': {'type': 'melee_weapon', 'damage': 'd8 PIERCING', 'weight': 2, 'properties': ['finesse']},
	'greatsword': {'type': 'melee_weapon', 'damage': '2d6 SLASHING', 'weight': 7, 'properties': ['heavy', 'two-handed']},
	'scimitar': {'type': 'melee_weapon', 'damage': 'd6 SLASHING', 'weight': 3, 'properties': ['finesse', 'light']},
	'pike': {'type': 'melee_weapon', 'damage': 'd10 PIERCING', 'properties': ['heavy', 'reach', 'two-handed'], 'weight': 18},
	'lance': {'type': 'melee_weapon', 'damage': 'd12 PIERCING', 'properties': ['reach'], 'weight': 6, 'description': "You have disadvantage when you use a lance to Attack a target within 5 feet of you. Also, a lance requires two hands to wield when you aren't mounted."},
	'light_hammer': {'type': 'melee_weapon', 'damage': 'd4 BLUDGEONING', 'range': (20, 60), 'weight': 2, 'properties': ['light', 'range', 'thrown']},
	'quarterstaff': {'type': 'melee_weapon', 'damage': 'd6 BLUDGEONING', 'secondary_damage': 'd8 BLUDGEONING', 'weight': 4, 'properties': ['versatile']},
	'maul': {'type': 'melee_weapon', 'damage': '2d6 BLUDGEONING', 'properties': ['heavy', 'two-handed'], 'weight': 10},
	'warhammer': {'type': 'melee_weapon', 'damage': 'd8 BLUDGEONING', 'secondary_damage': 'd10 BLUDGEONING', 'weight': 2, 'properties': ['versatile']},
	'halberd': {'type': 'melee_weapon', 'damage': 'd10 SLASHING', 'weight': 6, 'properties': ['reach', 'two-handed']},
	'handaxe': {'type': 'melee_weapon', 'damage': 'd6 SLASHING', 'range': (20, 60), 'weight': 2, 'properties': ['light', 'range', 'thrown']},
	'battleaxe': {'type': 'melee_weapon', 'damage': 'd8 SLASHING', 'secondary_damage': 'd10 SLASHING', 'weight': 4, 'properties': {'versatile'}},
	'greataxe': {'type': 'melee_weapon', 'damage': 'd12 SLASHING', 'weight': 7, 'properties': ['heavy', 'two-handed']},
	'war_pick': {'type': 'melee_weapon', 'damage': 'd8 PIERCING', 'weight': 2},
	'sickle': {'type': 'melee_weapon', 'damage': 'd4 SLASHING', 'weight': 2, 'properties': ['light']},
	'flail': {'type': 'melee_weapon', 'damage': 'd8 BLUDGEONING', 'weight': 2},
	'morningstar': {'type': 'melee_weapon', 'damage': 'd8 PIERCING', 'weight': 4},
	'glaive': {'type': 'melee_weapon', 'damage': 'd10 SLASHING', 'weight': 6, 'properties': ['heavy', 'reach', 'two-handed']},
	'whip': {'type': 'melee_weapon', 'damage': 'd4 SLASHING', 'weight': 3, 'properties': ['finesse', 'reach']},
	'javelin': {'type': 'melee_weapon', 'damage': 'd6 PIERCING', 'range': (30, 120), 'properties': ['range', 'thrown'], 'weight': 2},
	'spear': {'type': 'melee_weapon', 'damage': 'd6 PIERCING', 'secondary_damage': 'd8 PIERCING', 'range': (20, 60), 'properties': ['range', 'thrown', 'versatile'], 'weight': 3},
	'trident': {'type': 'melee_weapon', 'damage': 'd6 PIERCING', 'secondary_damage': 'd8 PIERCING', 'range': (20, 60), 'properties': ['range', 'thrown', 'versatile'], 'weight': 4},
	'leather_armor': {'type': 'light_armor', 'armor_class': 11, 'weight': 10},
	'shortbow': {'type': 'ranged_weapon', 'damage': 'd6 PIERCING', 'range': (80, 320), 'weight': 2, 'properties': ['range', 'two-handed', 'ammunition']},
	'longbow': {'type': 'ranged_weapon', 'damage': 'd8 PIERCING', 'range': (150, 600), 'weight': 2, 'properties': ['range', 'two-handed', 'ammunition', 'heavy']},
	'blowgun': {'type': 'ranged_weapon', 'damage': '1 PIERCING', 'range': (25, 100), 'weight': 1, 'properties': ['range', 'loading']},
	'dart': {'type': 'melee_weapon', 'damage': 'd4 PIERCING', 'range': (20, 60), 'weight': 0.25, 'properties': ['finesse', 'range', 'thrown']},
	'hand_crossbow': {'type': 'ranged_weapon', 'damage': 'd6 PIERCING', 'range': (30, 120), 'weight': 3, 'properties': ['range', 'loading', 'light']},
	'light_crossbow': {'type': 'ranged_weapon', 'damage': 'd8 PIERCING', 'range': (80, 320), 'weight': 5, 'properties': ['range', 'loading', 'two-handed']},
	'heavy_crossbow': {'type': 'ranged_weapon', 'damage': 'd10 PIERCING', 'range': (100, 400), 'weight': 18, 'properties': ['range', 'loading', 'heavy', 'two-handed']},
	'net': {'type': 'ranged_weapon', 'range': (5, 15), 'weight': 3, 'properties': ['range', 'thrown']},
	'improvised': {'damage': 'd4', 'range': (20, 60), 'properties': ['range', 'improvised']},
	'ball_bearings': {'weight': 2, 'target': 'Each creature in a 10-foot square centered on a point within range', 'save': '10 DEXTERITY'},
	'backpack': {'weight': 5, 'description': 'A backpack can hold one cubic foot or 30 pounds of gear. You can also strap items, such as a Bedroll or a coil of rope, to the outside of a backpack.'},
	'waterskin': {'weight': 5, 'description': 'A waterskin can hold up to 4 pints of liquid.'},
	'rations': {'weight': 2, 'description': 'A day worth of dry food.'},
	'gp': {'weight': 0.02},
	'bell': {'weight': 1},
	'candle': {'weight': 1, 'range': (5, 10), 'duration': '1h'},
	'crowbar': {'weight': 5, 'description': 'advantage to strength checks where the crowbar can be used'},
	'hammer': {'weight': 3},
	'piton': {'weight': 0.25},
	'hooded_lantern': {'weight': 2, 'range': (30, 60), 'duration': '6h', 'description': 'Once lit, it burns for 6 hours on a flask (1 pint) of oil. As an action, you can lower the hood, reducing the light to dim light in a 5-foot radius.'},
	'oil': {'weight': 1, 'range': (20, 60), 'properties': ['improvised'], 'damage': '5 FIRE', 'duration': '12s', 'description': 'Oil usually comes in a clay flask that holds 1 pint. As an action, you can splash the oil in this flask onto a creature within 5 feet of you or throw it up to 20 feet, shattering it on impact. Make a ranged Attack against a target creature or object, treating the oil as an improvised weapon. On a hit, the target is covered in oil. If the target takes any fire damage before the oil dries (after 1 minute), the target takes an additional 5 fire damage from the burning oil. You can also pour a flask of oil on the ground to cover a 5-foot-square area, provided that the surface is level. If lit, the oil burns for 2 rounds and deals 5 fire damage to any creature that enters the area or ends its turn in the area. A creature can take this damage only once per turn.'},
	'tinderbox': {'weight': 1, 'description': 'This small container holds flint, fire steel, and tinder (usually dry cloth soaked in light oil) used to kindle a fire. Using it to light a torch - or anything else with abundant, exposed fuel - takes an action. Lighting any other fire takes 1 minute.'},
	'bedroll': {'weight': 7},
	'disguise_kit': {'weight': 3},
	'belt_pouch': {'weight': 0.5, 'description': 'carries 6 pounds, 1/5 cubic feet'},
	'thieves_tools': {'weight': 1, 'description': 'This set of tools includes a small file, a set of lock picks, a small mirror mounted on a metal handle, a set of narrow-bladed scissors, and a pair of pliers.'},
	'robes': {'weight': 4},
	'ink': {'weight': 1},
	'knife': {'weight': 1},
	'torch': {'weight': 1, 'range': (20, 40), 'duration': '1h', 'damage': '1 FIRE'},
	'mess_kit': {'weight': 1, 'description': 'This tin box contains a cup and simple cutlery. The box clamps together, and one side can be used as a cooking pan and the other as a plate or shallow bowl.'},
	'hempen_rope': {'weight': 10, 'description': '50ft. 2 hit points and can be burst with a DC 17 Strength check.'},
	'alchemists_supplies': {'weight': 8},
	'shovel': {'weight': 5},
	'iron_pot': {'weight': 10},
	'quiver': {'weight': 1, 'description': 'holds 20 arrows'},
	'string': {'description': '10 ft.'},
	'chest': {'weight': 25, 'description': '12 cubic ft, 300 lbs.'},
	'scroll_case': {'weight': 1, 'description': 'This cylindrical leather case can hold up to ten rolled-up sheets of paper or five rolled-up sheets of Parchment.'},
	'fine_clothes': {'weight': 6},
	'lamp': {'weight': 1, 'range': (15, 45), 'duration': '6h', 'description': 'Once lit, it burns for 6 hours on a flask (1 pint) of oil.'},
	'costume': {'weight': 4},
	'blanket': {'weight': 3},
}

simple_weapons=[
	'club',
	'dagger',
	'greatclub',
	'handaxe',
	'javelin',
	'light_hammer',
	'mace',
	'quarterstaff',
	'sickle',
	'spear',
	'light_crossbow',
	'dart',
	'shortbow',
	'sling'
]

martial_weapons=[
	'battleaxe',
	'flail',
	'glaive',
	'greataxe',
	'greatsword',
	'halberd',
	'lance',
	'longsword',
	'maul',
	'morningstar',
	'pike',
	'rapier',
	'scimitar',
	'shortsword',
	'trident',
	'war_pick',
	'warhammer',
	'whip',
	'blowgun',
	'hand_crossbow',
	'heavy_crossbow',
	'longbow',
	'net'
]

weapons=simple_weapons+martial_weapons

burglars_pack=[
	'backpack', 'ball_bearings', 'string', 'bell', {'candle': 5}, 'crowbar',
	'hammer', {'piton': 10}, 'hooded_lantern', {'oil': 2}, {'rations': 5},
	'tinderbox', 'waterskin', 'hempen_rope',
]

diplomats_pack=[
	'chest', {'scroll_case': 2}, 'fine_clothes', 'ink', 'pen', 'lamp',
	{'oil': 2}, {'paper': 5}, 'perfume', 'sealing_wax', 'soap',
]

dungeoneers_pack=[
	'backpack', 'crowbar', 'hammer', {'piton': 10}, {'torch': 10}, 'tinderbox',
	{'rations': 10}, 'waterskin', 'hempen_rope',
]

entertainers_pack=[
	'backpack', 'bedroll', {'costume': 2}, {'candle': 5}, {'rations': 5},
	'waterskin', 'disguise_kit',
]

explorers_pack=[
	'backpack', 'bedroll', 'mess_kit', 'tinderbox',
	{'torch': 10}, {'rations': 10},
	'waterskin', 'hempen_rope',
]

priests_pack=[
	'backpack', 'blanket', {'candle': 10}, 'tinderbox', 'alms_box',
	{'incense': 2}, 'censer', 'vestments', {'rations': 2}, 'waterskin',
]

scholars_pack=[
	'backpack', 'book_of_lore', 'ink', 'pen', {'parchment': 10}, 'bag_of_sand',
	'knife',
]

# house rules for more interesting nonmagical weapons
weapon_mods=[
	'req_str_12', 'req_str_14', 'req_str_16', 'req_str_18', 'req_str_20',
	'req_dex_12', 'req_dex_14', 'req_dex_16', 'req_dex_18', 'req_dex_20',
	'd4', 'd6', 'd8', 'd10', 'd12',
	'extra_die',
	'crit_on_19', 'crit_on_18',
	'extra_crit_die_1', 'extra_crit_die_2', 'extra_crit_die_3',
]
