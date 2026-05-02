"""Ej-9"""
import random


def trans_inv_geom(p):
    """genera una v.a geometrica con el método de transformada inversa"""
    prob = p
    acumulada = p
    i = 1
    u = random.random()
    while u >= acumulada:
        i += 1
        prob *= (1-p)
        acumulada += prob
    return i


def geometrica_directa(p):
    """genera una v.a geometrica muy directo"""
    k = 1
    while True:
        u = random.random()
        if u <= p:
            return k
        k += 1


def sim_geometrica_trans_inv(p, n_sim):
    """simula una v.a geometrica con TI y da el promedio de valores generados"""
    acum = 0
    for _ in range(n_sim):
        valor = trans_inv_geom(p)
        acum += valor

    return acum/n_sim


def sim_geometrica_directa(p, n_sim):
    """simula una v.a geometrica a lo bestia y da el promedio de valores generados"""
    acum = 0
    for _ in range(n_sim):
        valor = geometrica_directa(p)
        acum += valor

    return acum/n_sim


n = 1000
r1 = sim_geometrica_directa(0.8, n)
r2 = sim_geometrica_trans_inv(0.8, n)
r3 = sim_geometrica_directa(0.2, n)
r4 = sim_geometrica_trans_inv(0.2, n)

print(f"p = 0.8 Promedio con método directo: {r1}")
print(f"p = 0.8 Promedio con método TI: {r2}")
print(f"p = 0.2 Promedio con método directo: {r3}")
print(f"p = 0.2 Promedio con método TI: {r4}")
