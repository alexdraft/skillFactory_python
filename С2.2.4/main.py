class Square:
    def __init__(self, side):
        self.side = side

    def get_area(self):
         return self.side ** 2

class SquareFactory:

    @staticmethod
    def square_maker(side):
        return Square(side)

sq_1 = SquareFactory.square_maker(5)
print(sq_1.get_area())