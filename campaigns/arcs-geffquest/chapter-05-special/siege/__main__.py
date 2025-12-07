from pathlib import Path
import sys

DIR = Path(__file__).resolve().parent

sys.path.append(str(DIR.parent.parent.parent.parent))

import dnd

from allies import *
from archers import *
from cavalry import *
from dragon import *
from ex import *
from giant import *
from infantry import *
from lieutenant import *
from one_based import *
from roll import *
from skeleton import *
from unit import *

dragon = OneBasedList(Dragon(i=i+1) for i in range(3))
archers = Archers()
cavalry = Cavalry()
infantry = OneBasedList(Infantry(i=i+1) for i in range(8))
tensa = Tensa()
alfred = Alfred()
ingrid = Ingrid()
ados = Ados()
melvin = Melvin()
marjoria = Marjoria()

skels = OneBasedList(Skels(i=i+1) for i in range(10))
giant = OneBasedList(Giant(i=i+1) for i in range(3))
lieutenant = OneBasedList(Lieutenant(i=i+1) for i in range(8))
ex = Ex()

def status():
    for i in globals().values():
        if not any([
            isinstance(i, Unit),
            isinstance(i, OneBasedList),
        ]):
            continue
        print(i)
        print()

def raise_dead(x, context=''):
    if isinstance(x, Unit):
        if x.hp <= 0:
            if context: print(context, end='')
            print(x, end=' -> ')
            x.hp = x.hp_max
            print(x)
            x.save()
        elif x.n <= 0:
            if context: print(context, end='')
            print(x, end=' -> ')
            x.n = x.n_max
            print(x)
            x.save()
        elif x.n < x.n_max:
            if context: print(context, end='')
            print(x.n_max - x.n, type(x).__name__, 'unaccounted')
    elif isinstance(x, OneBasedList):
        for i, v in enumerate(x):
            raise_dead(v, context=f'{i+1}: ')

def mass_raise_dead():
    for v in globals().values():
        raise_dead(v)
