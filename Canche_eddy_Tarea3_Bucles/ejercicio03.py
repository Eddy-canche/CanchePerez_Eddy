# Nombre: eddy maria canche perez
# Grupo: 1er año programacion y webmaster
""" Ejercicio 3: Factorial de un número
Pide un número entero positivo y calcula su factorial. Muestra la operación completa y el
resultado: 5! = 1 x 2 x 3 x 4 x 5 = 120. Si el número es negativo, muestra "No existe el factorial
de un número negativo". Define también qué ocurre con 0, cuyo factorial es 1.
Pista: El acumulador del producto empieza en 1; si empieza en 0, todo el resultado se vuelve 0.
Multiplica en cada vuelta desde 1 hasta el número. Con 0 el ciclo no debe ejecutarse y el resultado
queda en 1."""

# Pido un número entero al usuario.
numero = int(input("Número: "))

# Reviso si el número es negativo porque no se calcula su factorial.
if numero < 0:
    # Muestro el mensaje que indica que no existe ese factorial.
    print("No existe el factorial de un número negativo.")
else:
    # Inicio el resultado en 1 para que la multiplicación funcione.
    factorial = 1
    # Inicio el contador en 1 para multiplicar desde el primer número.
    contador = 1
    # Guardo el inicio de la operación que voy a mostrar.
    operacion = "1"

    # Repito mientras el contador no pase del número ingresado.
    while contador <= numero:
        # Multiplico el resultado por el contador actual.
        factorial = factorial * contador
        # Si no es la primera vuelta, agrego el siguiente factor a la operación.
        if contador > 1:
            # Escribo el factor que se acaba de multiplicar.
            operacion = operacion + f" x {contador}"
        # Aumento el contador para avanzar al siguiente número.
        contador = contador + 1

    # Muestro el factorial, la operación completa y el resultado.
    print(f"{numero}! = {operacion} = {factorial}")