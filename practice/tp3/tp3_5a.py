"""tp3-ej5a"""
import random
import math

def g(u):
    """function to integrate in (0,1)"""
    return (1 - u ** 2) ** (1.5)

def monte_carlo(n_sim):
    """estimate integral with Monte Carlo method"""
    summ = 0
    for _ in range(n_sim):
        u = random.random()
        summ += g(u)

    return summ / n_sim

if __name__ == "__main__":
    exact_value = (3 * math.pi) / 16
    print(f"--- VALUE: {exact_value:.6f} ---\n")

    values = [100, 1000, 10000, 100000, 1000000]
    for n in values:
        res = monte_carlo(n)
        error = abs(exact_value - res)
        print(f"Sim length: {n:<8} | Result: {res:.6f} | Error: {error:.6f}")
        