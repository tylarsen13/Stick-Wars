

class Unit(object):
    def __init__(self, team):
        self.team = team

    def move(self):
        pass

class GroundUnit(Unit):
    def __init__(self, team, unitClass):
        super(GroundUnit, self).__init__(self, team)
        self.unitClass = unitClass

class Infantry(GroundUnit):
    def __init__(self, team, unitClass, unitType, hp):
        super(Infantry, self).__init__(self, team, unitClass)
        self.unitType = unitType
        self.hp = hp
        self.hpMax = 10
