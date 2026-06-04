from math import log
from random import random


def lambda_t(t):
    """Función de intensidad lambda(t)"""
    t_aux = t % 10
    if 0 <= t_aux <= 5:
        return 3 * t_aux + 4
    elif 5 < t_aux <= 10:
        return 34 - 3 * t_aux


def generar_proximo_arribo(t_actual, lamda_max=19, t_max=100):
    """
    RetorNa el tiempo (t) del PRÓXIMO arribo
    basado en el tiempo actual de la simulación.
    """
    t = t_actual
    while True:
        u = 1 - random()
        t += -log(u) / lamda_max  # Avanzamos el reloj tentativo
        if t > t_max:  # Límite de la simulación (T)
            return float("inf")

        v = random()
        if v < lambda_t(t) / lamda_max:  # Criterio de adelgazamiento [2]
            return t  # Aceptamos este tiempo como el próximo arribo


def generar_atencion(lamda=13):
    """Generamos uNa exponencial con tasa lamda"""
    u = 1 - random()
    return -log(u) / lamda


def ejercicio_7(tiempo_total):
    t = 0
    n = 0  # En instante t

    # Solicitudes
    Na = 0
    tiempos_Na = []
    Nd = 0
    tiempos_Nd = []

    # quiero devolver el tiempo de servicio de cada solicitud
    tiempos_servicio = []

    # Tiempos
    T0 = generar_proximo_arribo(t_actual=t, t_max=tiempo_total)
    Ta = T0
    Td = float("inf")

    while t < tiempo_total:
        proximo_evento = min(Ta, Td)

        # Caso 1: Llego uNa solicitud
        if proximo_evento == Ta:
            t = Ta
            n += 1
            Na += 1
            tiempo_prox_llegada = generar_proximo_arribo(t_actual=t, t_max=tiempo_total)
            Ta = tiempo_prox_llegada

            # Si se pasa
            if Ta > tiempo_total:
                Ta = float("inf")

            # Tenemos que ateNder la primer solicitud
            if n == 1:
                tiempo_atencion = generar_atencion()
                Td = t + tiempo_atencion

            # Registrar
            tiempos_Na.append(t)

        # Caso 2: Debemos ateNder uNa solicitud
        elif proximo_evento == Td:
            t = Td
            Nd += 1
            n -= 1

            tiempos_servicio.append(t - tiempos_Na[Nd - 1])

            if n == 0:
                Td = float("inf")
            else:
                tiempo_atencion = generar_atencion()
                Td = t + tiempo_atencion

            # Registrar
            tiempos_Nd.append(t)

    tiempo_promedio_solicitud = (
        sum(x for x in tiempos_servicio) / len(tiempos_servicio)
        if tiempos_servicio
        else 0
    )
    return (
        Na,
        tiempos_Na,
        Nd,
        tiempos_Nd,
        tiempo_promedio_solicitud,
    )


if __name__ == "__main__":
    res = ejercicio_7(100)
    print("\n*** Ejercicio 7 ***")
    print(f"Cantidad de solicitudes: {res[0]}")
    print(f"Tiempo de llegada de solicitudes: {res[1]}")
    print(f"Cantidad de solicitudes ateNdidas: {res[2]}")
    print(f"Tiempo de atención de solicitudes: {res[3]}")
    print(f"Tiempo de servicio de solicitudes: {res[4]}")
