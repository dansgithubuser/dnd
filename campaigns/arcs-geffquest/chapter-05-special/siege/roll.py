import random

def roll(n=1, sides=20):
    return sum(random.randint(1, sides) for _ in range(n))
