from collections import deque


# t tiempo simulado transcurrido
# n_solicitudes número de solicitudes en el instante t
# solicitudes: número de solicitudes hasta el tiempo t
# servicios_atendidos: número de servicios atendidos hasta el tiempo t
# descansos[]: lista de descansos, en donde un descanso es de la forma (t_inicio, t_final)
# servicios_pendientes[]: cola de servicios por atender

def generar_llegada():
    return 10


def generar_atencion():
    return 10


def generar_descanso():
    return 10


def ejercicio_7a(tiempo_total):
    t = 0
    n_solicitudes_actuales = 0  # en instante t

    # Solicitudes
    cantidad_solicitudes = 0
    llegada_de_solicitudes = []
    cantidad_solicitudes_atendidas = 0
    tiempo_atencion_de_solicitudes = []

    # Descansos
    fin_descanso = tiempo_total
    descansando = False
    descansos = []
    servicios_pendientes = deque()

    # Tiempos
    tiempo_llegada = generar_llegada()
    tiempo_proxima_llegada = tiempo_llegada
    tiempo_fin_servicio = tiempo_total  # "infinito"

    while t < tiempo_total:
        proximo_evento = min(tiempo_proxima_llegada,
                             tiempo_fin_servicio, fin_descanso)

        # caso 1: Llego una solicitud
        if proximo_evento == tiempo_proxima_llegada:
            t = tiempo_proxima_llegada
            n_solicitudes_actuales += 1
            servicios_pendientes.append((t, n_solicitudes_actuales))
            cantidad_solicitudes += 1
            tiempo_prox_llegada = generar_llegada()
            tiempo_proxima_llegada = t + tiempo_prox_llegada

            # si se pasa
            if tiempo_proxima_llegada > tiempo_total:
                tiempo_proxima_llegada = tiempo_total

            # tenemos que atender la primer solicitud
            if n_solicitudes_actuales == 1 and not descansando:
                tiempo_atencion = generar_atencion()
                tiempo_fin_servicio = t + tiempo_atencion

            # registrar
            llegada_de_solicitudes.append(t)

        # caso 2: Debemos atender una solicitud
        elif proximo_evento == tiempo_fin_servicio:
            t = tiempo_fin_servicio
            cantidad_solicitudes_atendidas += 1
            n_solicitudes_actuales -= 1
            servicios_pendientes.append((t, n_solicitudes_actuales))

            # registrar
            tiempo_atencion_de_solicitudes.append(t)

            if n_solicitudes_actuales == 0:
                tiempo_fin_servicio = tiempo_total
                fin_descanso = t + generar_descanso()
                descansando = True
                descansos.append((t, fin_descanso - t))

                # El descanso supera el tiempo que el servidor atiende
                if fin_descanso > tiempo_total:
                    fin_descanso = tiempo_total

            else:
                tiempo_atencion = generar_atencion()
                tiempo_fin_servicio = t + tiempo_atencion

        # gestionar el descanso, re-descanso si no hay solicitudes
        elif proximo_evento == fin_descanso:
            t = fin_descanso
            if n_solicitudes_actuales == 0:
                fin_descanso = t + generar_descanso()
                descansando = True
                descansos.append((t, fin_descanso - t))

                # El descanso supera el tiempo que el servidor atiende
                if fin_descanso > tiempo_total:
                    fin_descanso = tiempo_total
            else:
                descansando = False
                fin_descanso = tiempo_total
                tiempo_atencion = generar_atencion()
                tiempo_fin_servicio = t + tiempo_atencion

    return (
        cantidad_solicitudes,
        llegada_de_solicitudes,
        cantidad_solicitudes_atendidas,
        tiempo_atencion_de_solicitudes,
        descansos,
        servicios_pendientes
    )
