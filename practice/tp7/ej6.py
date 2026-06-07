import numpy as np
from scipy.stats import chi2


def calcular_estadistico_pearson(N_i, E_i):
    """
    Calcula el estadístico T siguiendo la fórmula de Pearson [1].
    T = sum((frec_obs - frec_esp)^2 / frec_esp)
    """
    return np.sum((N_i - E_i) ** 2 / E_i)


def frecuencias_generadas(n, p):
    """
    Genera frecuencias simuladas bajo H0 usando binomiales condicionadas [3].
    Esta lógica es eficiente para muestras grandes como n=637.
    """
    freq = []
    sum_freq = 0
    l = len(p)
    for k in range(l - 1):
        # Probabilidad condicionada lambda_j = p_j / (1 - P(X < j)) [3]
        denominador = 1 - sum(p[:k])
        prob_cond = p[k] / denominador

        # Generación binomial para la categoría actual
        x = np.random.binomial(n=n - sum_freq, p=prob_cond)
        freq.append(x)
        sum_freq += x

    # La última categoría recibe el resto de la muestra [3]
    freq.append(n - sum_freq)
    return np.array(freq)


def resolver_ejercicio_6():
    # 1. Preparación de datos del enunciado [4, 5]
    prob = np.array([0.31, 0.22, 0.12, 0.10, 0.08, 0.06, 0.04, 0.04, 0.02, 0.01])
    frec_obs = np.array([188, 138, 87, 65, 48, 32, 30, 34, 13, 2])
    n_total = np.sum(frec_obs)
    frec_esp = n_total * prob

    # --- Parte 6d) Aproximación Chi-cuadrado ---
    t_obs = calcular_estadistico_pearson(frec_obs, frec_esp)
    # Grados de libertad k-1 (10 categorías - 1) [1]
    p_chi2 = chi2.sf(t_obs, df=len(prob) - 1)

    print("=== Ejercicio 6d) Pearson ===")
    print(f"T observado: {t_obs:.4f}")
    print(f"p-valor (Chi-cuadrado): {p_chi2:.4f}")

    # --- Parte 6e) Simulación de Monte Carlo ---
    Nsim = 10000
    hits = 0

    for _ in range(Nsim):
        # Generar nueva muestra bajo H0
        frec_sim = frecuencias_generadas(n_total, prob)
        # Calcular T para la muestra simulada
        t_sim = calcular_estadistico_pearson(frec_sim, frec_esp)

        if t_sim >= t_obs:
            hits += 1

    p_montecarlo = hits / Nsim

    print("\n=== Ejercicio 6e) Simulación ===")
    print(f"p-valor estimado ({Nsim} sims): {p_montecarlo:.4f}")


if __name__ == "__main__":
    resolver_ejercicio_6()
