import math
import random
import numpy as np
from scipy.stats import chi2, binom

# EJERCICIO 3


def cdf_normal_estandar(x):
    return math.erf(x / math.sqrt(2.0)) / 2.0 + 0.5


def calcular_estadistido_D_normal(muestra, mu, sigma):
    muestra.sort()
    n = len(muestra)
    d = 0
    for j, y_j in enumerate(muestra):
        z_j = (y_j - mu) / sigma
        f_y = cdf_normal_estandar(z_j)

        d1 = ((j + 1) / n) - f_y
        d2 = f_y - (j / n)
        d = max(d, d1, d2)
    return d


def calcular_estadistico_D_unif(muestra):
    muestra.sort()
    d = 0
    n = len(muestra)
    for j, y_j in enumerate(muestra):
        # Usamos la media de referencia para la CDF
        f_y = y_j
        d1 = ((j + 1) / n) - f_y
        d2 = f_y - (j / n)
        d = max(d, d1, d2)
    return d


def simular_con_uniformes(muestra, mu, sigma, n_sim):
    d_obs = calcular_estadistido_D_normal(muestra, mu, sigma)
    hits = 0
    n = len(muestra)
    for _ in range(n_sim):
        # Generar muestra exponencial con la media estimada original
        muestra_sim = [random.random() for _ in range(n)]
        d_sim = calcular_estadistico_D_unif(muestra_sim)

        if d_sim >= d_obs:
            hits += 1

    return hits / n_sim


muestra_ej3 = [
    491.455,
    496.387,
    491.175,
    502.551,
    509.838,
    491.708,
    501.39,
    496.717,
    494.769,
    503.901,
    502.351,
    503.617,
    501.754,
    497.783,
    501.019,
    501.494,
    502.689,
    501.762,
    509.541,
    504.808,
    507.551,
    498.701,
    501.114,
    504.87,
    506.344,
    511.543,
    496.488,
    498.155,
    501.201,
    507.446,
]


d = calcular_estadistido_D_normal(muestra_ej3, 500, 5)
p_valor = simular_con_uniformes(muestra_ej3, 500, 5, 10000)
print("Ejercicio 3b)")
print(f"El valor del estadistico D de la muestra es {d}")
print("Ejercicio 3c)")
print(f"p-valor simulado ~ {p_valor}")

# FIN EJERCICIO 3


# EJERCICIO 4


def ejercicio_4a():
    frecuencias = np.array([25, 68, 70, 37])
    n_binomial = 3
    N_total = sum(frecuencias)
    p = 0.5
    # Valores posibles de la variable
    k = 4

    datos = []
    for respuestas_correctas, freq in enumerate(frecuencias):
        datos.extend([respuestas_correctas] * freq)

    prob_teoricas = np.array([binom.pmf(i, n_binomial, p) for i in range(k)])

    frec_esperadas = N_total * prob_teoricas

    T = np.sum((frecuencias - frec_esperadas) ** 2 / frec_esperadas)

    p_valorr = chi2.sf(T, df=3)

    return T, p_valorr


def ejercicio_4b():
    frecuencias = np.array([25, 68, 70, 37])
    n_binomial = 3
    N_total = sum(frecuencias)
    # Valores posibles de la variable
    k = 4

    datos = []
    for respuestas_correctas, freq in enumerate(frecuencias):
        datos.extend([respuestas_correctas] * freq)

    p_est = np.mean(datos) / n_binomial

    prob_teoricas = np.array([binom.pmf(i, n_binomial, p_est) for i in range(k)])

    frec_esperadas = N_total * prob_teoricas

    T = np.sum((frecuencias - frec_esperadas) ** 2 / frec_esperadas)

    p_valor = chi2.sf(T, df=2)

    return p_est, T, p_valor


