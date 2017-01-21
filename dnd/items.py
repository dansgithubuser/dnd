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
	'scale_mail': {'type': 'medium armor', 'armor_class': 14, 'weight': 45, 'disadvantages': ['stealth']},
	'shield': {'type': 'shield', 'armor_class': 2, 'weight': 6},
	'mace': {'type': 'melee weapon', 'damage': 'd6', 'damage_type': 'bludgeoning', 'weight': 4},
	'dagger': {'type': 'melee weapon', 'damage': 'd4', 'damage_type': 'piercing', 'range': (20, 60), 'weight': 1, 'properties': ['finesse', 'light', 'range', 'thrown']},
	'shortsword': {'type': 'melee weapon', 'damage': 'd6', 'damage_type': 'piercing', 'weight': 2, 'properties': ['finesse', 'light']},
	'chain_mail': {'type': 'heavy armor', 'armor_class': 16, 'disadvantages': ['stealth'], 'weight': 55},
	'longsword': {'type': 'melee weapon', 'damage': 'd8', 'secondary_damage': 'd10', 'damage_type': 'slashing', 'weight': 3, 'properties': 'versatile'},
	'pike': {'type': 'melee weapon', 'damage': 'd10', 'damage_type': 'piercing', 'properties': ['heavy', 'reach', 'two-handed'], 'weight': 18},
	'leather_armor': {'type': 'light armor', 'armor_class': 11, 'weight': 10},
	'shortbow': {'type': 'ranged weapon', 'damage': 'd6', 'damage_type': 'piercing', 'range': (80, 320), 'weight': 2, 'properties': ['range', 'two-handed']},
}
