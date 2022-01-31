'''
    Walmart Question 10: Generate Random point in a Circle

Given the radius and the position of the center of a circle, implement the function randPoint which generates a uniform random point inside the circle.
Implement the Solution class:
Solution(double radius, double x_center, double y_center) initializes the object with the radius of the circle radius and the position of the center (x_center, y_center).
randPoint() returns a random point inside the circle. A point on the circumference of the circle is considered to be in the circle. The answer is returned as an array [x, y].

'''
import math
import random
class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.r = radius
        self.cx = x_center
        self.cy = y_center

    def randPoint(self):
        randRadius = self.r * math.sqrt(random.random())
        randAngle = 2 * math.pi * random.random()
        x = self.cx + randRadius * math.cos(randAngle)
        y = self.cy + randRadius * math.sin(randAngle)
        return [x, y]