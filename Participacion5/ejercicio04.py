# Ejercicio 4: Cajero automático
"""Un cajero parte de un saldo de $5000.00. Muestra un menú dentro de un ciclo con tres
opciones numeradas: 1. consultar saldo, 2. retirar dinero, 3. salir. El menú se repite hasta que
el usuario elija salir.
Si intenta retirar más de lo que hay, muestra "Fondos insuficientes" y no descuentes
nada.
• Si elige una opción que no existe, muestra "Opción no válida".
• Tras un retiro válido, muestra el saldo y no aceptes montos negativos ni de cero."""


# Inicio el cajero con 5000 pesos
saldo = 5000.00

# Inicio la opción en cero
opcion = 0

# Repito el menú hasta que el usuario elija salir
while opcion != 3:

    # Muestro el menú del cajero
    print("\n--- CAJERO AUTOMÁTICO ---")
    print("1. Consultar saldo")
    print("2. Retirar dinero")
    print("3. Salir")

    # Pido que el usuario elija una opción
    opcion = int(input("Elige una opción: "))

    # Si elige 1, puede consultar su saldo
    if opcion == 1:

        # Muestro cuánto dinero tiene
        print(f"Tu saldo es: ${saldo:.2f}")

    # Si elige 2, puede retirar dinero
    elif opcion == 2:

        # Pregunto cuánto dinero quiere retirar
        monto = float(input("¿Cuánto deseas retirar? "))

        # Compruebo que el monto sea mayor que cero
        if monto <= 0:

            # Aviso que la cantidad no es válida
            print("El monto debe ser mayor que cero.")

        # Compruebo si tiene suficiente dinero
        elif monto > saldo:

            # Aviso que no tiene fondos suficientes
            print("Fondos insuficientes")

        else:

            # Descuento el dinero de su saldo
            saldo = saldo - monto

            # Muestro el saldo después del retiro
            print(f"Retiro realizado. Saldo actual: ${saldo:.2f}")

    # Si elige 3, sale del cajero
    elif opcion == 3:

        # Muestro un mensaje de despedida
        print("Gracias por utilizar el cajero.")

    else:

        # Si escribe otra opción, aviso que no existe
        print("Opción no válida")