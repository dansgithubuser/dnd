from roll import roll
from unit import Unit

class Dragon(Unit):
    def __init__(self, **kwargs):
        super().__init__(hp=256, ac=19, **kwargs)
        self.stats(27, 14, 25, 16, 15, 24)
        self.hit_bonus = 14
        self.dmg_bonus = 8

    def attack_group(self, other):
        damage = roll(12, 10)
        m = 1 - other.saving_throw('dex', 21) / 2
        other.damage(damage * m, area=True)

    def attack_single(self, other):
        for _ in range(3):
            damage += self.attack_damage(other, 2, 10)
            for _ in range(2):
                damage += self.attack_damage(other, 2, 6)
        other.damage(damage)

    def attack(self, other):
        if other.n > 1:
            self.attack_group(other)
        else:
            self.attack_single(other)
