from math import exp, log, sqrt
from random import random
from time import time


def suma():
    u = random()
    v = random()
    return u + v


def inversa():
    u = random()
    if u < 0.5:
        return sqrt(2 * u)
    else:
        return 2 - sqrt(2 - 2 * u)


def f(x):
    if 0 <= x < 1:
        return x
    elif 1 <= x < 2:
        return 2 - x
    else:
        return 0


def aceptacion_rechazo():
    while True:
        y = random() * 2
        u = random()
        if u < f(y):
            return y


def sim_suma(n_sim):
    prom = 0
    casos_mayores = 0
    inicio = time()
    for _ in range(n_sim):
        x = suma()
        if x > 1.5:
            casos_mayores += 1
        prom += x
    final = time()
    return (final - inicio, prom / n_sim, casos_mayores / n_sim)


def sim_inversa(n_sim):
    prom = 0
    casos_mayores = 0
    inicio = time()
    for _ in range(n_sim):
        x = inversa()
        if x > 1.5:
            casos_mayores += 1
        prom += x
    final = time()
    return (final - inicio, prom / n_sim, casos_mayores / n_sim)


def sim_aceptacion_rechazo(n_sim):
    prom = 0
    casos_mayores = 0
    inicio = time()
    for _ in range(n_sim):
        x = aceptacion_rechazo()
        if x > 1.5:
            casos_mayores += 1
        prom += x
    final = time()
    return (final - inicio, prom / n_sim, casos_mayores / n_sim)


n = 10000
r1 = sim_inversa(n)
r2 = sim_aceptacion_rechazo(n)
r3 = sim_suma(n)
print(f"Transformada inversa E[X] = {r1[1]} y tiempo aprox: {r1[0]:.4f}")
print(f"Proporcion de P(X > x0): {r1[2]}")
print(f"Aceptación rechazo E[X] = {r2[1]} y tiempo aprox: {r2[0]:.4f}")
print(f"Proporcion de P(X > x0): {r2[2]}")
print(f"Suma E[X] = {r3[1]} y tiempo aprox: {r3[0]:.4f}")
print(f"Proporcion de P(X > x0): {r3[2]}")
