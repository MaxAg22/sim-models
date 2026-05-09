from random import random
import math


def generar_W():
    u = random()
    if u < 0.5:
        return 1
    elif u < 0.8:
        return 2
    else:
        return 3


def gen_exp():
    w = generar_W()
    if w == 1:
        m = 3
    elif w == 2:
        m = 5
    else:
        m = 7
    u = 1 - random()
    return -m * math.log(u)


def sim_exp(n_sim):
    acum = 0
    for _ in range(n_sim):
        exp = gen_exp()
        acum += exp
    return acum / n_sim


n = 10000
r = sim_exp(n)
print(f"La esperanza estimada es {r:.4}")
