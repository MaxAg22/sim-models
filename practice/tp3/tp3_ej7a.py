"""tp3-ej7"""
import random as r


def get_variables_number():
    """Returns the number of uniform random variables needed for their sum to exceed 1."""
    summ = 0
    count = 0
    while summ <= 1:
        summ += r.random()
        count += 1

    return count


def get_sim_avg(n_sim):
    """Returns uniform variables avarage needed for their sum to exceed 1."""
    number = 0
    for _ in range(n_sim):
        number += get_variables_number()

    return number/n_sim

values = [100, 1000, 10000, 100000, 1000000]
for n in values:
    res = get_sim_avg(n)
    print(f"avg: {res} sim length: {n}")