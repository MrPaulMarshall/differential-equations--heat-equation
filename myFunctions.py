# -*- coding: utf-8 -*-

import math

# funkcje pomocnicze:
    # k(x, y) - współczynnik przeływu
def k(x, y):
    if y > 0.5 and y <= 1:
        return 2
    else:
        return 1

    # g(x, y) - pochodna normalna na brzegu Neumanna
def g(x, y):
    return (x**2)**(1.0/3)

# zaokrąglenie do n miejsc po przecinku
def round(x, n):
    power = 1
    for i in range(n):
        power *= 10
    return math.floor(power * x) / power

# funkcja do wypisania wektora z zadaną dokładnością
def print_vector(vec, n):
    print map(lambda a: round(a, 2), vec)
