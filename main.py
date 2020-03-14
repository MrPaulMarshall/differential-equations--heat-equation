# -*- coding: utf-8 -*-

from BaseFunction import BaseFunction
from LinearEquationsSystem import LinearEquationsSystem
from Solution import Solution
from myFunctions import printVector


# 2n+1 piramid wzdłuż każdej osi
n = 1

# Lista funkcji bazowych -> piramid
eArr = []

# pomija piramidy na brzegu Dirichleta
#   piramidy o środkach poniżej osi OX
for j in range(-n, 0):
    for i in range(-n, n+1):
        eArr.append( BaseFunction(n, i, j) )
#   piramidy o środkach powyżej osi OX, na lewo od osi OY
for j in range(0, n+1):
    for i in range(-n, 0):
        eArr.append( BaseFunction(n, i, j) )


# dopisuje piramidy na brzegu Dirichleta
#   na środku układu
#eArr.append( BaseFunction(n, 0, 0) )
#   wzdłuż osi OY
#for i in range(1, n+1):
#    eArr.append( BaseFunction(n, 0, i) )
#   wzdłuż osi OX
#for i in range(1, n+1):
#    eArr.append( BaseFunction(n, i, 0) )


# przygotowanie macierzy, podaje tu dla jakiej ilości podziałów chcę liczyć całki
systemSolver = LinearEquationsSystem(eArr, 100)

# obliczanie wektora współczynników
x = systemSolver.solve()

# wypisanie wektora, w celu sprawdzenia;
# print_vector(x, 2)

# stworzenie rozwiązania, mając funkcje bazowe i współczynniki
u = Solution(eArr, x)

u.draw_graph()
