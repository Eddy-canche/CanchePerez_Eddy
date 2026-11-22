"""5.5 Palabra al revés y conteo de letras
Pide una palabra. Debes mostrarla letra por letra, una debajo de otra; cuántas letras tiene, sin
usar len(); la palabra invertida, y cuántas veces aparece la letra a.
Con mariposa, la salida debe indicar 8 letras, la palabra invertida asopiram y que la letra a
aparece 2 veces.
Pista: para invertir, acumula cada letra al inicio de la cadena: invertida = letra + invertida."""

# Pido una palabra al usuario
palabra = input("Escribe una palabra: ")

# Inicio el contador de letras en cero
cantidad_letras = 0

# Creo una variable vacía para invertir la palabra
invertida = ""

# Inicio el contador de letras a en cero
cantidad_a = 0

# Recorro cada letra de la palabra
for letra in palabra:

    # Muestro cada letra en una línea
    print(letra)

    # Cuento cada letra que aparece
    cantidad_letras = cantidad_letras + 1

    # Voy colocando las letras al inicio para invertir la palabra
    invertida = letra + invertida

    # Compruebo si la letra es a o A
    if letra == "a" or letra == "A":

        # Aumento el contador de letras a
        cantidad_a = cantidad_a + 1

# Muestro cuántas letras tiene la palabra
print(f"Cantidad de letras: {cantidad_letras}")

# Muestro la palabra invertida
print(f"Palabra invertida: {invertida}")

# Muestro cuántas veces aparece la letra a
print(f"La letra a aparece: {cantidad_a} veces")