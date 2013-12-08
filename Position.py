
class PositionBase(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def X(self):
        return self.x

    def Y(self):
        return self.y

    def XY(self):
        return self.x, self.y

    def DeltaXY(self, x, y):
        dx = x - self.X()
        dy = y - self.Y()
        return dx, dy

    def AdjustBy(self, dx, dy):
        self.x += dx
        self.y += dy

    def BlockDistanceToXY(self, x, y):
        dx, dy = self.DeltaXY(x, y)
        return abs(dx) + abs(dy)

    def KingDistanceToXY(self, x, y):
        pass

    def EuclidianDistanceToXY(self, x, y):
        pass


class Position(PositionBase):

    def Distance(self, x, y):
        return self.BlockDistanceToXY(x, y)


