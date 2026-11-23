# Nombre: eddy maria canche perez
# Grupo: 1er año programacion y webmaster
""" Ejercicio 9: Calculadora con menú repetitivo
Muestra un menú dentro de un ciclo con sumar, restar, multiplicar, dividir y salir. Según la
opción, pide dos números y muestra el resultado. Si elige dividir y el segundo número es 0,
muestra "Error: no se puede dividir entre cero" y no cuentes esa operación. Si elige una opción
que no existe, muestra "Opción no válida". Lleva un contador de operaciones realizadas y
muéstralo al salir.
Pista: Después de cada operación vuelve a mostrar el menú; no lo cierres. Cuenta solo las operaciones
que se completaron: la división entre cero y las opciones inválidas no cuentan."""

# Inicio el contador de operaciones completadas en cero.
operaciones = 0
# Esta variable controla si el menú debe seguir apareciendo.
opcion = 0

# El menú se repite mientras el usuario no elija salir.
while opcion != 5:
    # Muestro las opciones disponibles de la calculadora.
    print("1. Sumar")
    # Muestro la opción para restar.
    print("2. Restar")
    # Muestro la opción para multiplicar.
    print("3. Multiplicar")
    # Muestro la opción para dividir.
    print("4. Dividir")
    # Muestro la opción para terminar el programa.
    print("5. Salir")

    # Pido la opción y la convierto a entero.
    opcion = int(input("Opción: "))

    # Si elige del 1 al 4, necesita escribir dos números.
    if opcion >= 1 and opcion <= 4:
        # Pido el primer número de la operación.
        primero = float(input("Primer número: "))
        # Pido el segundo número de la operación.
        segundo = float(input("Segundo número: "))

        # Si eligió 1, hago una suma.
        if opcion == 1:
            # Calculo la suma de los dos números.
            resultado = primero + segundo
            # Muestro el resultado de la suma.
            print(f"Resultado: {resultado}")
            # Cuento la operación porque sí se realizó.
            operaciones = operaciones + 1

        # Si eligió 2, hago una resta.
        elif opcion == 2:
            # Calculo la resta.
            resultado = primero - segundo
            # Muestro el resultado de la resta.
            print(f"Resultado: {resultado}")
            # Aumento el contador de operaciones realizadas.
            operaciones = operaciones + 1

        # Si eligió 3, hago una multiplicación.
        elif opcion == 3:
            # Calculo la multiplicación.
            resultado = primero * segundo
            # Muestro el resultado de la multiplicación.
            print(f"Resultado: {resultado}")
            # Cuento la operación terminada.
            operaciones = operaciones + 1

        # Si eligió 4, reviso primero que no se divida entre cero.
        elif opcion == 4:
            # Compruebo si el segundo número es cero.
            if segundo == 0:
                # Muestro el error y no aumento el contador.
                print("Error: no se puede dividir entre cero")
            # Si el segundo número no es cero, puedo dividir.
            else:
                # Calculo la división.
                resultado = primero / segundo
                # Muestro el resultado de la división.
                print(f"Resultado: {resultado}")
                # Cuento la división porque se realizó correctamente.
                operaciones = operaciones + 1

    # Si la opción no está entre 1 y 5, no es una opción válida.
    elif opcion != 5:
        # Aviso que la opción no existe.
        print("Opción no válida")

# Cuando el usuario elige 5, el ciclo termina y muestro el total.
print(f"Operaciones realizadas: {operaciones}")