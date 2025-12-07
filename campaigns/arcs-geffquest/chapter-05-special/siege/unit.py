from roll import roll

import copy
import json
import os

class Unit:
    def __init__(self, *, hp=1, ac=10, n=1, i=None):
        self.hp_max = hp
        self.hp = hp
        self.ac = ac
        self.n_max = n
        self.n = n
        self.i = i
        self.hit_bonus = 0
        self.dmg_bonus = 0
        self.stats()
        self.load()

    def stats(self, str=10, dex=10, con=10, int=10, wis=10, cha=10):
        self.str = str
        self.dex = dex
        self.con = con
        self.int = int
        self.wis = wis
        self.cha = cha

    def __repr__(self):
        return f'<{type(self).__name__} hp={self.hp}/{self.hp_max} ac={self.ac}>'

    def ability_score(self, stat):
        return getattr(self, stat)

    def ability_mod(self, stat):
        return (self.ability_score(stat) - 10) // 2

    def saving_throw(self, stat, dc):
        return roll() + self.ability_mod(stat) >= dc

    def attack_damage(self, other, n, sides):
        if roll() + self.hit_bonus > other.ac:
            return roll(n, sides) + self.dmg_bonus
        return 0

    def damage(self, damage, *, area=False):
        print(self, end=' -> ')
        self.hp -= int(damage)
        print(self)
        if self.hp <= 0:
            print('💀')
        self.save()

    def match(self, other):
        clone = copy.deepcopy(other)
        self.attack(other)
        clone.attack(self)

    def test(self, other):
        clone = copy.deepcopy(other)
        self.attack(clone)

    def test_match(self, other):
        self.test(other)
        other.test(self)

    def file_name(self):
        file_name = type(self).__name__
        if self.i:
            file_name += f'{self.i}'
        file_name += '.json'
        return file_name

    def save(self):
        with open(self.file_name(), 'w') as f:
            json.dump(
                {
                    'hp': self.hp,
                },
                f,
            )

    def load(self):
        if not os.path.exists(self.file_name()):
            return
        with open(self.file_name()) as f:
            j = json.load(f)
        self.hp = j['hp']
