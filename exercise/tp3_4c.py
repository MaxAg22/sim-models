"""tp3-ej4c"""
import random
from numpy.random import exponential

rates = [1/3, 1/4, 1/5]

def get_rate(x):
    """get the correct rate index"""
    if x <= 0.4:
        return 0
    return 1 if x <= 0.4 + 0.32 else 2

def simulate_queue(n_sim):
    """simulates queue selection"""
    count = 0
    for _ in range(n_sim):
        u = random.random()
        rate = rates[get_rate(u)]
        e = exponential(1/rate)

        if e <= 4:
            count += 1

    return count / n_sim

if __name__ == "__main__": 
    sim_len = 1000
    prob = simulate_queue(sim_len)
    print(f"Simulation result: {prob}")
