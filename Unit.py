from Position import Position
from Command import CommandGroup
from copy import deepcopy

class MoveableBase(object):

    def __init__(self, x, y):
        self.position = Position(x, y)

    def X(self):
        return self.position.X()

    def Y(self):
        return self.position.Y()

    def XY(self):
        return self.X(), self.Y()

    def Distance(self, x, y):
        return self.position.Distance(x, y)

    def Step(self, dx, dy):
        self.position.AdjustBy(dx, dy)

    def North(self):    self.Step(0, 1)
    def East(self):     self.Step(1, 0)
    def South(self):    self.Step(0, -1)
    def West(self):     self.Step(-1, 0)
    def Wait(self):     self.Step(0, 0)
    def NorthEast(self): self.Step(1, 1)
    def SouthEast(self): self.Step(1,-1)
    def SouthWest(self): self.Step(-1,-1)
    def NorthWest(self): self.Step(-1,1)


class Moveable(MoveableBase):

    def __init__(self, x, y):
        super(Moveable, self).__init__(x, y)

    def Moves(self):
        return [Moveable.North, Moveable.East, Moveable.South, Moveable.West]


class Commandable(object):

    def __init__(self, commandGroup=CommandGroup()):
        self.commands = commandGroup.AsList()

    def Commands(self):
        return self.commands

    def Execute(self, command):
        return command.Execute(self)


class Utilitarian(Commandable):

    def __init__(self, commandGroup, strategy):
        super(Utilitarian, self).__init__(commandGroup)
        self.strategy = strategy

    def Utility(self):
        return self.Strategy().Utility(self)

    def Strategy(self, strategy=None):
        if not strategy:
            return self.strategy
        self.strategy = strategy

    def UtilityOfCommand(self, command):
        selfClone = deepcopy(self)
        selfClone.Execute(command)
        utility = selfClone.Utility()
        if not selfClone.IsValid():
            return None
        del selfClone
        return utility

    def OptimalCommand(self):
        optimalCommand, maxUtility = None, None
        for command in self.Commands():
            utility = self.UtilityOfCommand(command)
            if utility == None:
                continue
            if not optimalCommand or utility > maxUtility:
                optimalCommand, maxUtility = command, utility
        return optimalCommand

    def IsValid(self):
        return True


class Unit(Moveable, Utilitarian):

    def __init__(self, x, y, commandGroup, strategy):
        Moveable.__init__(self, x, y)
        Utilitarian.__init__(self, commandGroup, strategy)

