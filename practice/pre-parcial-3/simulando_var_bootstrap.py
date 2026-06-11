from random import choice


def calular_muestras_bootstrap(lista, cantidad):
    muestras = []
    for _ in range(cantidad):
        muestras.append([choice(lista) for _ in range(len(lista))])
    return muestras


def calcular_media(datos):
    """Calcula la media aritmética (X̄)."""
    return sum(datos) / len(datos)


def calcular_varianza_muestral(datos):
    """Calcula el estadístico S^2 usando el divisor n-1 [3, 4]."""
    n = len(datos)
    media = calcular_media(datos)
    return sum((x - media) ** 2 for x in datos) / (n - 1)


def ejercicio_6b_simulando(n_sim):
    datos_originales = [5, 4, 9, 6, 21, 17, 11, 20, 7, 10, 21, 15, 13, 16, 8]
    n = len(datos_originales)

    # 2. Generar todas las n^n muestras bootstrap
    muestras_bootstrap = calular_muestras_bootstrap(datos_originales, n_sim)

    # 3. Calcular S^2 para cada muestra bootstrap
    replicaciones_s2 = [calcular_varianza_muestral(
        m) for m in muestras_bootstrap]

    # 4. Calcular el promedio de las replicaciones
    media_de_replicaciones = calcular_media(replicaciones_s2)

    # 5. Calcular la Varianza Bootstrap del estimador
    suma_errores_cuadrados = sum(
        (s2 - media_de_replicaciones) ** 2 for s2 in replicaciones_s2
    )

    varianza_bootstrap_final = suma_errores_cuadrados / (n_sim - 1)

    return varianza_bootstrap_final


# Resultado esperado: 1.0
print(
    f"La estimación bootstrap de Var(S^2) es: {ejercicio_6b_simulando(10000)}")
