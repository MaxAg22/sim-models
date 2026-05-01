import random
import time 

def trans_inv_mejorada():
    p = [0.11, 0.14, 0.09, 0.08, 0.12, 0.10, 0.09, 0.07, 0.11, 0.09]
    orden_mayor_menor = [1,4,0,8,5,2,6,9,3,7]
    p_nuevo_orden = [p[i] for i in orden_mayor_menor]
    u = random.random()
    acumulada = 0
    for i in range(len(p)):
        acumulada += p_nuevo_orden[i]
        if u < acumulada:
            return orden_mayor_menor[i] + 1


def sim_trans_inv_mejorada(n_sim):
    inicio = time.time()
    for _ in range(n_sim):
        trans_inv_mejorada()
    fin = time.time()
    return fin - inicio


n = 10000
tiempo_total = sim_trans_inv_mejorada(n)
print(f"Total de simulaciones: {n}")
print(f"Tiempo total: {tiempo_total:.6f} segundos")
print(f"Tiempo promedio por variable: {(tiempo_total/n):.8f} segundos")