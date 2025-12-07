from roll import roll
from unit import Unit

class Giant(Unit):
    def __init__(self, **kwargs):
        super().__init__(hp=230, ac=16, **kwargs)
        self.stats(29, 14, 20, 16, 18, 18)
        self.hit_bonus = 14
        self.dmg_bonus = 9

    def attack(self, other):
        damage = 0
        for _ in range(3 * 2):
            damage += self.attack_damage(other, 6, 6)
        other.damage(damage)
