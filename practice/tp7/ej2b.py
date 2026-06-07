import numpy as np
from ej2a import estadisticoT


def generar_numero_discreto(p, x):
    """
    x: lista de valores posibles de la variable aleatoria
    p: lista de probabilidades asociadas a cada valor de x
    """
    u = np.random.random()
    i = 0
    F = p
    while u >= F:
        i = i + 1
        F = F + 1 / 6
    return x[i]


def frecuencias_generadas(n):
    freq = [0, 0, 0, 0, 0, 0]
    for k in range(n):
        x = generar_numero_discreto(1 / 6, [1, 2, 3, 4, 5, 6])
        freq[x - 1] = freq[x - 1] + 1
    return freq


def ejercicio_2b(frecuencias, probabilidades, NSim):
    pvalor = 0
    n = sum(frecuencias)  # cantidad de datos de mi muestra
    t_obs = estadisticoT(frecuencias, probabilidades)
    for k in range(NSim):
        freq = frecuencias_generadas(
            n
        )  # frecuencias de las clases en mi muestra generada con distribución U{1,6}
        t = estadisticoT(
            freq, probabilidades
        )  # calculo el estadístico para la muestra generada
        if t_obs <= t:
            pvalor = pvalor + 1
    return pvalor / NSim


probabilidades = [1 / 6, 1 / 6, 1 / 6, 1 / 6, 1 / 6, 1 / 6]
frecuencias = [158, 172, 164, 181, 160, 165]
Nsim = 10000
t = ejercicio_2b(frecuencias, probabilidades, Nsim)

print("Ejercicio b:")
print("p-valor estimado: ", t)
