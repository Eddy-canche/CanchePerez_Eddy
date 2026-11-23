# Nombre: eddy maria canche perez
# Grupo: 1er año programacion y webmaster
""" Ejercicio 2: Validar una edad
Pide la edad de una persona y no avances hasta recibir un número entre 0 y 120. Si el dato es
incorrecto, muestra el error y vuelve a pedir la edad. Con una edad válida, indica si es menor
de edad (menos de 18), mayor de edad (de 18 a 64) o adulto mayor (65 o más).
Pista: Valida el rango con una condición doble: la edad debe ser 0 o más y 120 o menos. Mientras no
se cumpla, muestra el error y vuelve a pedir el dato. Después clasifica con las tres opciones: menos de
18, de 18 a 64 y 65 o más.
"""

# Pido la edad por primera vez y la convierto a número entero.
edad = int(input("Edad: "))

# Repito la pregunta mientras la edad esté fuera del rango permitido.
while edad < 0 or edad > 120:
    # Aviso que el dato no es correcto.
    print("Edad inválida. Escribe un número entre 0 y 120.")
    # Vuelvo a pedir la edad para revisar el dato nuevo.
    edad = int(input("Edad: "))

# Si la edad es menor que 18, la persona es menor de edad.
if edad < 18:
    # Muestro la clasificación correspondiente.
    print("Menor de edad")
# Si tiene de 18 a 64 años, entra en esta opción.
elif edad <= 64:
    # Muestro que es mayor de edad.
    print("Mayor de edad")
# Si no entró en las opciones anteriores, tiene 65 años o más.
else:
    # Muestro que es adulto mayor.
    print("Adulto mayor")