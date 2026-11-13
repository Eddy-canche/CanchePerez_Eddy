
# Nombre: Eddy maria canche perez
# Grupo: PROGRAMACION Y WEBMASTER
""" Ejercicio 3: El año bisiesto Pide un año y determina si es bisiesto. Un año es bisiesto si es divisible entre 4, excepto los
que terminan en 00: esos solo son bisiestos si además son divisibles entre 400.
Muestra el resultado con el año incluido, por ejemplo «El año 2024 es bisiesto» o «El año 1900
no es bisiesto». Comprueba tu programa con 2024, 1900 y 2000.
"""
# solicita un año y lo convierte a número entero.
año = int(input("Ingresa un año: "))

# Comprueba si es divisible entre 4 y no entre 100,
# o si es divisible entre 400.
if (año % 4 == 0 and año % 100 != 0) or año % 400 == 0:

    # muestra que el año es bisiesto.
    print("El año", año, "es bisiesto")

# Si no cumple ninguna de las condiciones.
else:

    # muestra que el año no es bisiesto.
    print("El año", año, "no es bisiesto")
