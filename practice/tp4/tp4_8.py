from random import random, randint
from math import factorial, exp

def new_var_trans_inv(_lambda, k):
    """método de transformada inversa para una variable X dada con un P especifico"""
    const = 0
    for j in range(k):
        const += ((_lambda ** j) / factorial(j)) * exp(-_lambda)
    i = 0
    prob = exp(-_lambda) / const
    acumulada = prob
    u = random()
    while u >= acumulada:
        i += 1
        prob *= _lambda / i
        acumulada += prob
    return i

def estimar_prob_mayor_2_ti(n_sim):
    """estima la probabilidad de que X sea mayor que 2"""
    count = 0
    for _ in range(n_sim):
        x = new_var_trans_inv(0.7, 10)
        count += 1 if x > 2 else 0
    return count/n_sim


def new_var_acept_rechazo(_lambda, k):
    """método de aceptacion rechazo para una variable X dada con un P especifico"""
    # calculamos la constante
    const = 0
    for j in range(k):
        const += ((_lambda ** j) / factorial(j)) * exp(-_lambda)
    q = 1 / (k+1)
    # el c esta dado por el maximo del numerador ya que el denominador es constante
    c = (k+1) * (int(_lambda) + 1)
    cq = c*q

    while True:
        y = randint(0,10)
        u = random()
        # calculamos P(X = y)
        prob = ((_lambda**y) * (exp(-_lambda))) / (factorial(y) * const)
        if u < prob / cq:
            return y
        

def estimar_prob_mayor_2_ar(n_sim):
    """estima la probabilidad de que X sea mayor que 2"""
    count = 0
    for _ in range(n_sim):
        x = new_var_acept_rechazo(0.7, 10)
        count += 1 if x > 2 else 0
    return count/n_sim


n = 1000
result = estimar_prob_mayor_2_ti(n)
result1 = estimar_prob_mayor_2_ar(n)
print("\n*** Ejercicio 8 ***")
print("N° de sim = 1000")
print(f"""Estimación P(X > 2) con TI ~ {result}""")
print(f"""Estimación P(X > 2) con AR ~ {result1}""")



