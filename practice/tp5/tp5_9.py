from math import log, sqrt, cos, sin, pi, exp
from random import random


# genera una v.a normal estándar
def Normal_rechazo(mu, sigma):
    while True:
        y1 = -log(1 - random())
        y2 = -log(1 - random())
        if y2 >= (y1 - 1) ** 2 / 2:
            if random() < 0.5:
                return y1 * sigma + mu
            return -y1 * sigma + mu


# genera dos v.a normales estándar
def MetodoPolar(mu, sigma):
    Rcuadrado = -2 * log(1 - random())
    Theta = 2 * pi * random()
    x = sqrt(Rcuadrado) * cos(Theta)
    y = sqrt(Rcuadrado) * sin(Theta)
    return (x * sigma + mu, y * sigma + mu)


# genera una v.a normal estándar por el método de razón entre uniformes
NV_MAGICCONST = 4 * exp(-0.50) / sqrt(2.0)


def normalvariate(mu, sigma):
    while 1:
        u1 = random()
        u2 = 1.0 - random()
        z = NV_MAGICCONST * (u1 - 0.5) / u2
        zz = z * z / 4.0
        if zz <= -log(u2):
            break
    return mu + z * sigma


def calcular_estadisticos(funcion_generadora, mu, sigma, n_sim=10000):
    suma = 0
    suma_cuadrados = 0

    # Caso especial: MetodoPolar genera 2 variables por llamada
    es_polar = funcion_generadora.__name__ == "MetodoPolar"
    iteraciones = n_sim // 2 if es_polar else n_sim

    for _ in range(iteraciones):
        resultado = funcion_generadora(mu, sigma)

        if es_polar:
            # Procesamos ambos valores devueltos (X, Y)
            for v in resultado:
                suma += v
                suma_cuadrados += v**2
        else:
            # Procesamos el valor único
            suma += resultado
            suma_cuadrados += resultado**2

    media = suma / n_sim
    # Aplicamos la fórmula de la varianza muestral
    varianza = (suma_cuadrados - n_sim * (media**2)) / (n_sim - 1)

    return media, varianza


# Ejercicio 9
mu, sigma = 0, 1  # Normal estándar
m_rech, v_rech = calcular_estadisticos(Normal_rechazo, mu, sigma)
m_polar, v_polar = calcular_estadisticos(MetodoPolar, mu, sigma)
m_razon, v_razon = calcular_estadisticos(normalvariate, mu, sigma)

print(f"Rechazo: Media={m_rech:.4f}, Var={v_rech:.4f}")
print(f"Polar:   Media={m_polar:.4f}, Var={v_polar:.4f}")
print(f"Razón:   Media={m_razon:.4f}, Var={v_razon:.4f}")
