from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from pydantic import BaseModel

import math
import random

#===== vectors =====#
def add3(a, b):
    return [i+j for i, j in zip(a, b)]

def sub3(a, b):
    return [i-j for i, j in zip(a, b)]

#===== fun stuff =====#
GLYPHS = [
    "△",
    "|",
    "‖",
    "/",
    "╳",
    "⫯",
    "O",
]

def number_to_glyphs(n):
    n = int(n)
    if n < 0:
        return ""
    if not n:
        return glyphs[0]
    glyphs = []
    while n:
        glyphs.append(GLYPHS[n % 6])
        n //= 6
    return " ".join(glyphs)

class Tuner:
    def __init__(self, setting, power, distance, angle):
        self.setting = setting
        self.power = 10 * power
        angle *= math.tau / 360
        self.position = (distance * math.cos(angle), distance * math.sin(angle))

r1 = 1121
r2 = 21/23 * r1
r3 = 7/23 * r1

tuners = {
    "ver": Tuner(0.25, 6, r1, 180),  # far left
    "dou": Tuner(0.73, 6, r1,   0),  # far right
    "spa": Tuner(0.08, 3, r2,  60),  # toppish
    "cro": Tuner(0.90, 1, r3,  60),  # inner toppish
    "sem": Tuner(0.09, 1, r3, 180),  # inner left
    "who": Tuner(0.96, 1, r3, 240),  # inner bottomish
}

leyflare_origin = (-719, 902, -568)  # east, north, up
leyflare = leyflare_origin

def force_toward(pos3, power):
    global leyflare
    s = sub3(pos3, leyflare)
    d = sum(i ** 2 for i in s) ** (1/2)
    if d < 1:
        return
    force = [power*i/d for i in s]
    leyflare = add3(leyflare, force)

def update(iters=10):
    for i in range(iters):
        for j, tuner in enumerate(tuners.values()):
            force_toward((*tuner.position, 0), tuner.power * tuner.setting)
        righting = sub3(leyflare, leyflare_origin)
        righting = sum(i ** 2 for i in righting) ** (1/2) / 2
        force_toward(leyflare_origin, righting)

update(100)

def distance(glyph):
    tuner = tuners[glyph]
    s = sub3((*tuner.position, 0), leyflare)
    d = sum(i ** 2 for i in s) ** (1/2)
    d += random.triangular(-2, 2)
    return number_to_glyphs(d)

#===== server =====#
class Rsp(BaseModel):
    reading: str
    setting: float

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/{glyph}")
def ping(glyph: str, setting: float) -> Rsp:
    if glyph not in tuners:
        return Rsp(
            reading="",
            setting=0,
        )
    if setting >= 0:
        tuners[glyph].setting = setting
    update()
    print(leyflare)
    return Rsp(
        reading=distance(glyph),
        setting=tuners[glyph].setting,
    )
