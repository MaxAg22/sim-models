import sympy as sp

def integral_exacta_sympy(f, a, b):
    """
    Calcula la integral definida exacta de una función f entre a y b.
    """
    x = sp.Symbol('x')
    funcion = f(x)
    resultado = sp.integrate(funcion, (x, a, b))
    
    print(f"Integrando: {funcion} | Límite inferior: {a} | Límite superior: {b}")
    print(f"Resultado simbólico exacto: {resultado}")
    print(f"Valor numérico: {resultado.evalf():.4f}\n")
    
    return resultado

if __name__ == "__main__":
    f = lambda x: x / (x**2 - 1)
    integral_exacta_sympy(f, 2, 3)
