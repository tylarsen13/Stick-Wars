

class Unit(object):
    def __init__(self, unitId, hp, hpMax, hpMin):
        self.unitId = unitId
        self.hp = hp
        self.hpMax = hpMax
        self.hpMin = hpMin

    def move(self):
        pass

class GroundUnit(Unit):
    def __init__(self, unitId, unitClass):
        super(GroundUnit, self).__init__(self, unitId)
        self.unitClass = unitClass

class Infantry(GroundUnit):
    def __init__(self, unitId, unitClass, unitType):
        super(Infantry, self).__init__(self, unitId, unitClass)
        self.unitType = unitType
