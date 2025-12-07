from roll import roll
from unit import Unit

class Tensa(Unit):
    def __init__(self, **kwargs):
        super().__init__(hp=102, ac=15, **kwargs)
        self.stats(12, 12, 12, 20, 12, 12)

class Alfred(Unit):
    def __init__(self, **kwargs):
        super().__init__(hp=80, ac=18, **kwargs)
        self.stats(20, 12, 12, 12, 12, 12)

class Ingrid(Unit):
    def __init__(self, **kwargs):
        super().__init__(hp=179, ac=17, **kwargs)
        self.stats(12, 20, 18, 12, 12, 12)

class Ados(Unit):
    def __init__(self, **kwargs):
        super().__init__(hp=80, ac=16, **kwargs)
        self.stats(20, 12, 12, 12, 12, 12)

class Melvin(Unit):
    def __init__(self, **kwargs):
        super().__init__(hp=110, ac=16, **kwargs)
        self.stats(12, 14, 12, 12, 12, 20)

class Marjoria(Unit):
    pass
