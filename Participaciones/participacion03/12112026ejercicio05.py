
# Nombre: Eddy Canche
# Grupo: programacion y webmaster
"""Ejercicio 5: Acceso al sistema Un sistema escolar tiene registrado el usuario «alumno» con la contraseña «python2026». Pide
ambos datos y muestra un mensaje según el caso.
usuario y contraseña correctos: Bienvenido al sistema
usuario correcto y contraseña distinta: Contraseña incorrecta
usuario distinto: Usuario no encontrado
Resuélvelo con condicionales anidados: primero comprueba el usuario y, solo si existe,
comprueba la contraseña."""

# solicita el nombre de usuario.
usuario = input("Ingresa tu usuario: ")

# solicita la contraseña.
contraseña = input("Ingresa tu contraseña: ")

# Comprueba primero si el usuario es correcto.
if usuario == "alumno":

    # si el usuario existe, comprueba la contraseña.
    if contraseña == "python2026":

        # Permite el acceso si ambos datos son correctos.
        print("Bienvenido al sistema")

    # Si la contraseña es incorrecta.
    else:

        # Muestra el mensaje correspondiente.
        print("Contraseña incorrecta")

# Si el usuario no existe.
else:

    # muestra el mensaje de usuario no encontrado.
    print("Usuario no encontrado")
