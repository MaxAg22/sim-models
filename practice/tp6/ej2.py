from random import random
from math import sqrt, exp


def f(u):
    return exp(u) / sqrt(2 * u)


def g(x):
    return (x ** 2) * exp(-(x**2))


def h(y):
    return (g(1 - 1/y) * (1/(y**2))) + (g((1/y) - 1) * (1/(y**2)))


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
    return media, scuad, n, val / n


media, scuad, n, integral = monte_carlo(f, 100, 0.01)
print(f"Integral ~ {integral:.4f}")
print(f"Media ~ {media:.4f}")
print(f"Scuad ~ {scuad:.4f}")
print(f"n ~ {n:.4f}")

media, scuad, n, integral = monte_carlo(h, 100, 0.01)
print(f"Integral ~ {integral:.4f}")
print(f"Media ~ {media:.4f}")
print(f"Scuad ~ {scuad:.4f}")
print(f"n ~ {n:.4f}")
