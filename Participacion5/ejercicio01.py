""" Ejercicio5.1 Control de acceso
Una tienda guarda en una caja fuerte la contraseña python2026. Pide la contraseña al usuario
y sigue preguntando hasta que acierte, con un máximo de tres intentos. Al final muestra
"Acceso concedido" si acertó o "Cuenta bloqueada" si se agotaron los intentos, y en ambos
casos indica cuántos intentos se realizaron.
Pista: necesitas dos condiciones a la vez, contraseña incorrecta y menos de 3 intentos."""


# Guardo la contraseña correcta
contrasena_correcta = "python2026"

# Inicio el contador de intentos en cero
intentos = 0

# Creo una variable para guardar la contraseña
contrasena = ""

# Repito mientras la contraseña sea incorrecta y tenga menos de 3 intentos
while contrasena != contrasena_correcta and intentos < 3:

    # Pido al usuario que escriba la contraseña
    contrasena = input("Escribe la contraseña: ")

    # Aumento un intento cada vez que escribe
    intentos = intentos + 1

# Compruebo si la contraseña es correcta
if contrasena == contrasena_correcta:

    # Muestro que el acceso fue permitido
    print("Acceso concedido")

else:

    # Si se terminan los intentos, bloqueo la cuenta
    print("Cuenta bloqueada")

# Muestro la cantidad de intentos realizados
print(f"Intentos realizados: {intentos}")