def ejercicio_4c():
    frecuencias = np.array([25, 68, 70, 37])
    n_binomial = 3
    N_total = sum(frecuencias)
    # Valores posibles de la variable
    k = 4

    datos = []
    for respuestas_correctas, freq in enumerate(frecuencias):
        datos.extend([respuestas_correctas] * freq)

    p_est = np.mean(datos) / n_binomial

    prob_teoricas = np.array([binom.pmf(k, n_binomial, p_est) for k in range(k)])

    frec_esperadas = N_total * prob_teoricas

    t_obs = np.sum((frecuencias - frec_esperadas) ** 2 / frec_esperadas)

    n_sim = 100000
    hits = 0
    for _ in range(n_sim):

        # Genero una muestra binomial con el p estimado
        muestra = np.random.binomial(n=n_binomial, p=p_est, size=N_total)

        # Reestimar p^
        p_sim = np.mean(muestra) / n_binomial
        N_sim = np.array([np.sum(muestra == i) for i in range(k)])

        # Calculamos las probabilidades teoricas con p_sim
        prob_sim = np.array([binom.pmf(i, n_binomial, p_sim) for i in range(k)])

        # Calculamos T_sim
        E_sim = N_total * prob_sim
        T_sim = np.sum((N_sim - E_sim) ** 2 / E_sim)  # estadìstico

        if T_sim >= t_obs:
            hits += 1

    return hits / n_sim


print("Ejercicio 4a)")
T, p_v = ejercicio_4a()
print(f"T observado = {T:.4f}")
print(f"p-valor (Chi-cuadrado) = {p_v:.4f}")
print("Ejercicio 4b")
p_est, T1, p_v1 = ejercicio_4b()
print(f"p estimado = {p_est:.4f}")
print(f"T observado = {T1:.4f}")
print(f"p-valor (Chi-cuadrado) = {p_v1:.4f}")
p_v_simulado = ejercicio_4c()
print("Ejercicio 4c")
print(f"p-valor (Simulado) = {p_v_simulado:.4f}")

# FIN EJERCICIO 4


# EJERCICIO 2


def obtener_mtra_bootstrap(datos):
    n = len(datos)
    muestra = np.random.choice(datos, size=n, replace=True)
    return muestra


def obtener_mediana_bootstrap(datos):
    datos.sort()
    return (datos[7] + datos[8]) / 2


def ejercicio2a():
    muestra = [27, 25, 80, 79, 61, 55, 31, 35, 60, 8, 87, 89, 41, 90, 96, 63]
    muestra.sort()
    mediana_fe = (muestra[7] + muestra[8]) / 2
    N = 5000
    # obtenemos las muestras bootstrap
    muestras_bt = []
    for i in range(N):
        muestras_bt.append(obtener_mtra_bootstrap(muestra))

    # obtener mediana de cada mustra bootstrap
    medianas_bt = []
    for i in range(N):
        medianas_bt.append(obtener_mediana_bootstrap(muestras_bt[i]))

    medianas_bt = np.array(medianas_bt)
    return sum((medianas_bt - mediana_fe) ** 2) / N


def ejercicio2b():
    muestra = np.array([27, 25, 80, 79, 61, 55, 31, 35, 60, 8, 87, 89, 41, 90, 96, 63])
    muestra.sort()
    media_muestral = np.mean(muestra)
    varianza_fe = sum((muestra - media_muestral) ** 2) / 16
    N = 5000
    # obtenemos las muestras bootstrap
    muestras_bt = []
    for i in range(N):
        muestras_bt.append(obtener_mtra_bootstrap(muestra))

    # obtener mediana de cada mustra bootstrap
    medianas_bt = []
    for i in range(N):
        medianas_bt.append(obtener_mediana_bootstrap(muestras_bt[i]))

    medianas_bt = np.array(medianas_bt)
    return sum((medianas_bt - varianza_fe) ** 2) / N


print("Ejercicio 2a")
print("ECM(mediana) =", ejercicio2a())
print("Ejercicio 2b")
print("ECM(varianza) =", ejercicio2b())

# FIN EJERCICIO 2
