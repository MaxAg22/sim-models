from math import exp
import random as rm


def monte_carlo(N):

    g = lambda x: exp(-x + exp(-x))
    h = lambda y: g(4*y - 1) * 4

    val = 0
    for _ in range(N):
        u = rm.random()
        val += h(u)
    
    return val/N

print("\n*** Ejercicio 1 ***")
for n in [1000, 10000, 100000]:
    print(f"N° de sim = {n}, Integral ~ {monte_carlo(n)}")