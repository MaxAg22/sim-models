from random import choice


def estimar_p(n_sim):
    n = 10
    vars = [56, 101, 78, 67, 93, 87, 64, 72, 80, 69]
    count = 0
    for _ in range(n_sim):
        muestra_bootstrap = [choice(vars) for _ in range(n)]
        media_bootstrap = sum(muestra_bootstrap) / n
        if 71.7 < media_bootstrap < 81.7:
            count += 1
    return count / n_sim


res = estimar_p(10000)
print(f"Estimación ~ {res:.4f}")
