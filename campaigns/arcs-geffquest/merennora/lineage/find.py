#!/usr/bin/env python3

import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('--clan')
parser.add_argument('--vocation')
parser.add_argument('--dead-ok', action='store_true')
args = parser.parse_args()

for path in os.listdir('.'):
    with open(path) as f:
        lines = f.readlines()
    lines = [line.strip() for line in lines]
    lines = [line for line in lines if line]
    name = lines[0]
    vocation = lines[1]
    born = lines[2]
    died = lines[3]
    mother = lines[4]
    father = lines[5]
    if args.clan:
        if args.clan not in name.lower():
            continue
    if args.vocation:
        if args.vocation not in vocation.lower():
            continue
    if not args.dead_ok:
        if 'died: -' not in died:
            continue
    print(path, name)
