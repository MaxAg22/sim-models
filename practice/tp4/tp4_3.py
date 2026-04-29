# Ejercicio 3. Se lanzan simultáneamente un par de dados legales y se anota el resultado de la suma de ambos.
# El proceso se repite hasta que todos los resultados posibles: 2,3,...,12 hayan aparecido al menos una vez.
# Estudiar mediante una simulación la variable N, el número de lanzamientos necesarios para cumplir el
# proceso. Cada lanzamiento implica arrojar el par de dados.
# a) Describa la estructura lógica del algoritmo que permite simular en computadora el número de lanzamientos necesarios para cumplir el proceso.
# b) Mediante una implementación en computadora,
# (i) estime el valor medio y la desviación estándar del número de lanzamientos, repitiendo el algoritmo: 100, 1000, 10000 y 100000 veces.
# (ii) estime la probabilidad de que N sea por lo menos 15 y la probabilidad de que N sea a lo sumo
# 9, repitiendo el algoritmo: 100, 1000, 10000 y 100000.
from random import randint

def lanzamiento():
    """simula un lanzamiento de dos dados"""
    U1 = randint(1,6)
    U2 = randint(1,6)
    return U1 + U2

def jugar():
    """juego de lanzar dados, devuelve la cantidad de lanzaimentos"""
    a = [False] * 11
    N = 0
    while False in a:
        S = lanzamiento()
        a[S-2] = True
        N += 1
    return N

def sim_valor_medio(n_sim):
    """estima E[N] y E[N^2]"""
    count = 0
    count_sq = 0
    for _ in range(n_sim):
        N = jugar()
        count += N
        count_sq += N ** 2
    return (count/n_sim, count_sq/n_sim)

def obtener_media_y_desviacion(n_sim):
    """obtiene la media y la desviacion del juego"""
    (E, E2) = sim_valor_medio(n_sim)
    Desv = (E2 - E**2) ** 0.5
    return (E, Desv)

def almenos_15(n_sim):
    """estima la probabilidad de que N sea por lo menos 15"""
    count = 0
    for _ in range(n_sim):
        N = jugar()
        count += 1 if N >= 15 else 0
    return count/n_sim


print("\n*** Ejercicio 3 ***")
for n in [100, 1000, 10000, 100000]:
    (E, Desv) = obtener_media_y_desviacion(n)
    print(f"N° de sim = {n}, Valor medio ~ {E}, Desviación ~ {Desv}")

for n in [100, 1000, 10000, 100000]:
    p1 = almenos_15(n)
    print(f"N° de sim = {n}, al menos 15 ~ {p1}, a lo sumo 9 ~ 0.00")