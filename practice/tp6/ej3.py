from scipy import stats
from math import sin, pi, sqrt
from random import random


def calculo_z(alpha):
    return stats.norm.ppf(1-alpha/2)


def f1(x):
    return sin(x)/x


def h1(y):
    return f1(pi + pi * y) * pi


def f2(x):
    return 3 / (3 + (x**4))


def h2(y):
    return f2(1/y - 1) / (y**2)


def monte_carlo(fun, n_min, alpha, L):          # L = ancho del intervalo
    moments = {}

    z_alpha_2 = calculo_z(alpha)                # 1.96
    d = L / (2 * z_alpha_2)
    media = fun(random())                       # x1
    scuad, n = 0, 1
    # mientras no se cumpla alguna de las condiciones mencionadas
    while n < n_min or sqrt(scuad/n) > d:

        if n == 1000 or n == 5000 or n == 7000:
            moments[n] = (media, scuad, intervalo(media, scuad, alpha, n))
        n = n + 1

        x = fun(random())           # Simular X2, X3, ..., XN
        media_ant = media
        media = media_ant + (x - media_ant) / n
        scuad = scuad * (1 - 1/(n-1)) + n * (media - media_ant)**2
    return media, scuad, n, moments


def intervalo(media, scuad, alpha, n):
    z_alpha_2 = stats.norm.ppf(1-alpha/2)
    std = sqrt(scuad/n)
    izq = media - z_alpha_2 * std
    der = media + z_alpha_2 * std
    intervalo = f"[{izq:.4f}, {der:.4f}]"
    return intervalo


n_min = 100
alpha = 0.05
L = 2 * 0.001
media, scuad, n, moments = monte_carlo(h1, n_min, alpha, L)

print('Valor real: ', -0.4338)
print('Estimación integral:', media)
print('Semi-ancho IC: ', stats.norm.ppf(1-alpha/2)*sqrt(scuad/n))
print('Cantidad de datos generados N_s: ', n)
print('Intervalo de confianza: ', intervalo(media, scuad, alpha, n))

print("=======momentos========")
print(f"Nsim=1000: Estimacion I ~ {moments[1000][0]}")
print(f"Nsim=1000: Estimacion S ~ {moments[1000][1]}")
print(f"Nsim=1000: IC (%95) = {moments[1000][2]}")

print(f"Nsim=5000: Estimacion I ~ {moments[5000][0]}")
print(f"Nsim=5000: Estimacion S ~ {moments[5000][1]}")
print(f"Nsim=5000: IC (%95) = {moments[5000][2]}")

print(f"Nsim=7000: Estimacion I ~ {moments[7000][0]}")
print(f"Nsim=7000: Estimacion S ~ {moments[7000][1]}")
print(f"Nsim=7000: IC (%95) = {moments[7000][2]}")

media1, scuad1, n1, moments1 = monte_carlo(h2, n_min, alpha, L)

print('Valor real: ', 1.4618)
print('Estimación integral:', media1)
print('Semi-ancho IC: ', stats.norm.ppf(1-alpha/2)*sqrt(scuad1/n1))
print('Cantidad de datos generados N_s: ', n1)
print('Intervalo de confianza: ', intervalo(media1, scuad1, alpha, n1))

print("=======momentos========")
print(f"Nsim=1000: Estimacion I ~ {moments1[1000][0]}")
print(f"Nsim=1000: Estimacion S ~ {moments1[1000][1]}")
print(f"Nsim=1000: IC (%95) = {moments1[1000][2]}")

print(f"Nsim=5000: Estimacion I ~ {moments1[5000][0]}")
print(f"Nsim=5000: Estimacion S ~ {moments1[5000][1]}")
print(f"Nsim=5000: IC (%95) = {moments1[5000][2]}")

print(f"Nsim=7000: Estimacion I ~ {moments1[7000][0]}")
print(f"Nsim=7000: Estimacion S ~ {moments1[7000][1]}")
print(f"Nsim=7000: IC (%95) = {moments1[7000][2]}")
