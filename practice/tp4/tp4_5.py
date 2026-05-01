from random import random
import time


def binomial(n,p):
    prob = (1-p)**n
    const = p / (1-p)
    u = random()
    F = prob
    i = 0
    while u >= F:
        prob *= const * (n-i)/(i+1)
        # actualizamos la acumulada
        F += prob
        i += 1
    return i


def trans_inv():
    u = random()
    if u < 0.35:
        return 3
    elif u < 0.55:
        return 4
    elif u < 0.75:
        return 1
    elif u < 0.90:
        return 0
    else: 
        return 2
    

def acept_rechazo():
    p =[0.15, 0.20, 0.10, 0.35, 0.20] 
    q =[0.0915, 0.2995, 0.3675, 0.2005, 0.0410]
    c = 4.88

    while True:
        y = binomial(4, 0.45)
        u = random()
        if u < p[y] / (c * q[y]):
            return y


def sim_trans_inv(n_sim):
    inicio = time.time()
    for _ in range(n_sim):
        trans_inv()
    fin = time.time()

    return fin - inicio

def sim_acept_rechazo(n_sim):
    inicio = time.time()
    for _ in range(n_sim):
        acept_rechazo()
    fin = time.time()

    return fin - inicio


n = 10000
tiempo_ti = sim_trans_inv(n)
tiempo_ar = sim_acept_rechazo(n)

print(f"Total de simulaciones: {n}")
print(f"Tiempo total TI: {tiempo_ti:.6f} segundos")
print(f"Tiempo total AR: {tiempo_ar:.6f} segundos")
