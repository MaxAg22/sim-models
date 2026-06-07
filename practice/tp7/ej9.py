import math
import random


# CDF de la exponencial usando la media estimada
def exponencial_cdf(x, media):
    return 1 - math.exp(-x / media)


def estadisticoD(muestra, media_ref):
    muestra.sort()
    d = 0
    n = len(muestra)
    for j, y_j in enumerate(muestra):
        # Usamos la media de referencia para la CDF
        f_y = exponencial_cdf(y_j, media_ref)
        d1 = ((j + 1) / n) - f_y
        d2 = f_y - (j / n)
        d = max(d, d1, d2)
    return d


if __name__ == "__main__":
    muestra = [
        1.6,
        10.3,
        3.5,
        13.5,
        18.4,
        7.7,
        24.3,
        10.7,
        8.4,
        4.9,
        7.9,
        12,
        16.2,
        6.8,
        14.7,
    ]
    n = len(muestra)

    # 1. Estimar media original
    media_est = sum(muestra) / n

    # 2. Estadístico observado
    d_obs = estadisticoD(muestra, media_est)

    # 3. Simulación para parámetros NO especificados (Ejemplo 8.4)
    Nsim = 10000
    hits = 0
    for _ in range(Nsim):
        # Generar muestra exponencial con la media estimada original
        muestra_sim = [-media_est * math.log(random.random()) for _ in range(n)]

        # RE-ESTIMAR la media para la muestra simulada
        media_sim = sum(muestra_sim) / n

        # Calcular D_sim comparando contra su propia media estimada
        d_sim = estadisticoD(muestra_sim, media_sim)

        if d_sim >= d_obs:
            hits += 1

    print(f"p-valor ~ {hits / Nsim}")
