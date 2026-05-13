from random import random


def tirar_moneda(p):
    u = random()
    if u < p:
        return 1
    return 0


def simular_experimento(p):
    neutro = 100
    i = 1
    results = [neutro]
    while True:
        x = tirar_moneda(p)
        results.append(x)
        if results[i-1] != results[i] and results[i-1] != neutro:
            return len(results) - 1
        i += 1


def estimar_prob(x, p, n_sim):
    count = 0
    for _ in range(n_sim):
        r = simular_experimento(p)
        if r == x:
            count += 1
    return count / n_sim


print(f"P(X = 4) ~ {estimar_prob(4, 1/3, 10000):.4f}")
