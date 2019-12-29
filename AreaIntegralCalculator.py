# -*- coding: utf-8 -*-

from myFunctions import k

class AreaIntegralCalculator:
    def __init__(self, eArr, N):
        # eArr - lista funkcji bazowych
        self.eArr = eArr
        # N - ilość przedziałów, na które dzielę [-1,1] wzdłuż osi X, oraz wzdłuż osi Y
        self.N = N
    
    def compute(self, a, b):
        # eA, eB - 2 funkcje bazowe, używane w wyliczaniu elementu macierzy
        eA = self.eArr[a]
        eB = self.eArr[b]
        if( abs(eA.i - eB.i) + abs(eA.j - eB.j) > 1 ):
            return 0
        # else:
            # licze calke z definicji, na zbiorze [-1,1]x[-1,1]
        dx = float(2)/self.N
        dy = dx
        integral = 0
        for i in range(self.N):
            for j in range(self.N):
                dXeA = eA.dXf(i*dx-1, j*dy-1)
                dXeB = eB.dXf(i*dx-1, j*dy-1)
                dYeA = eA.dYf(i*dx-1, j*dy-1)
                dYeB = eB.dYf(i*dx-1, j*dy-1)

                # ze wzoru na element macierzy oraz dS = dx*dy
                integral += k(i*dx-1, j*dy-1) * (dXeA*dXeB + dYeA*dYeB) * dx*dy
        return integral
