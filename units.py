

class Unit(object):
    def __init__(self, team):
        self.team = team

    def move(self):
        pass

class GroundUnit(Unit):
    def __init__(self, team):
        super(GroundUnit, self).__init__(team)
        self.unitClass = "GroundUnit"

class Infantry(GroundUnit):
    def __init__(self, team, hp):
        super(Infantry, self).__init__(team)
        self.unitType = "Infantry"
        self.hp = hp
        self.hpMax = 10


    def attack(self, unit):
        unit.hp *= (.50)
        unit.hp = int(unit.hp)
        self.hp *= (.80)
        self.hp = int(self.hp)
        
