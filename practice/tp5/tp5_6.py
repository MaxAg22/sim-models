from random import random
from time import time


def trans_inv(n):
    u = random()
    return u ** (1 / n)


def AyR(n):
    f = lambda x: n * (x ** (n - 1))
    while 1:
        y = random()
        u = random()
        if u < f(y) / n:
            return y


def maximo(n):
    u_array = [random() for _ in range(n)]
    return max(u_array)


def calcular_tiempo_ti(n_sim, n):
    ti_inicio = time()
    for _ in range(n_sim):
        trans_inv(n)
    ti_final = time()
    return ti_final - ti_inicio


def calcular_tiempo_ayr(n_sim, n):
    ayr_inicio = time()
    for _ in range(n_sim):
        AyR(n)
    ayr_final = time()
    return ayr_final - ayr_inicio


def calcular_tiempo_max(n_sim, n):
    max_inicio = time()
    for _ in range(n_sim):
        maximo(n)
    max_final = time()
    return max_final - max_inicio


n_sim = 10000
n = 1000
print(f"Tiempo aprox. transformada inversa: {calcular_tiempo_ti(n_sim, n):.2}")
print(f"Tiempo aprox. aceptacion y rechazo: {calcular_tiempo_ayr(n_sim, n):.2}")
print(f"Tiempo aprox. maximo: {calcular_tiempo_max(n_sim, n):.2}")
