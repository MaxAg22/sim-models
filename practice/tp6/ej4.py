from random import random, uniform
from math import sqrt
from scipy import stats


def en_el_circulo():
    u = uniform(-1, 1)
    v = uniform(-1, 1)
    if u**2+v**2 <= 1:
        return 1
    else:
        return 0


def ejercicio_6a(d):
    p = 0
    n = 0
    while n <= 100 or sqrt(p*(1-p)/n) > d:
        n += 1
        x = en_el_circulo()
        p += (x-p) / n
    return p, n


d = 0.01
p, n = ejercicio_6a(d)

print('Ejercicio a:')
print('Estimación de proporción: ', p)
print('Estimación de pi: ', 4*p)    # Multiplico por 4 por el teórico de arriba
print('Número de simulaciones: ', n)


def ejercicio_6b(L=0.1, alpha=0.05):
    z_alpha_2 = stats.norm.ppf(1-alpha/2)
    cota = L / (4 * 2 * z_alpha_2)

    n = 0
    p = 0

    while n <= 100 or sqrt(p * (1-p) / n) > cota:
        n += 1
        X = en_el_circulo()
        p = p + (X - p) / n

    pi_est = 4 * p
    error = z_alpha_2 * 4 * sqrt(p * (1-p) / n)
    IC = (pi_est - error, pi_est + error)

    print(f"Estimación de pi = {pi_est}")
    print(f"Intervalo de confianza 95% = {IC}")
    print(f"Amplitud del intervalo maxima = {L}")
    print(f"Amplitud del intervalo = {2 * error}")
    print(f"Número de simulaciones = {n}")

    return pi_est, IC, n


print("Inciso b)")
print("\nAmplitud del IC < 0.1")
res1 = ejercicio_6b(L=0.1, alpha=0.05)

print("\nAmplitud del IC < 0.05")
res2 = ejercicio_6b(L=0.05, alpha=0.05)

print("\nAmplitud de IC < 0.001")
res3 = ejercicio_6b(L=0.001, alpha=0.05)
