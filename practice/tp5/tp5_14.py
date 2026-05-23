from random import random
from math import log


def lamda1(t):
    return 3 + (4 / (t + 1))


def lamda2(t):
    return (t - 2) ** 2 - 5 * t + 17


def lamda3(t):
    if 2 <= t <= 3:
        return (t / 2) - 1
    elif 3 <= t <= 6:
        return 1 - (t / 6)
    return 0


def poisson_no_homogeneo_adelgazamiento(lamda, T, lamda_t):
    """Devuelve el número de eventos NT y los tiempos en Eventos"""
    NT = 0
    Eventos = []
    u = 1 - random()
    t = -log(u) / lamda
    while t <= T:
        v = random()
        if v < lamda_t(t) / lamda:
            NT += 1
            Eventos.append(t)
        t += -log(1 - random()) / lamda
    return NT, Eventos


def poisson_no_homogeneo_mejorado(T=3):
    # Definición de subintervalos y sus cotas locales
    interv = [3, 4, 7]
    lambdas = [7, 5, 4.3333]

    j = 0  # Índice del intervalo actual
    t = -log(1 - random()) / lambdas[j]
    NT = 0
    eventos = []

    while t <= T:
        if t <= interv[j]:
            # Algoritmo de adelgazamiento estándar dentro del intervalo
            v = random()
            intensidad_t = 3 + 4 / (t + 1)

            if v < intensidad_t / lambdas[j]:
                NT += 1
                eventos.append(t)

            t += -log(1 - random()) / lambdas[j]
        else:
            # Salto al siguiente intervalo aprovechando la exponencial generada [5]
            if j < len(lambdas) - 1:
                t = interv[j] + (t - interv[j]) * lambdas[j] / lambdas[j + 1]
                j += 1
            else:
                break  # Fin del tiempo total T

    return NT, eventos


n_eventos, tiempos = poisson_no_homogeneo_mejorado()
print(f"Número de eventos: {n_eventos}")
print(f"Tiempos: {tiempos}")
