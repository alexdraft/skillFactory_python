class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def get_area(self):
        return self.width * self.height


r_1 = Rectangle(5, 12)
print("r_1.get_width =", r_1.get_width())
print("r_1.get_height = ", r_1.get_height())
