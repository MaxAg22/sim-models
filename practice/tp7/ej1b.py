import numpy as np
from ej1a import estadisticoT


def generar_numero_discreto(p, x):
    """
    Generando número discreto con método de transformada inversa.

    x: lista de valores posibles de la variable aleatoria
    p: lista de probabilidades asociadas a cada valor de x
    """
    u = np.random.random()
    i = 0
    F = 0.0
    while i < len(p) and u >= F + p[i]:
        F += p[i]
        i += 1
    return x[i]


# X_1: Flor blanca
# X_2: Flor rosa
# X_3: Flor roja
def frecuencias_generadas(n):
    freq = [0, 0, 0]
    for k in range(n):
        x = generar_numero_discreto([1 / 4, 1 / 2, 1 / 4], [1, 2, 3])
        freq[x - 1] = freq[x - 1] + 1
    return freq


def ejercicio_2b(frecuencias, probabilidades, NSim):
    pvalor = 0
    n = sum(frecuencias)  # cantidad de datos de mi muestra
    t_obs = estadisticoT(frecuencias, probabilidades)
    for k in range(NSim):
        freq = frecuencias_generadas(n)
        t = estadisticoT(freq, probabilidades)
        if t_obs <= t:
            pvalor = pvalor + 1
    return pvalor / NSim


if __name__ == "__main__":
    probabilidades = [1 / 4, 1 / 2, 1 / 4]
    frecuencias = [141, 291, 132]
    Nsim = 10000
    t = ejercicio_2b(frecuencias, probabilidades, Nsim)

    print("Ejercicio b:")
    print("p-valor estimado: ", t)
