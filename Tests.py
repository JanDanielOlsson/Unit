import unittest

from Position import Position
from Unit import Moveable, Commandable, Utilitarian, Unit
from Command import Command, CommandGroup
from Strategy import Strategy

class TestPosition(unittest.TestCase):

    def setUp(self):
        self.position = Position(5,5)

    def test_XY(self):
        self.assertEqual(self.position.XY(), (5,5))

    def test_AdjustBy(self):
        self.position.AdjustBy(4,-3)
        self.assertEqual(self.position.XY(), (9,2))

    def test_Distance(self):
        self.assertEqual(self.position.Distance(10,8), 8)


class TestMoveable(unittest.TestCase):

    def setUp(self):
        self.moveable = Moveable(5,5)

    def test_Step(self):
        self.moveable.North()
        self.assertEqual(self.moveable.XY(), (5,6))

    def test_Moves(self):
        moves = self.moveable.Moves()
        self.assertTrue(Moveable.North in moves)
        self.assertFalse(Moveable.NorthEast in moves)


class TestCommandable(unittest.TestCase):

    def setUp(self):
        class UnitClass(Commandable):
            def TestMethod(self):
                return 15
        self.unit = UnitClass()

    def test_Command(self):
        value = self.unit.Execute(Command('TestMethod'))
        self.assertEqual(value, 15)


class TestUtilitarian(unittest.TestCase):

    def setUp(self):
        class UnitStrategy(Strategy):
            def __init__(self):
                Strategy.__init__(self, self)

            def Utility(self, subject):
                return -subject.x*(subject.x-6)

        class UnitTestClass(Utilitarian):
            def __init__(self, strategy, commandGroup):
                super(UnitTestClass, self).__init__(strategy, commandGroup)
                self.x = 5

            def Increase(self):
                self.x += 1

            def Decrease(self):
                self.x -= 1

        commandGroup = CommandGroup([Command('Increase'), Command('Decrease')])
        strategy = UnitStrategy()
        self.unit = UnitTestClass(commandGroup, strategy)

    def test_MakeDecision(self):
        optimalCommand = self.unit.OptimalCommand()
        self.assertEqual(optimalCommand.Action(), 'Decrease')

class UnitStrategy(Strategy):
        def __init__(self, x, y):
            self.x, self.y = x, y
            Strategy.__init__(self, self)

        def Utility(self, subject):
            return -subject.Distance(self.x, self.y)

class TestUnit(unittest.TestCase):

    def setUp(self):
        commandGroup = CommandGroup([Command('West'), Command('East'), Command('Wait')])
        strategy = UnitStrategy(0, 5)
        self.unit = Unit(5, 5, commandGroup, strategy)

    def test_TestOptimalCommand(self):
        self.assertEqual(self.unit.OptimalCommand().Action(), 'West')
        self.assertEqual(self.unit.XY(), (5, 5))
        self.unit.Strategy(UnitStrategy(6, 5))
        self.assertEqual(self.unit.OptimalCommand().Action(), 'East')
        self.unit.Strategy(UnitStrategy(5, 5))
        self.assertEqual(self.unit.OptimalCommand().Action(), 'Wait')



if __name__ == '__main__':
    unittest.main()

