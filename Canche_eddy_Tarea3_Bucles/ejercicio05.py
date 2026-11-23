# Nombre: eddy maria canche perez
# Grupo: 1er año programacion y webmaster
""" Ejercicio 5: Saber si un número es primo
Pide un número entero mayor que 1 y determina si es primo. Usa una bandera es_primo y
break al encontrar el primer divisor. Muestra si el número es primo o no; cuando no lo sea,
indica cuál fue el primer divisor encontrado. Prueba con 97 (primo) y con 91 (divisible entre 7).
Pista: Busca divisores desde 2 hasta el número anterior. En cuanto encuentres uno, cambia la bandera
y sal del ciclo con break. Al final, la bandera decide el mensaje que se muestra."""

# Pido un número entero al usuario.
numero = int(input("Número: "))

# Pido otro número mientras el valor sea menor o igual que 1.
while numero <= 1:
    # Explico qué tipo de número necesito.
    print("Escribe un número entero mayor que 1.")
    # Vuelvo a pedir el número.
    numero = int(input("Número: "))

# Al principio supongo que el número sí es primo.
es_primo = True
# Esta variable guardará el primer divisor si encuentro uno.
primer_divisor = 0
# Empiezo a probar divisores desde el número 2.
divisor = 2

# Reviso los posibles divisores hasta llegar al número anterior.
while divisor < numero:
    # Compruebo si la división deja residuo cero.
    if numero % divisor == 0:
        # Cambio la bandera porque encontré un divisor.
        es_primo = False
        # Guardo el primer divisor que encontré.
        primer_divisor = divisor
        # Salgo del ciclo porque ya no necesito seguir buscando.
        break
    # Si no fue divisor, pruebo con el siguiente número.
    divisor = divisor + 1

# Si la bandera sigue en verdadero, el número es primo.
if es_primo:
    # Muestro que el número es primo.
    print(f"{numero} es primo.")
# Si la bandera cambió, encontré un divisor.
else:
    # Muestro el número y el primer divisor encontrado.
    print(f"{numero} no es primo. Su primer divisor es {primer_divisor}.")