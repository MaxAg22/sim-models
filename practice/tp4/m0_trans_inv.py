import random
import time 

def transformada_inversa(n_sim):
    p = [0.11, 0.14, 0.09, 0.08, 0.12, 0.10, 0.09, 0.07, 0.11, 0.09]
    ordering = [1,4,0,8,5,2,6,9,3,7]
    ordered_p = [p[i] for i in ordering]
    resultados = []
    inicio = time.time()
    
    for _ in range(n_sim):
        U = random.random()
        for i in range(len(p)):
            if U < sum(ordered_p[0:i+1]):
                resultados.append(ordering[i]+1)
                break
                
    fin = time.time()
    return fin - inicio

n = 10000
tiempo_total = transformada_inversa(n)

print(f"Total de simulaciones: {n}")
print(f"Tiempo total: {tiempo_total:.6f} segundos")
print(f"Tiempo promedio por variable: {(tiempo_total/n):.8f} segundos")