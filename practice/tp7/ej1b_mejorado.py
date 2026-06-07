import numpy as np
from ej1a import estadisticoT


def generar_binomial(n, p):
    c = p / (1 - p)
    prob = (1 - p) ** n
    F = prob
    i = 0
    u = np.random.random()
    while u >= F:
        prob *= c * (n - i) / (i + 1)
        F += prob
        i += 1
    return i


# X_1: Flor blanca
# X_2: Flor rosa
# X_3: Flor roja
def frecuencias_generadas(n, p):
    freq = []
    sum_freq = 0
    l = len(p)
    for k in range(l - 1):
        # Probabilidad de la categoría k dado que no cayó en las anteriores
        # P(X=k | X no es de 0..k-1) = p_k / (1 - suma de probabilidades anteriores)
        denominador = 1 - sum(p[:k])
        prob_cond = p[k] / denominador
        x = generar_binomial(n - sum_freq, prob_cond)
        freq.append(x)
        sum_freq += x
    freq.append(n - sum_freq)
    return freq


def ejercicio_2b(frecuencias, probabilidades, NSim):
    pvalor = 0
    n = sum(frecuencias)  # cantidad de datos de mi muestra
    t_obs = estadisticoT(frecuencias, probabilidades)
    for k in range(NSim):
        freq = frecuencias_generadas(n, probabilidades)
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
