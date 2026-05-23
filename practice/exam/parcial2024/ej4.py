from random import random
from math import log


def tirar_moneda(p):
    u = random()
    if u < p:
        return 1
    return 0


def simular_experimento(p):
    neutro = 100
    i = 1
    results = [neutro]
    while True:
        x = tirar_moneda(p)
        results.append(x)
        if results[i-1] != results[i] and results[i-1] != neutro:
            return len(results) - 1
        i += 1


def estimar_prob(x, p, n_sim):
    count = 0
    for _ in range(n_sim):
        r = simular_experimento(p)
        if r == x:
            count += 1
    return count / n_sim


print(f"P(X = 4) ~ {estimar_prob(4, 1/3, 10000):.4f}")


# ej 4b)

def geom(p):
    u = random()
    return int(log(1-u)/log(1-p)) + 1  # o aca poner + 2


def p(j):
    if j < 2:
        return 0
    return ((2 ** (j-1)) + 2) / (3 ** j)


def q(j): return (1/3) * ((2/3) ** (j - 1))


def generar_x(p_geom):
    while True:
        y = geom(p_geom)
        u = random()
        if u < p(y) / (q(y) * 2):
            return y


def estimar_con_aceptacion_rechazo(p_geom, n_sim):
    count = 0
    for _ in range(n_sim):
        x = generar_x(p_geom)
        if x == 4:
            count += 1
    return count / n_sim


print(f"AyR: P(X = 4) ~ {estimar_con_aceptacion_rechazo(1/3, 10000):.4f}")
