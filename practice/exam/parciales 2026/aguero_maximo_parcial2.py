from random import random
from math import log, exp


def varY():
    u = random()
    if u < 0.2:
        # k en {0,1,2,3,4}
        k = int(random() * 5)
        return 2 * k + 1
    else:
        # k en {1,2,3,4,5}
        k = int(random() * 5) + 1
        return 2 * k


def exponencial(_lambda):
    u = 1 - random()
    return -log(u) / _lambda


def rechazoX():
    c = 1.47
    while True:
        u = random()
        w = exponencial(1 / 3)
        if u < ((w**2) * exp(-0.5 * w)) / c:
            return w


# funcion auxiliar, genera Y ~ Bernoulli(0.4)
# genera una exponencial X ~ e(0.5)
def buscar_tesoro(p, l):
    y = 0
    u = random()
    e = exponencial(0.5)
    if u < p:
        y = 1
    return (y, e)


# ejercicio 4a
def jugador(p, l):
    intentos = 0
    tiempo_total = 0
    tesoro_encontrado = False
    while not tesoro_encontrado:
        y, t = buscar_tesoro(p, l)
        intentos += 1
        tiempo_total += t
        if y == 1:
            tesoro_encontrado = True
    return (intentos, tiempo_total)


# ejercicio 4b
def estimar_minutos_e_intentos(p, l, n_sim):
    total_minutos = 0
    total_intentos = 0
    for _ in range(n_sim):
        y, t = jugador(p, l)
        total_minutos += t
        total_intentos += y
    return (total_intentos / n_sim, total_minutos / n_sim)


# ejercicio 4c
def estimar_minutos_e_intentos_tres_o_mas(p, l, n_sim):
    total_minutos = 0
    total_intentos = 0
    for _ in range(n_sim):
        y, t = jugador(p, l)
        if y >= 3:
            total_minutos += t
            total_intentos += y
    return (total_intentos / n_sim, total_minutos / n_sim)


print(f"jugador: {jugador(0.4, 0.5)}")
r = estimar_minutos_e_intentos(0.4, 0.5, 10000)
print(f"Estimacion de minutos ~ {r[1]} estimacion de intentos ~ {r[0]}")

r = estimar_minutos_e_intentos_tres_o_mas(0.4, 0.5, 10000)
print(f"P(N >= 3) ~ {r[0]}")
