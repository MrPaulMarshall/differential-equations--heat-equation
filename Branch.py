# -*- coding: utf-8 -*-

class Branch:
    # poszczególne gałęzie - ściany piramid - mają postać:
    # f(x, y) = (aX*x + bX) * (aY*y + bY)
    def __init__(self, aX, bX, aY, bY):
        self.aX = aX
        self.bX = bX
        self.aY = aY
        self.bY = bY
    
    def f(self, x, y):
        return (self.aX*x + self.bX)*(self.aY*y + self.bY)
    
    def dXf(self, x, y):
        return self.aX*(self.aY*y + self.bY)
    
    def dYf(self, x, y):
        return self.aY*(self.aX*x + self.bX)
