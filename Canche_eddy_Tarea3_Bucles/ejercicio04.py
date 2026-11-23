# Nombre: eddy maria canche perez
# Grupo: 1er año programacion y webmaster
""" Ejercicio 4: Suma de los dígitos
Pide un número entero positivo y suma sus dígitos sin convertir el número a texto. Con 4729
debe mostrar 22. Usa el módulo para obtener el último dígito y la división entera para eliminarlo,
hasta que el número llegue a 0. Si el usuario escribe un número negativo, avísale y pide otro.
Pista: Haz una copia del número y trabaja sobre la copia: en cada vuelta suma copia % 10 y luego
reemplázala por copia // 10. El ciclo termina cuando la copia llega a 0."""

# Pido un número entero al usuario.
numero = int(input("Número: "))

# Si el número es negativo, vuelvo a pedirlo hasta que sea válido.
while numero < 0:
    # Aviso que necesito un número positivo o cero.
    print("Escribe un número positivo.")
    # Pido otro número para volver a comprobarlo.
    numero = int(input("Número: "))

# Hago una copia para no modificar el número original.
copia = numero
# Inicio la suma en cero porque todavía no he sumado ningún dígito.
suma = 0

# El ciclo sigue mientras todavía queden dígitos en la copia.
while copia > 0:
    # Obtengo el último dígito usando el residuo de dividir entre 10.
    digito = copia % 10
    # Agrego ese último dígito a la suma.
    suma = suma + digito
    # Quito el último dígito usando división entera.
    copia = copia // 10

# Muestro la suma de todos los dígitos.
print(f"La suma de los dígitos es {suma}")
