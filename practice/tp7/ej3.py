from scipy.stats import chi2
from random import random, uniform


def unif(y):
    return y


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
    return pvalor / n_sim


muestra = [0.12, 0.18, 0.06, 0.33, 0.72, 0.83, 0.36, 0.27, 0.77, 0.74]
pvalor = simular_p_valor(10000, muestra, unif)
print("=== Ejercicio 3 ===")
print(f"p-valor estimado ~ {pvalor}")
