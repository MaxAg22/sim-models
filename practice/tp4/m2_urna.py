import random
import time 

def urna(n_sim):
    p = [0.11, 0.14, 0.09, 0.08, 0.12, 0.10, 0.09, 0.07, 0.11, 0.09]
    times_it_ocurs = [int(x * 100) for x in p]
    A = [[i+1] * times_it_ocurs[i] for i in range(len(p))]
    A = sum(A, [])
    print(A)
    k = 100
    resultados = []
    inicio = time.time()
    
    for _ in range(n_sim):
        I = int(random.random()*k)
        resultados.append(A[I])
                
    fin = time.time()
    return fin - inicio

n = 10000
tiempo_total = urna(n)

print(f"Total de simulaciones: {n}")
print(f"Tiempo total: {tiempo_total:.6f} segundos")
print(f"Tiempo promedio por variable: {(tiempo_total/n):.8f} segundos")