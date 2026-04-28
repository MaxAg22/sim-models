import random 

def g(x):
    return x / ((x**2) - 1)

def integral_monte_carlo(functiong, a, b, Nsim):
    integral = 0
    for _ in range(Nsim):
        integral += functiong(a + (b-a) * random.random())

    return integral*(b-a)/Nsim

if __name__ == "__main__":
    values = [100, 1000, 10000, 100000, 1000000]
    for n in values:
        res = integral_monte_carlo(g, 2, 3, n)
        print(f"Sim length: {n} and result: {res:.4f}")

