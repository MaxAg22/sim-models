# Ejercicio 2. Se desea construir una aproximación de:
# ...
# a) Escriba un algoritmo para estimar la cantidad deseada.
# b) Obtenga la aproximación sorteando 100 números aleatorios.
# c) Escriba un algoritmo para calcular la suma de los primeros 100 términos, y compare el valor exacto
# con las dos aproximaciones, y el tiempo de cálculo.
from math import exp
from random import random
import time 

def estimacion_a(nsim):
    inicio = time.time()
    sum = 0
    for _ in range(nsim):
        U = int(random() * 10000) + 1
        sum += exp(U/10000)
    fin = time.time()
    return (sum / nsim * 10000, inicio, fin)

def primeros_100():
    inicio = time.time()
    sum = 0
    for index in range(99):
        sum += exp(index+1/10000)
    fin = time.time()
    return (sum, inicio, fin)


result = estimacion_a(100)
print("\n*** Ejercicio 2 ***")
print(f"""N° de sim = 100, 
      Estimación ~ {result[0]}
      Tiempo de ejecución: {result[2] - result[1]} segundos""")

result1 = primeros_100()
print(f"""Suma de los primeros 100: {result1[0]}
      Tiempo de ejecución: {result1[2] - result1[1]} segundos""")
