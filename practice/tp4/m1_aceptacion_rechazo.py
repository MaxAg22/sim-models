import random
import time 

def aceptacion_rechazo(n_sim):
    p = [0.11, 0.14, 0.09, 0.08, 0.12, 0.10, 0.09, 0.07, 0.11, 0.09]
    c = 1.4
    q = 0.1
    cq = c * q
    
    resultados = []
    inicio = time.time()
    
    for _ in range(n_sim):
        while True:
            Y = int(random.random() * 10) + 1
            U = random.random()
            if U < p[Y-1] / cq:
                resultados.append(Y)
                break
                
    fin = time.time()
    return fin - inicio

n = 10000
tiempo_total = aceptacion_rechazo(n)

print(f"Total de simulaciones: {n}")
print(f"Tiempo total: {tiempo_total:.6f} segundos")
print(f"Tiempo promedio por variable: {(tiempo_total/n):.8f} segundos")