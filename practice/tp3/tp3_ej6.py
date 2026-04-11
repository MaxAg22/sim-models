"""tp3-ej6"""
import random as r

def pi_value(n_sim):
    count = 0.
    for _ in range(n_sim):
        u = 2 * r.random() - 1
        v = 2 * r.random() - 1
        if u ** 2 + v ** 2 <= 1:
            count += 1
    return 4 * count/n_sim

values = [1000, 10000, 100000]
for n in values:
    pi = pi_value(n)
    print(f"pi: {pi} sim_length: {n}")