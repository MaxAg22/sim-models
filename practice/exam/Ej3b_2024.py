import random as rm
from math import log

def f(x):
    """f function"""
    return 1 / ((x**2) * log(x + 1))

def h(y):
    """h function"""
    return f(1/y)/(y**2)

def monte_carlo(N):
    """monte carlo method"""
    val = 0
    for _ in range(N):
        u = rm.random()
        val += h(u)
    
    return val/N

print("\n*** Ejercicio 3 ***")
for n in [1000, 10000, 100000]:
    print(f"N° de sim = {n}, Integral ~ {monte_carlo(n)}")