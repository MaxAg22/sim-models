from ej8a import ejercicio_8
from math import sqrt


def monte_carlo(fun, n_min, d):
    tiempo_total = 100
    val = fun(tiempo_total)[5]
    media = val
    scuad, n = 0, 1
    while n < n_min or sqrt(scuad / n) > d:
        n += 1
        x = fun(tiempo_total)[5]
        val += x
        media_ant = media
        media = media_ant + (x - media_ant) / n
        scuad = scuad * (1 - 1 / (n - 1)) + n * (media - media_ant) ** 2
    return media, scuad, n, val / n


print(monte_carlo(ejercicio_8, 10000, 0.05)[3])
