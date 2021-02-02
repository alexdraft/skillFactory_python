class Rectangle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def __str__(self):
        return "Прямоугольник ("+str(self.x)+", "+str(self.y)+", "+str(self.width)+", "+str(self.height)+")"


r_1 = Rectangle(10, 10, 9, 6)
print(str(r_1))
