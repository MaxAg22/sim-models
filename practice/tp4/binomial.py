import random
import time 

def binomial(n,p):
    prob = (1-p)**n
    const = p / (1-p)
    u = random.random()
    F = prob
    i = 0
    while u >= F:
        prob *= const * (n-i)/(i+1)
        # actualizamos la acumulada
        F += prob
        i += 1
    return i

def sim_binomial(n_sim):
    frecuencia = {}
    frecuencia[0] = 0
    frecuencia[10] = 0
    inicio = time.time()
    for _ in range(n_sim):
        valor = binomial(10, 0.3)
        if valor in frecuencia:
            frecuencia[valor] += 1
        else:
            frecuencia[valor] = 1

    fin = time.time()
    max_key = max(frecuencia, key=frecuencia.get)
    max_key_freq = frecuencia[max_key]

    return (fin - inicio, max_key, max_key_freq, frecuencia[0]/n_sim, frecuencia[10]/n_sim)

n = 10000
tiempo_total, max_value, max_value_freq, freq_0, freq_10 = sim_binomial(n)

print(f"Total de simulaciones: {n}")
print(f"Tiempo total: {tiempo_total:.6f} segundos")
print(f"Tiempo promedio por variable: {(tiempo_total/n):.8f} segundos")
print(f"Valor con más ocurrencias: {max_value} con frecuencia de {max_value_freq}")
print(f"Proporcion de veces del 0: {freq_0}")
print(f"Proporcion de veces del 10: {freq_10}")
