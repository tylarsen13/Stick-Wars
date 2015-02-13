

class Unit(object):
    def __init__(self):
        pass

    def move(self):
        pass

class GroundUnit(Unit):
    def __init__(self, unitClass):
        self.unitClass = unitClass

class Infantry(GroundUnit):
    def __init__(self, unitClass, unitType, hp):
        super(Infantry, self).__init__(self, unitClass)
        self.unitType = unitType
        self.hp = hp
        self.hpMax = 10
