import math
import random


def cdf_normal_estandar(x):
    return math.erf(x / math.sqrt(2.0)) / 2.0 + 0.5


def Normal_rechazo(mu, sigma):
    while True:
        y1 = -math.log(1 - random.random())
        y2 = -math.log(1 - random.random())
        if y2 >= (y1 - 1) ** 2 / 2:
            z = y1 if random.random() < 0.5 else -y1
            return z * sigma + mu


def estadistico_KS_normal(muestra, mu, sigma):
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


if __name__ == "__main__":
    datos = [
        91.9,
        97.8,
        111.4,
        122.3,
        105.4,
        95.0,
        103.8,
        99.6,
        96.6,
        119.3,
        104.8,
        101.7,
    ]

    n = len(datos)

    # 1. Estimación de parámetros originales
    mu_est = sum(datos) / n
    # S^2 = 1/(n-1) * sum((xi - media)^2)
    var_est = sum((x - mu_est) ** 2 for x in datos) / (n - 1)
    desv_est = math.sqrt(var_est)

    # 2. Estadístico observado
    d_obs = estadistico_KS_normal(datos, mu_est, desv_est)

    # 3. Simulación de Monte Carlo
    Nsim = 10000
    hits = 0
    for _ in range(Nsim):
        # Generamos muestra normal bajo H0
        muestra_sim = [Normal_rechazo(mu_est, desv_est) for _ in range(n)]

        # RE-ESTIMAMOS para la muestra simulada
        mu_sim = sum(muestra_sim) / n
        var_sim = sum((x - mu_sim) ** 2 for x in muestra_sim) / (n - 1)
        desv_sim = math.sqrt(var_sim)

        # Calculamos D_sim
        d_sim = estadistico_KS_normal(muestra_sim, mu_sim, desv_sim)

        if d_sim >= d_obs:
            hits += 1

    print(f"Estadístico D observado: {d_obs:.4f}")
    print(f"p-valor ~ {hits / Nsim:.4f}")
