import math
import random


def rt(df):  # df grados de libertad
    """Genera un número aleatorio que sigue la distribución T-student"""
    x = random.gauss(0.0, 1.0)
    y = 2.0 * random.gammavariate(0.5 * df, 2.0)

    return x / (math.sqrt(y / df))


def cdf_normal_estandar(x):
    return math.erf(x / math.sqrt(2.0)) / 2.0 + 0.5


def estadisticoD(muestra, fun):
    muestra.sort()
    d = float("-inf")
    n = len(muestra)
    for j, y_j in enumerate(muestra):
        d1 = ((j + 1) / n) - fun(y_j)
        d2 = fun(y_j) - (j / n)
        d = max(d1, d2, d)
    return d


def generar_uniformes(n):
    uniformes = []
    for _ in range(n):
        uniformes.append(random.random())
    return uniformes


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


if __name__ == "__main__":
    tamanos = [10, 20, 100, 1000]
    print("N | Estadístico D | p-valor")
    for n in tamanos:
        muestra = [rt(11) for _ in range(n)]
        d_obs = estadisticoD(muestra, cdf_normal_estandar)
        p_val = simular_p_valor(10000, muestra, cdf_normal_estandar)
        print(f"{n} | {d_obs:.4f} | {p_val:.4f}")
