"""Ej7"""
from random import random
from time import time
from math import exp


def poisson(_lambda):
    """genera una v.a Poisson"""
    u = random()
    i = 0
    p = exp(-_lambda)
    f = p
    while u >= f:
        i += 1
        p *= _lambda / i
        f += p
    return i


def poisson_mejorado(_lambda):
    """genera una v.a Poisson - version mejorada"""
    p = exp(-_lambda)
    f = p
    # calculamos (lamba ** (lambda + 1)) / (lambda + 1)!
    for j in range(1, int(_lambda) + 1):
        p *= _lambda / j
        f += p
    u = random()
    if u >= f:
        j = int(_lambda) + 1
        while u >= f:
            p *= _lambda / j
            f += p
            j += 1
        return j - 1
    # else
    j = int(_lambda)
    while u < f:
        f -= p
        p *= j / _lambda
        j -= 1
    return j + 1


def sim_poisson(n_sim):
    """simula y calcula el promedio de veces que sale Y > 2"""
    count = 0
    inicio = time()
    for _ in range(n_sim):
        y = poisson(10)
        count += 1 if y > 2 else 0
    fin = time()
    return (count/n_sim, fin - inicio)


def sim_poisson_mejorado(n_sim):
    """simula y calcula el promedio de veces que sale Y > 2 con Poisson mejorado"""
    count = 0
    inicio = time()
    for _ in range(n_sim):
        y = poisson_mejorado(10)
        count += 1 if y > 2 else 0
    fin = time()
    return (count/n_sim, fin - inicio)


n = 1000
result = sim_poisson(n)
result1 = sim_poisson_mejorado(n)
print("\n*** Ejercicio 7 ***")
print("N° de sim = 1000")
print(f"""Estimación P(Y > 2) poisson normal ~ {result[0]}
      Tiempo de ejecución: {result[1]} segundos""")

print(f"""Estimación P(Y > 2) poisson normal ~ {result1[0]}
      Tiempo de ejecución: {result1[1]} segundos""")
