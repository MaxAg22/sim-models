from math import exp, log
from random import random
from time import time


def inversa():
    u = random()
    return exp(u)


def aceptacion_rechazo():
    e = exp(1)
    f = lambda x: 1 / x
    g = 1 / (e - 1)
    while True:
        y = random() * (e - 1) + 1
        u = random()
        if u < 1 / y:
            return y


def sim_inversa(n_sim):
    prom = 0
    inicio = time()
    for _ in range(n_sim):
        x = inversa()
        prom += x
    final = time()
    return (final - inicio, prom / n_sim)


def sim_aceptacion_rechazo(n_sim):
    prom = 0
    inicio = time()
    for _ in range(n_sim):
        x = aceptacion_rechazo()
        prom += x
    final = time()
    return (final - inicio, prom / n_sim)


def ti_estimar_acumulada(x, n_sim):
    exitos = 0
    for _ in range(n_sim):
        y = inversa()
        exitos += 1 if y <= x else 0
    return exitos / n_sim


def ar_estimar_acumulada(x, n_sim):
    exitos = 0
    for _ in range(n_sim):
        y = aceptacion_rechazo()
        exitos += 1 if y <= x else 0
    return exitos / n_sim


n = 10000
r1 = sim_inversa(n)
r2 = sim_aceptacion_rechazo(n)
print(f"Transformada inversa E[X] = {r1[1]} y tiempo aprox: {r1[0]:.4f}")
print(f"Aceptación rechazo E[X] = {r2[1]} y tiempo aprox: {r2[0]:.4f}")

r11 = ti_estimar_acumulada(2, 10000)
r22 = ar_estimar_acumulada(2, 10000)
print(f"Transformada inversa - P(X <= 2) = {r11}")
print(f"Aceptación rechazo - P(X <= 2) = {r22}")
