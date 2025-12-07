from roll import roll
from unit import Unit

class Skels(Unit):
    def __init__(self, **kwargs):
        super().__init__(n=1000, **kwargs)
        self.ac = 13
        self.atk_bonus = 4
        self.dmg_bonus = 2

    def __repr__(self):
        return f'<{type(self).__name__} n={self.n}>'

    def attack(self, other):
        damage = 0
        for _ in range(3 * min(self.n, 30)):
            damage += self.attack_damage(other, 1, 6)
        other.damage(damage)

    def damage(self, damage, *, area=False):
        print(self, end=' -> ')
        if area:
            self.n -= int(damage * self.n / 5)
        else:
            self.n -= int(damage / 5)
        print(self)
        if self.n <= 0:
            print('💀')
