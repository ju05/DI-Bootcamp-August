
class Circle:
    def __init__(self, radius=0, diameter=0):
        self.radius = radius
        self.diameter = diameter

    @classmethod
    def from_radius(cls, radius):
        return cls(radius = radius, diameter = radius *2)

c1 = Circle.from_radius(5)
print(c1.diameter)