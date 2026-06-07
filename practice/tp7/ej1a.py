"""Aproximando p-valor por prueba Pearson con chi-cuadrado"""

from scipy.stats import chi2
import numpy as np


def estadisticoT(frecuencias, probabilidades):
    t = 0
    K = len(frecuencias)
    n = sum(frecuencias)
    for k in range(K):
        t = t + (frecuencias[k] - n * probabilidades[k]) ** 2 / (n * probabilidades[k])
    return t


if __name__ == "__main__":
    probabilidades = [1 / 4, 1 / 2, 1 / 4]
    frecuencias = [141, 291, 132]
    print("Cantidad de datos: ", sum(frecuencias))

    t0 = estadisticoT(frecuencias, probabilidades)
    print(
        "p-valor: ", 1 - chi2.cdf(t0, df=2)
    )  # df=2 porque tengo k-1 grados de libertad y k=3
