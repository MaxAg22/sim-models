from math import exp, log
from random import random


def gen_exponencial(l):
    u = 1 - random()
    return -log(u) / l


def gen_M(n_sim):
    v = 0
    for _ in range(n_sim):
        x1 = gen_exponencial(1)
        x2 = gen_exponencial(2)
        x3 = gen_exponencial(3)
        v += max(x1, x2, x3)
    return v / n_sim


def gen_m(n_sim):
    v = 0
    for _ in range(n_sim):
        x1 = gen_exponencial(1)
        x2 = gen_exponencial(2)
        x3 = gen_exponencial(3)
        v += min(x1, x2, x3)
    return v / n_sim


n = 10000
print(f"E[M]: {gen_M(n)}")

print(f"E[m]: {gen_m(n)}")
