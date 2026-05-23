from random import random
import tp5_12


def simular_aficionados(lamda, T):
    cantidad_eventos, _ = tp5_12.calcular_eventos_y_tiempo(lamda, T)
    aficionados = 0
    for _ in range(cantidad_eventos):
        u = int(random() * 21) + 20
        aficionados += u
    return aficionados


# Para el ejercicio 13: lamda = 5, T = 1
total_arribados = simular_aficionados(5, 1)
print(f"Total de aficionados tras 1 hora: {total_arribados}")
