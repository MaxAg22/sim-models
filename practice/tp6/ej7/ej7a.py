from ej7 import ejercicio_7
from math import sqrt


def monte_carlo(fun, n_min, d):
    val = fun(100)[4]
    media = val
    scuad, n = 0, 1
    while n < n_min or sqrt(scuad / n) > d:
        n += 1
        x = fun(100)[4]
        val += x
        media_ant = media
        media = media_ant + (x - media_ant) / n
        scuad = scuad * (1 - 1 / (n - 1)) + n * (media - media_ant) ** 2
    return media, scuad, n, val / n


print(monte_carlo(ejercicio_7, 1000, 0.01)[3])
