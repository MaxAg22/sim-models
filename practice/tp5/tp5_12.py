from random import random
from math import log


def calcular_eventos_y_tiempo(T, lamda):
    tiempo_total = 0
    cantidad_eventos = 0
    eventos = []
    while tiempo_total < T:
        u = 1 - random()
        tiempo_total += -log(u) / lamda
        if tiempo_total <= T:
            cantidad_eventos += 1
            eventos.append(tiempo_total)
    return cantidad_eventos, eventos
