#!/usr/bin/env python3

import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('--tribe')
parser.add_argument('--vocation')
parser.add_argument('--dead-ok', action='store_true')
parser.add_argument('--age-min', type=int)
parser.add_argument('--age-max', type=int)
parser.add_argument('--gender')
args = parser.parse_args()

year = 2232

for path in os.listdir('.'):
    with open(path) as f:
        lines = f.readlines()
    lines = [line.strip().replace('<br>', '') for line in lines]
    lines = [line for line in lines if line]
    name = lines[0]
    vocation = lines[1]
    born = lines[2]
    died = lines[3]
    mother = lines[4]
    father = lines[5]
    if args.tribe:
        if args.tribe not in name.lower():
            continue
    if args.vocation:
        if args.vocation not in vocation.lower():
            continue
    if not args.dead_ok:
        if died != 'died: -':
            continue
    age = year - int(born.split()[1])
    if args.age_min:
        if age < args.age_min:
            continue
    if args.age_max:
        if age > args.age_max:
            continue
    if args.gender:
        if name.split()[-1][1].lower() != args.gender.lower():
            continue
    print(f'{path:10} {name:40} {born:10} {died:10} {vocation:20}')
