from math import log
from random import random, uniform


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


def generar_descanso():
    return uniform(0, 0.3)


def ejercicio_8(tiempo_total):
    t = 0
    n = 0  # En instante t

    # Solicitudes
    Na = 0
    tiempos_Na = []
    Nd = 0
    tiempos_Nd = []

    cola = []
    periodos_descanso = []
    descansando = False

    # Ejercicio 8b) Tiempo de servicio de solicitudes
    tiempos_servicio = []

    # Tiempos
    inf = float("inf")
    Ta = generar_proximo_arribo(t_actual=t, t_max=tiempo_total)
    Td = inf
    Tr = inf

    while Ta < inf or n > 0:
        proximo_evento = min(Ta, Td, Tr)

        # Caso 1: Llego uNa solicitud
        if proximo_evento == Ta:
            t = Ta
            n += 1
            Na += 1
            tiempo_prox_llegada = generar_proximo_arribo(t_actual=t, t_max=tiempo_total)
            Ta = tiempo_prox_llegada

            # Si se pasa
            if Ta > tiempo_total:
                Ta = inf

            # Tenemos que ateNder la primer solicitud
            if n == 1 and not descansando:
                Td = t + generar_atencion()

            # Registrar
            tiempos_Na.append(t)

        # Caso 2: Debemos ateNder uNa solicitud
        elif proximo_evento == Td and not descansando:
            t = Td
            Nd += 1
            n -= 1

            tiempos_servicio.append(t - tiempos_Na[Nd - 1])

            if n == 0:
                Td = inf
                Tr = t + generar_descanso()
                inicio_descanso = t
                descansando = True
            else:
                Td = t + generar_atencion()

            # Registrar
            tiempos_Nd.append(t)

        elif proximo_evento == Tr and descansando:
            t = Tr
            periodos_descanso.append(Tr - inicio_descanso)
            descansando = False
            Tr = inf

            if n > 0:
                Td = t + generar_atencion()
            else:
                inicio_descanso = t
                Tr = t + generar_descanso()
                descansando = True

        cola.append((t, n))

    tiempo_promedio_solicitud = (
        sum(x for x in tiempos_servicio) / len(tiempos_servicio)
        if tiempos_servicio
        else 0
    )

    tiempo_promedio_descanso = (
        sum(x for x in periodos_descanso) / len(periodos_descanso)
        if periodos_descanso
        else 0
    )

    return (
        tiempos_Na,
        tiempos_Nd,
        periodos_descanso,
        tiempo_promedio_descanso,
        cola,
        tiempo_promedio_solicitud,
    )


if __name__ == "__main__":
    res = ejercicio_8(100)
    print("\n*** Ejercicio 8 ***")
    # print(f"Tiempos de llegada (Na): {res[0][:10]} ...")
    # print(f"Tiempos de atención (Nd): {res[1][:10]} ...")
    print(f"Periodos de descanso: {[float(f'{d:.2f}') for d in res[2][:10]]} ...")
    print(
        f"Evolución de la cola (t, n): {[(float(f'{d:.4f}'), n) for (d, n) in res[4][:10]]} ..."
    )
    print(f"Tiempo promedio de servicio: {res[5]:.4f}")
