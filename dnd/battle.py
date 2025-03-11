from . import base

class Member:
    def __init__(self, hp, ac, hit, dmg, vantage=0):
        self.hp = hp
        self.ac = ac
        self.hit = hit
        self.dmg = dmg
        self.vantage = vantage

    def attack(self, target):
        if base.roll(f'd20+{self.hit}', self.vantage) >= target.ac:
            target.hp -= base.roll(self.dmg)

class Team:
    def __init__(self, members):
        self.members = members

    def attack(self, other_team):
        for member in self.standing():
            target = sorted(other_team.standing(), key=lambda i: i.hp)[0]
            member.attack(target)
            if other_team.dead():
                break

    def dead(self):
        return all(i.hp <= 0 for i in self.members)

    def standing(self):
        return [i for i in self.members if i.hp > 0]

def two_teams(team_1, team_2):
    while not team_1.dead() and not team_2.dead():
        print('team 1 attacks')
        team_1.attack(team_2)
        if team_2.dead(): break
        print('team 2 attacks')
        team_2.attack(team_1)
    if team_2.dead():
        print('team 1 wins')
        return team_1
    else:
        print('team 2 wins')
        return team_2
