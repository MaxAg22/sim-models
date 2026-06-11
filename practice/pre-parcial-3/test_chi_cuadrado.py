import numpy as np
from scipy.stats import chi2, binom


def ejercicio_3b():
    frecuencias = np.array([38, 144, 342, 287, 164, 25])
    # Monedas lanzadas en cada experimento
    n_binomial = 5
    # Total de repeticiones
    N_total = sum(frecuencias)
    # Valores posibles de la variable
    k = 6

    datos = []
    for caras, freq in enumerate(frecuencias):
        datos.extend([caras] * freq)

    p_est = np.mean(datos) / n_binomial

    prob_teoricas = np.array(
        [binom.pmf(k, n_binomial, p_est) for k in range(k)])

    frec_esperadas = N_total * prob_teoricas

    T = np.sum((frecuencias - frec_esperadas)**2 / frec_esperadas)

    p_valor = chi2.sf(T, df=4)

    print(f"p estimado = {p_est:.4f}")
    print(f"T observado = {T:.4f}")
    print(f"p-valor (Chi-cuadrado) = {p_valor:.4f}")


def ejercicio_3c():
    frecuencias = np.array([38, 144, 342, 287, 164, 25])
    # Monedas lanzadas en cada experimento
    n_binomial = 5
    # Total de repeticiones
    N_total = sum(frecuencias)
    # Valores posibles de la variable
    k = 6

    datos = []
    for caras, freq in enumerate(frecuencias):
        datos.extend([caras] * freq)

    p_est = np.mean(datos) / n_binomial

    prob_teoricas = np.array(
        [binom.pmf(k, n_binomial, p_est) for k in range(k)])

    frec_esperadas = N_total * prob_teoricas

    t_obs = np.sum((frecuencias - frec_esperadas)**2 / frec_esperadas)

    n_sim = 10000
    hits = 0
    for _ in range(n_sim):
        muestra = np.random.binomial(n=n_binomial, p=p_est, size=N_total)
        # Reestimar p^
        p_sim = np.mean(muestra) / n_binomial
        N_sim = np.array([np.sum(muestra == k) for k in range(k)])
        prob_sim = np.array([binom.pmf(i, n_binomial, p_sim)
                            for i in range(k)])
        E_sim = N_total * prob_sim
        T_sim = np.sum((N_sim - E_sim) ** 2 / E_sim)  # estadìstico

        if T_sim >= t_obs:
            hits += 1

    print("p-valor (simulado) ~", hits/n_sim)


ejercicio_3b()
ejercicio_3c()
