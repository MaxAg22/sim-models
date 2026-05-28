from random import random
from math import sqrt, exp


def f(u):
    return exp(u) / sqrt(2 * u)


def monte_carlo(fun, n_min, d):
    val = fun(random())
    media = val
    scuad, n = 0, 1
    while n < n_min or sqrt(scuad / n) > d:
        n += 1
        u = random()
        x = fun(u)
        val += x
        media_ant = media
        media = media_ant + (x - media_ant) / n
        scuad = scuad * (1 - 1 / (n - 1)) + n * (media - media_ant) ** 2
    return media, scuad, n


res = monte_carlo(f, 100, 0.01)
print(f"Integral ~ {res}")
