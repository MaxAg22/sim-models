import random
import time 

def urna():
    p = [0.11, 0.14, 0.09, 0.08, 0.12, 0.10, 0.09, 0.07, 0.11, 0.09]
    times_it_ocurs = [int(x * 100) for x in p] # lista [11, 14, 9, 8, 12, 10, 9, 7, 11, 9]
    A = [[i+1] * times_it_ocurs[i] for i in range(len(p))] # [[1], [1], ..., [1] (11 veces) y asi..]
    A = sum(A, []) # un join medio raro entre listas queda como [1,1,1,(11 veces) y asi..]
    k = 100 # k puede variar, si tengo un p = 0.001 necesito que k sea 1000
    I = int(random.random()*k)
    return A[I]

def sim_urna(n_sim):
    inicio = time.time()
    for _ in range(n_sim):
        urna() # no necesito el valor
    fin = time.time()
    return fin - inicio

n = 10000
tiempo_total = sim_urna(n)

print(f"Total de simulaciones: {n}")
print(f"Tiempo total: {tiempo_total:.6f} segundos")
print(f"Tiempo promedio por variable: {(tiempo_total/n):.8f} segundos")