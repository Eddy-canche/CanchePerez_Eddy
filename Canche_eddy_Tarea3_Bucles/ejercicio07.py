# Nombre: eddy maria canche perez
# Grupo: 1er año programacion y webmaster
""" Ejercicio 7: Pirámide de asteriscos
Pide la altura de una pirámide y dibújala con dos ciclos anidados. Para altura 4, la primera fila
lleva tres espacios y un asterisco, la segunda dos espacios y tres asteriscos, la tercera uno y
cinco, y la última ninguno y siete. Relaciona la cantidad de espacios y asteriscos con el número
de fila y prueba con 1, 4 y 10.
Pista: Para la fila i, que empieza en 1, imprime altura - i espacios y luego 2 * i - 1 asteriscos. Termina
cada fila con un salto de línea y no imprimas espacios de más al final."""

# Pido la altura que tendrá la pirámide.
altura = int(input("Altura: "))

# Compruebo que la altura sea por lo menos de una fila.
while altura < 1:
    # Aviso que la altura no es válida.
    print("La altura debe ser mayor que 0.")
    # Vuelvo a pedir la altura.
    altura = int(input("Altura: "))

# Este ciclo recorre cada fila de la pirámide desde 1 hasta la altura.
for fila in range(1, altura + 1):
    # Calculo cuántos espacios van antes de los asteriscos.
    espacios = altura - fila
    # Calculo cuántos asteriscos debe tener esta fila.
    asteriscos = 2 * fila - 1

    # Este ciclo imprime los espacios de la fila actual.
    for espacio in range(espacios):
        # Imprimo un espacio sin saltar a la siguiente línea.
        print(" ", end="")

    # Este ciclo imprime la cantidad de asteriscos calculada.
    for estrella in range(asteriscos):
        # Imprimo un asterisco sin saltar de línea.
        print("*", end="")

    # Cuando termina la fila, paso a la siguiente línea.
    print()