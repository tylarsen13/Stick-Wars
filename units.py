import math


class Unit(object):
    def __init__(self, team):
        self.team = team

    def move(self):
        pass

    def normalizeHP(self):
        self.hp = math.ceil(self.hp*10)/10

    def attack(self, unit):
        # Round HP up to the nearest integer
        selfRoundedHP = math.ceil(self.hp)
        # Calculate Defenders New HP
        unit.hp -= (self.firePower * selfRoundedHP) / (unit.defensePower * 1.5)
        # Round HP up to the nearest integer
        unitRoundedHP = math.ceil(unit.hp)
        # Calculate Attackers New HP
        if unit.hp > 0:
            self.hp -= (unit.firePower * unitRoundedHP) / (self.defensePower * 1.5)
        self.normalizeHP()
        unit.normalizeHP()


class GroundUnit(Unit):
    def __init__(self, team):
        super(GroundUnit, self).__init__(team)
        self.unitClass = "GroundUnit"
        self.active = True
        self.validTerrain = ['plain']


class Infantry(GroundUnit):
    def __init__(self, team, hp):
        super(Infantry, self).__init__(team)
        self.unitType = "Infantry"
        self.hp = hp
        self.hpMax = 10
        self.firePower = 1
        self.defensePower = 1
        self.moveAbility = 3
        self.rangeMin = 1
        self.rangeMax = 1


class Tank(GroundUnit):
    def __init__(self, team, hp):
        super(Tank, self).__init__(team)
        self.unitType = "Tank"
        self.hp = hp
        self.hpMax = 10
        self.firePower = 2
        self.defensePower = 3
        self.moveAbility = 5
        self.rangeMin = 1
        self.rangeMax = 1


class Artillery(GroundUnit):
    def __init__(self, team, hp):
        super(Artillery, self).__init__(team)
        self.unitType = "Artillery"
        self.hp = hp
        self.hpMax = 10
        self.firePower = 1.75
        self.defensePower = 3
        self.moveAbility = 3
        self.rangeMin = 1
        self.rangeMax = 3
        

class AirUnit(Unit):
    def __init__(self, team):
        super(AirUnit, self).__init__(team)
        self.unitClass = "AirUnit"
        self.active = True
        self.validTerrain = ['plain', 'sea']


class Fighter(AirUnit):
    def __init__(self, team, hp):
        super(Fighter, self).__init__(team)
        self.unitType = "Fighter"
        self.hp = hp
        self.hpMax = 10
        self.firePower = 5
        self.defensePower = 1
        self.moveAbility = 7
        self.rangeMin = 1
        self.rangeMax = 1