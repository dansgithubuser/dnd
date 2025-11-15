from roll import roll
from unit import Unit

class Lieutenant(Unit):
    def __init__(self, **kwargs):
        super().__init__(hp=100, ac=17, **kwargs)
        self.stats(11, 16, 16, 20, 14, 16)

    def attack_group(self, other):
        damage = roll(8, 6)
        m = 1 - other.saving_throw('con', 18) / 2
        other.damage(damage * m, area=True)

    def attack_single(self, other):
        damage = 0
        for _ in range(3):
            m = 1 - other.saving_throw('con', 18) / 2
            damage += m * (roll(7, 8) + 30)
        other.damage(damage)

    def attack(self, other):
        if other.n > 1:
            self.attack_group(other)
        else:
            self.attack_single(other)
