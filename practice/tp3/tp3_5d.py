"""tp3-ej5b"""
import random
from math import exp

def g(u):
    """function to integrate in (0,1)"""
    return 2 * exp(-((1/u) - 1)**2) / (u**2)

def monte_carlo(n_sim):
    """estimate integral with Monte Carlo method"""
    summ = 0
    for _ in range(n_sim):
        u = random.random()
        summ += g(u)

    return summ / n_sim

if __name__ == "__main__":
    values = [100, 1000, 10000, 100000, 1000000]
    for n in values:
        res = monte_carlo(n)
        print(f"Sim length: {n} and result: {res:.4f}")

