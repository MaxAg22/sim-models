import math
import random


def generar_exponencial(_lambda):
    u = 1 - random.random()
    return -math.log(u) / _lambda


def exponencial_cdf(x, media):
    return 1 - math.exp(-x / media)


def unif(y, media):
    return y


def calcular_estadistido_D(muestra, media_ref, fun):
    muestra.sort()
    d = 0
    n = len(muestra)
    for j, y_j in enumerate(muestra):
        # Usamos la media de referencia para la CDF
        f_y = fun(y_j, media_ref)
        d1 = ((j + 1) / n) - f_y
        d2 = f_y - (j / n)
        d = max(d, d1, d2)
    return d


def simular_con_uniformes(muestra, media_ref, n_sim):
    d_obs = calcular_estadistido_D(muestra, media_ref, exponencial_cdf)
    hits = 0
    n = len(muestra)
    for _ in range(n_sim):
        # Generar muestra exponencial con la media estimada original
        muestra_sim = [random.random() for _ in range(n)]
        d_sim = calcular_estadistido_D(muestra_sim, media_ref, unif)

        if d_sim >= d_obs:
            hits += 1

    return hits / n_sim


def simular_con_variables_que_verifiquen(muestra, media_ref, n_sim):
    d_obs = calcular_estadistido_D(muestra, media_ref, exponencial_cdf)
    hits = 0
    n = len(muestra)
    for _ in range(n_sim):
        # Generar muestra exponencial con la media estimada original
        muestra_sim = [generar_exponencial(0.05) for _ in range(n)]
        d_sim = calcular_estadistido_D(muestra_sim, media_ref, exponencial_cdf)

        if d_sim >= d_obs:
            hits += 1

    return hits / n_sim


print("Ejercicio 2b: ")

muestra = [15.22860536, 40.60145536, 33.67482894, 44.03841737, 15.69560109,
           16.2321714, 25.02174735, 30.34655637, 3.3181228, 5.69447539,
           10.1119561, 49.10266584, 3.6536329, 35.82047148, 3.37816632,
           36.72299321, 50.67085322, 3.25476304, 20.12426236, 20.2668814,
           17.49593589, 2.70768636, 14.77332745, 1.72267967, 23.34685662,
           8.46376635, 9.18330789, 9.97428217, 2.33951729, 137.51657441,
           9.79485269, 10.40308179, 1.57849658, 6.26959703, 4.74251574,
           1.53479053, 34.74136011, 27.47600572, 9.1075566, 1.88056595,
           27.59551348, 6.82283137, 12.45162807, 28.01983651, 0.36890593,
           7.82520791, 3.17626161, 46.91791271, 38.08371186, 41.10961135]
print(
    f"Valor del estadistico de la muestra = {calcular_estadistido_D(muestra, 1/0.05, exponencial_cdf)}")

print("Ejercicio 2c: ")
p_valor = simular_con_uniformes(muestra, 1/0.05, 10000)
print(f"p-valor ~ {p_valor}")

print("Ejercicio 2d: ")
p_valor = simular_con_variables_que_verifiquen(muestra, 1/0.05, 10000)
print(f"p-valor ~ {p_valor}")
