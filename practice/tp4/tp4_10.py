import random

def trans_inv_t1_t2(p1, p2):
    prob1 = p1 * 0.5
    prob2 = p2 * 0.5
    acum = prob1 + prob2
    i = 1
    u = random.random()
    while u >= acum:
        i += 1
        prob1 *= (1-p1)
        prob2 *= (1-p2)
        acum += prob1 + prob2
    return i

def sim_t1_t2(p1, p2, n_sim):
    values = 0
    for _ in range(n_sim):
        v = trans_inv_t1_t2(p1, p2)
        values += v
    return values/n_sim

n = 1000
r = sim_t1_t2(1/2, 1/3, n)
print(f"El valor estimado es {r}")