# -*- coding: utf-8 -*-

# do rysowania wykresu
import matplotlib.pyplot as plt
import numpy as np

class Solution:
    # eArr - lista funkcji bazowych
    # M - długośc tej listy
    # vec - lista obliczonych współczynników
    def __init__(self, eArr, vec):
        self.eArr = eArr
        self.vec = vec
        if(len(eArr) == len(vec)):
            self.M = len(eArr)
        else:
            raise RuntimeError, "Niezgodna ilość funkcji i współczynników"

    # oblicz wartość funkcji
    def f(self, x, y):
        sum = 0
        for i in range(self.M):
            sum += self.vec[i] * self.eArr[i].f(x, y)
        return sum

    # pochodne cząstkowe
    def dXf(self, x, y):
        sum = 0
        for i in range(self.M):
            sum += self.vec[i] * self.eArr[i].dXf(x, y)
        return sum
    def dYf(self, x, y):
        sum = 0
        for i in range(self.M):
            sum += self.vec[i] * self.eArr[i].dYf(x, y)
        return sum

    # rysowanie wykresu
    def draw_graph(self):
        # ilość pikseli wzdłuż jednej osi układu
        n = 500

        # macierz wartości Z
        Z = [[0] * n for i in range(n)]

        dx = float(2) / n
        dy = dx

        for i in range(n):
            for j in range(n):
                Z[i][j] = self.f(-1 + i*dx, -1 + j*dy)

        z_min, z_max = -np.abs(Z).max(), np.abs(Z).max()

        # generate 2 2d grids for the X & Y bounds
        Y, X = np.meshgrid(np.linspace(-1, 1, n), np.linspace(-1, 1, n))

        fig, ax = plt.subplots()

        # kolorowanie bwr
        c = ax.pcolormesh(X, Y, Z, cmap='bwr', vmin=z_min, vmax=z_max)

        # kolorowanie od białych
        # c = ax.pcolormesh(X, Y, Z, cmap='coolwarm', vmin=z_min, vmax=z_max)

        # kolorowanie od niebieskich
        # c = ax.pcolormesh(X, Y, Z, cmap='coolwarm', vmin=0.0, vmax=z_max)

        ax.set_title('pcolormesh')
        # set the limits of the plot to the limits of the data
        ax.axis([X.min(), X.max(), Y.min(), Y.max()])
        fig.colorbar(c, ax=ax)

        plt.show()
