from random import random
from math import exp


def exponencial(y, media=50):
    lamda = 1 / media
    return 1 - exp(-y * lamda)


def generar_uniformes(n):
    uniformes = []
    for _ in range(n):
        uniformes.append(random())
    return uniformes


def estadisticoD(muestra, fun):
    muestra.sort()
    d = float("-inf")
    n = len(muestra)
    for j, y_j in enumerate(muestra):
        d1 = ((j + 1) / n) - fun(y_j)
        d2 = fun(y_j) - (j / n)
        d = max(d1, d2, d)
    return d


def simular_p_valor(n_sim, muestra, fun):
    d = estadisticoD(muestra, fun)
    pvalor = 0
    n = len(muestra)
    for _ in range(n_sim):
        uniformes = generar_uniformes(n)
        uniformes.sort()
        d_j = 0
        for j in range(n):
            u_j = uniformes[j]
            d1 = ((j + 1) / n) - u_j
            d2 = u_j - (j / n)
            d_j = max(d_j, d1, d2)
        if d_j >= d:
            pvalor += 1
    return d, pvalor / n_sim


muestra = [
    86.0,
    133.0,
    75.0,
    22.0,
    11.0,
    144.0,
    78.0,
    122.0,
    8.0,
    146.0,
    33.0,
    41.0,
    99.0,
]
d, pvalor = simular_p_valor(10000, muestra, exponencial)
print("=== Ejercicio 4 ===")
print(f"d_obs = {d}")
print(f"p-valor estimado ~ {pvalor}")
