import numpy as np
from scipy.stats import chi2, binom

datos = [6, 7, 3, 4, 7, 3, 7, 2, 6, 3, 7, 8, 2, 1, 3, 5, 8, 7]
n = len(datos)

p_est = np.mean(datos) / 8  # estimador de p
# construye las frecs observadas
N = np.array([datos.count(k) for k in range(9)])
# tambièn puede ser: np.bincount(datos, minlength=9)

prob = np.array(
    [binom.pmf(k, 8, p_est) for k in range(9)]
)  # calcula las probs teòricas de la binomial(n, p^)

E = n * prob  # frecuecias esperadas

T = np.sum((N - E) ** 2 / E)  # estadístico (N-np)^2
pvalor = chi2.sf(T, df=7)  # P(χ^2_7 ​≥ T)

print("p estimado =", p_est)
print("T =", T)
print("p-valor =", pvalor)
