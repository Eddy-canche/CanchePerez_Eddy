# Nombre: eddy maria canche perez
# Grupo: 1er año programacion y webmaster
""" Ejercicio 1: Tabla de multiplicar
Pide un número entero y muestra su tabla de multiplicar del 1 al 10 con el formato 7 x 1 = 7. Al
terminar, pregunta si desea ver otra tabla y repite el proceso mientras la respuesta sea si.
Pista: Guarda la respuesta en una variable y compárala con "si". Para la tabla, usa un contador que
vaya de 1 a 10 y muestra cada renglón con el formato número x contador = resultado.
"""

# Esta variable guarda si quiero seguir haciendo otra tabla.
respuesta = "si"

# Mientras la respuesta sea "si", el programa vuelve a hacer una tabla.
while respuesta == "si":
    # Pido el número que quiero multiplicar y lo convierto a entero.
    numero = int(input("Número: "))

    # Este ciclo recorre los números del 1 al 10.
    for contador in range(1, 11):
        # Multiplico el número por el contador y muestro cada resultado.
        print(f"{numero} x {contador} = {numero * contador}")

    # Pregunto si quiero hacer otra tabla.
    respuesta = input("¿Otra tabla? (si/no): ")