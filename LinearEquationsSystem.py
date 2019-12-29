# -*- coding: utf-8 -*-

from AreaIntegralCalculator import AreaIntegralCalculator
from CurveIntegralCalculator import CurveIntegralCalculator
import math
from myFunctions import print_vector

class LinearEquationsSystem:
    def __init__(self, eArr, N):
        self.M = len(eArr)
        self.areaIntCalc = AreaIntegralCalculator(eArr, N)
        self.curveIntCalc = CurveIntegralCalculator(eArr, N)
        self.matrix = [[0] * (self.M+1) for i in range(self.M)]
        self.prepareMatrix()

    
    def swap_row(self, i, j):
        for k in range(self.M+1):
            temp = self.matrix[i][k]
            self.matrix[i][k] = self.matrix[j][k]
            self.matrix[j][k] = temp

    def add_to_row(self, i, j, scalar):
        for k in range(self.M+1):
            self.matrix[i][k] += scalar * self.matrix[j][k]

    def print_matrix(self):
        for i in range(self.M):
            print_vector(self.matrix[i], 2)
        print ''

    # funkcja testująca dla danej macierzy
    def testSolve(self, matrix, M):
        self.matrix = matrix
        self.M = M
        self.print_matrix()
        self.solve()
        

    # obliczenie współczynników i wyrazów wolnych układu
    def prepareMatrix(self):
        for i in range(self.M):
            for j in range(self.M):
                self.matrix[i][j] = self.areaIntCalc.compute(j, i)
                
                # sprawdzenie postępów obliczeń
                # print str(i*self.M+j) + "/" + str(self.M*self.M)
            self.matrix[i][self.M] = self.curveIntCalc.compute(i)

    # doprowadzenie macierzy do postaci trójkątnej górnej
    def forwardElim(self):
        # self.print_matrix()
        for k in range(self.M):
            # sprawdzanie postępów obliczeń
            # print str(k) + "/" + str(self.M)

            # inicjalizacja początkowych wartośći pivota
            i_max = k
            v_max = self.matrix[i_max][k]

            # znajdź większego pivota
            for i in range(k+1, self.M):
                if abs(self.matrix[i][k]) > v_max:
                    v_max = self.matrix[i][k]
                    i_max = i
            
            # jeżeli element przekątnej głównej jest 0, to układ nie jest oznaczony
            if self.matrix[k][i_max] == 0:
                return k
            
            # wzrzucamy wiersz z największą wartością w danej kolumnie na przekątna główną
            if i_max != k:
                self.swap_row(k, i_max)
                # self.print_matrix()
            
            # zerujemy niższe rzędzy w tej kolumnie
            for i in range(k+1, self.M):
                # współczynnik f do wyzerowania k-tego elem. w i-tym rzędzie
                f = float(self.matrix[i][k])/self.matrix[k][k]                

                # jedziemy po calym rzędzie
                self.add_to_row(i, k, -f)

                # ustawiamy element [i][k] na zero, bo double jest niedokładny
                self.matrix[i][k] = 0
            
            # self.print_matrix()
        # zakończono powodzeniem - układ oznaczony
        return -1
    
    # wyliczenie wartości niewiadomych
    def backSub(self):
        x = [0 for i in range(self.M)]
        # liczymy od ostatniego równania do pierwszego
        for i in range(self.M-1, -1, -1):
            x[i] = self.matrix[i][self.M]

            # odejmujemy współczynniki które nie są na współrzędnej głównej, 
            # za pomocą kombinacji liniowej niższych rzędów
            for j in range(i+1, self.M):
                x[i] -= self.matrix[i][j] * x[j]
            
            # dzielimy rząd przez wartość elementu na prz. głównej, żeby dostać na niej 1
            x[i] = x[i]/self.matrix[i][i]
        # zwracam wektor rozwiązań
        return x
    
    # funkcja wywoływana przez użytkownika
    def solve(self):
        self.print_matrix()
        flag = self.forwardElim()
        if flag != -1:
            print("Układ nie jest oznaczony\n")
            return []
        return self.backSub()
