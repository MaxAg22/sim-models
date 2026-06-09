"""Estima una probabilidad utilizando Bootstrap y MonteCarlo"""

import numpy as np


def obtener_mtra_bootstrap(datos):
    n = len(datos)
    muestra = np.random.choice(datos, size=n, replace=True)
    return muestra


def sim_bootstrap(n_sim, datos):
    acum = 0
    for _ in range(n_sim):
        mstra = obtener_mtra_bootstrap(datos)
        prom = np.mean(mstra)
        if 71.7 < prom < 81.7:
            acum += 1
    return acum / n_sim


datos = np.array([56, 101, 78, 67, 93, 87, 64, 72, 80, 69])
res = sim_bootstrap(10000, datos)
print(res)
