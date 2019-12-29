# -*- coding: utf-8 -*-

from myFunctions import k, g

class CurveIntegralCalculator:
    # eArr - lista funkcji bazowych
    # N - ilość podziałów -> dokładność liczenia całki
    def __init__(self, eArr, N):
        self.eArr = eArr
        self.N = N

    # liczenie całki po prostej wzdłuż osi X, dla ustalonego Y = y
    def computeDueToX(self, i, y, a, b):
        dx = float(b - a)/self.N
        integral = 0
        for j in range(self.N):
            # mnożę razy abs(dx), bo całka jest nieskierowana
            integral += k(a + j*dx, y) * g(a + j*dx, y) * self.eArr[i].f(a + j*dx, y) * abs(dx)
        return integral
    
    # liczenie całki po prostej wzdłuż osi Y, dla ustalonego X = x
    def computeDueToY(self, i, x, a, b):
        # dla naszego brzegu (x^2)^(1/3) = 1
        dy = float(b - a)/self.N
        integral = 0
        for j in range(self.N):
            # mnożę razy abs(dy), bo całka jest nieskierowana
            integral += k(x, a + j*dy) * g(x, a + j*dy) * self.eArr[i].f(x, a + j*dy) * abs(dy)
        return integral

    # sumuję całki po fragmentach brzegu, idąc zgodnie ze wskazówkami zegara
    def compute(self, i):
        return self.computeDueToY(i, 1, 0, -1) + self.computeDueToX(i, -1, 1, -1) + self.computeDueToY(i, -1, -1, 1) + self.computeDueToX(i, 1, -1, 0)
