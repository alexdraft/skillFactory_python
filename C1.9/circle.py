class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_radius(self):
        return self.radius

    def get_area(self):
        return 3.1415 * self.radius ** 2
