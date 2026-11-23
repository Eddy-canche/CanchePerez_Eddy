# Nombre: eddy maria canche perez
# Grupo: 1er año programacion y webmaster
""" Ejercicio 8: Tablas de multiplicar del 1 al 10 
Con dos ciclos anidados, imprime las tablas del 1 al 10. Cada tabla lleva el encabezado ---
Tabla del N ---, sus diez renglones y una línea en blanco antes de la siguiente. No pidas datos
al usuario. Al final indica cuántas multiplicaciones se imprimieron: deben ser 100.
Pista: El ciclo externo recorre las tablas del 1 al 10 y el interno los factores del 1 al 10. Lleva un contador
que aumente con cada multiplicación impresa y muéstralo al final."""

# Inicio un contador para contar todas las multiplicaciones.
total = 0

# Este ciclo externo elige qué tabla se va a imprimir.
for tabla in range(1, 11):
    # Muestro el encabezado de la tabla actual.
    print(f"--- Tabla del {tabla} ---")

    # Este ciclo interno recorre los factores del 1 al 10.
    for factor in range(1, 11):
        # Multiplico la tabla actual por el factor.
        resultado = tabla * factor
        # Muestro la multiplicación y su resultado.
        print(f"{tabla} x {factor} = {resultado}")
        # Aumento el total porque imprimí una multiplicación.
        total = total + 1

    # Dejo una línea en blanco antes de la siguiente tabla.
    print()

# Al terminar los dos ciclos, muestro cuántas operaciones se hicieron.
print(f"Total de multiplicaciones: {total}")