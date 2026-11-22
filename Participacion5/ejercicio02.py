# Ejercicio 2: Suma de pares e impares
"""Recorre los números del 1 al 100. Calcula por separado la suma de los pares, la suma de los
impares y cuántos números hay de cada tipo. Muestra los cuatro resultados con etiquetas
claras.
Pista: numero % 2 == 0 separa pares de impares; verifica que las dos cantidades sumen 100."""

# Inicio las sumas en cero
suma_pares = 0
suma_impares = 0

# Inicio los contadores en cero
cantidad_pares = 0
cantidad_impares = 0

# Recorro los números del 1 al 100
for numero in range(1, 101):

    # Compruebo si el número es par
    if numero % 2 == 0:

        # Sumo el número a los pares
        suma_pares = suma_pares + numero

        # Cuento un número par más
        cantidad_pares = cantidad_pares + 1

    else:

        # Si no es par, lo sumo a los impares
        suma_impares = suma_impares + numero

        # Cuento un número impar más
        cantidad_impares = cantidad_impares + 1

# Muestro la suma de los pares
print(f"Suma de pares: {suma_pares}")

# Muestro la suma de los impares
print(f"Suma de impares: {suma_impares}")

# Muestro cuántos números pares hay
print(f"Cantidad de pares: {cantidad_pares}")

# Muestro cuántos números impares hay
print(f"Cantidad de impares: {cantidad_impares}")