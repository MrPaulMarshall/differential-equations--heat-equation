# -*- coding: utf-8 -*-

from Branch import *

class BaseFunction:
    # i, j należą do {-n, -(n-1), ..., 0, 1, ..., n}
    #   są to indeksy, które mówią o ile wielokrotności liczby 1/n przesuwamy wierzchołek piramidy względem punktu (0, 0)
    #   i - wzdłuż osi X
    #   j - wzdłuż osi Y

    # funkcja ma 4 gałęzie - ściany piramidy
    #   oraz wynosi 0 dla punktów poza piramidą
    def __init__(self, n, i, j):
        self.n = n
        self.i = i
        self.j = j
        # braches -> lista gałęzi, żeby łatwo obliczać wartość funkcji
        self.branches = [
            # poniższe wartości współczynników policzyłem na kartce
            Branch( 0,   0,  0,   0),
            Branch(-n, 1+i, -n, 1+j),
            Branch( n, 1-i, -n, 1+j),
            Branch( n, 1-i,  n, 1-j),
            Branch(-n, 1+i,  n, 1-j)
        ]
    
    # sprawdza czy (x, y) jest poza zadanym obszarem
    def outsideOmega(self, x, y):
        if x < -1 or y < -1 or x > 1 or y > 1:
            return True
        if x > 0 and y > 0:
            return True
        else:
            return False
    
    # zwraca indeks podobszaru dziedziny, do której należy (x, y)
    def getSubArea(self, x, y):
        if self.outsideOmega(x, y) == True:
            return 0
        i = float(self.i)
        j = float(self.j)
        n = self.n

        # poniższe warunki określają odpowiednie trójkąty wokół wierzchołka piramidy
        if   x >= i/n and y >= j/n and y <  -x + (i+j+1)/n:
            return 1
        elif x <  i/n and y >= j/n and y <   x + (j-i+1)/n:
            return 2
        elif x <  i/n and y <  j/n and y >= -x + (i+j-1)/n:
            return 3
        elif x >= i/n and y <  j/n and y >=  x + (j-i-1)/n:
            return 4
        else:
            return 0

    # zwracanie wartości odpowiednio funkcji i jej pochodnych cząstkowych
    def f(self, x, y):
        return self.branches[ self.getSubArea(x,y) ].f(x,y)

    def dXf(self, x, y):
        return self.branches[ self.getSubArea(x,y) ].dXf(x,y)

    def dYf(self, x, y):
        return self.branches[ self.getSubArea(x,y) ].dYf(x,y)
