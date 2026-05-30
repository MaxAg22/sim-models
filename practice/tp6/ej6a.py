def calcular_media(datos):
    """Calcula la media aritmética (X̄)."""
    return sum(datos) / len(datos)


def calcular_varianza_muestral(datos):
    """Calcula el estadístico S^2 usando el divisor n-1 [3, 4]."""
    n = len(datos)
    if n < 2:
        return 0
    media = calcular_media(datos)
    return sum((x - media)**2 for x in datos) / (n - 1)


def ejercicio_6a_ideal():
    datos_originales = [1, 3]
    n = len(datos_originales)

    # 2. Generar todas las n^n muestras bootstrap
    muestras_bootstrap = [
        [1, 1],
        [3, 3],
        [1, 3],
        [3, 1]
    ]

    # 3. Calcular S^2 para cada muestra bootstrap
    replicaciones_s2 = [calcular_varianza_muestral(
        m) for m in muestras_bootstrap]

    # 4. Calcular el promedio de las replicaciones
    media_de_replicaciones = calcular_media(replicaciones_s2)

    # 5. Calcular la Varianza Bootstrap del estimador
    suma_errores_cuadrados = sum(
        (s2 - media_de_replicaciones)**2 for s2 in replicaciones_s2)

    varianza_bootstrap_final = suma_errores_cuadrados / len(muestras_bootstrap)

    return varianza_bootstrap_final


# Resultado esperado: 1.0
print(f"La estimación bootstrap de Var(S^2) es: {ejercicio_6a_ideal()}")
