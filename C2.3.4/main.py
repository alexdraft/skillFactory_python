class Square:
    _side = 1

    @property
    def area(self):
        return self.side ** 2

    @property
    def side(self):
        return self._side

    @side.setter
    def side(self, value):
        if value >= 0:
            self._side = value
        else:
            raise ValueError("Side must be positive")


sq_1 = Square()
print(sq_1.area)
sq_1.side = 20
print(sq_1.area)
