from scipy.stats import chi2


def estadisticoT(frecuencias, probabilidades):
    t = 0
    K = len(frecuencias)
    n = sum(frecuencias)
    for k in range(K):
        t = t + (frecuencias[k] - n * probabilidades[k]) ** 2 / (n * probabilidades[k])
    return t


if __name__ == "__main__":
    probabilidades = [1 / 6, 1 / 6, 1 / 6, 1 / 6, 1 / 6, 1 / 6]
    frecuencias = [158, 172, 164, 181, 160, 165]

    print("Cantidad de datos: ", sum(frecuencias))

    t0 = estadisticoT(frecuencias, probabilidades)
    print(
        "p-valor: ", 1 - chi2.cdf(t0, df=5)
    )  # df=5 porque tengo k-1 grados de libertad y k=6
