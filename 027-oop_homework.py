# OOP - Homework

# Problem 1:Fill in the Line class methods to accept coordinate as a pair of tuples and return the slope and distance of the line

# Example Output:
# coordinate1 = (3, 2)
# coordinate2 = (8, 10)
# distance = 9.433981132056603
# slope = 1.6

import math

class Line(object):

    def __init__(self, coord1, coord2):
        self.coord1 = coord1
        self.coord2 = coord2

    def distance(self):
        x1, y1 = self.coord1
        x2, y2 = self.coord2
        
        distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
        print("Distance:", distance)

    def slope(self):
        x1, y1 = self.coord1
        x2, y2 = self.coord2

        slope = float((y2 - y1)) / (x2 - x1)
        print("Slope:", slope)

li = Line([3, 2], [8, 10])
li.distance()
li.slope()
print()

# Problem 2: Fill in the class:

# Example Output:
# volume: 56.54
# surface_area: 94.21

class Cylinder(object):

    def __init__(self, height = 1, radius = 1):
        self.height = height
        self.radius = radius

    def volume(self):
        volume = self.height * (math.pi) * (self.radius) ** 2
        print("Volume:", volume)

    def surface_area(self):
        top = (3.14) * (self.radius) ** 2
        surface = 2 * top + 2 * math.pi * self.radius * self.height
        print("Surface Area:", surface)

c = Cylinder(2, 3)
c.volume()
c.surface_area()