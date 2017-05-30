# OOP - Methods

class Circle(object):

    # class object attributes
    pi = 3.14

    def __init__(self, radius = 1):
        self.radius = radius
    
    def area(self):
        return (self.radius ** 2) * Circle.pi

    def set_radius(self, new_radius):
        """ This method takes in a radius and resets the current radius of the Circle. """
        self.radius = new_radius

    def get_radius(self):
        return self.radius

c = Circle(radius = 100)
print("Radius:", c.radius)
print("Area:", c.area())

c.set_radius(20)
print("Radius:", c.get_radius())
print("Area:", c.area())
    