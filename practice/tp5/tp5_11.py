from math import tan, pi
from random import random
from time import time


def inversa_cauchy(lamda):
    u = random()
    return lamda * tan(pi * (u - 0.5))


def sim_cauchy(lamda, n_sim):
    aciertos = 0
    inicio = time()
    for _ in range(n_sim):
        x = inversa_cauchy(lamda)
        if -lamda < x < lamda:
            aciertos += 1
    fin = time()
    return (aciertos / n_sim, fin - inicio)


r1 = sim_cauchy(1, 10000)
r2 = sim_cauchy(2.5, 10000)
r3 = sim_cauchy(0.3, 10000)
print(f"Aciertos: {r1[0]} con tiempo: {r1[1]}")
print(f"Aciertos: {r2[0]} con tiempo: {r2[1]}")
print(f"Aciertos: {r3[0]} con tiempo: {r3[1]}")
