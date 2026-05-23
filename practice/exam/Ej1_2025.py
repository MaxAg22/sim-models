from random import random


def ejercicio1():
    while True:
        Y = random()
        U = random()
        if U < 16 * (Y**2) * (1 - (2 * Y) + (Y**2)):
            return Y


def sim_ejercicio1(n_sim):
    count = 0
    for _ in range(n_sim):
        x = ejercicio1()
        count += x
    return count / n_sim


def ejercicio2(p):
    U = random()
    i = 10
    prob = p
    F = p
    while U >= F:
        i += 1
        prob *= 1 - p
        F += prob
    return i


def sim_ejercicio2(n_sim, p):
    count = 0
    for _ in range(n_sim):
        x = ejercicio2(p)
        count += x
    return count / n_sim


n = 10000
print(f"ej1: E[X] ~ {sim_ejercicio1(n):.4f}")
print(f"ej2: E[X] ~ {sim_ejercicio2(n, 0.5):.4f}")
