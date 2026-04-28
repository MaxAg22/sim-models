# Ejercicio 1. Se baraja un conjunto de n = 100 cartas (numeradas consecutivamente del 1 al 100) y se extrae
# del mazo una carta por vez. Consideramos que ocurre un “éxito” si la i-ésima carta extraída es aquella cuyo
# número es i (i = 1,...,n).
# a) Calcule la probabilidad de que
# (i) las primeras r cartas sean coincidencias y dé su valor para r = 10.
# (ii) haya exactamente r coincidencias y estén en las primeras r cartas. Dé su valor para r = 10.
# b) Pruebe que E(X) = Var(X) = 1 donde X es el número de coincidencias obtenidas en una baraja de n
# cartas.
# c) Escriba un programa de simulación para estimar la esperanza y la varianza del número total de éxitos,
# y de los eventos del inciso (a) con r = 10, y compare los resultados obtenidos con 100, 1000, 10000
# y 100000 iteraciones.
import random


def expected_value(n_sim):
    count = 0
    count_sq = 0
    for _ in range(n_sim):
        k = 0
        random_list = list(range(1, 101))
        random.shuffle(random_list)
        for index, value in enumerate(random_list):
            k += 1 if index + 1 == value else 0
        count += k
        count_sq += k**2
    E = count/n_sim
    Var = count_sq/n_sim - E**2
    return (E,Var)


def first_r_cards(n_sim):
    count = 0
    for _ in range(n_sim):
        k = 0
        random_list = list(range(1, 101))
        random.shuffle(random_list)
        for index, value in enumerate(random_list[:10]):
            k += 1 if index + 1 == value else 0
        count += 1 if k == 10 else 0
    return count/n_sim


def just_first_r_cards(n_sim):
    count = 0
    for _ in range(n_sim):
        random_list = list(range(1, 101))
        random.shuffle(random_list)
        first_10 = True
        rest_cards = False
        for index, value in enumerate(random_list):
            pos = index + 1
            if pos <= 10:
                if value != pos:
                    first_10 = False
                    break
            else:
                if value == pos:
                    rest_cards  = True
                    break

        if first_10 and not rest_cards:
            count += 1
    return count/n_sim



for n in [100, 1000, 10000]:
    (E, Var) = expected_value(n)
    print(f"N° de sim = {n}, Esperanza ~ {E}, Varianza ~ {Var}")
    
for n in [100, 1000, 10000]:
    a_i = first_r_cards(n)
    a_ii = just_first_r_cards(n)
    print(f"N° de sim = {n}, éxito en primeras 10 ~ {a_i}, éxito solo en primeras 10 ~ {a_ii}")
