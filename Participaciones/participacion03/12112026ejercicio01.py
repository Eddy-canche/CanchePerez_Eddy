
# Nombre: Eddy maria canche perez
# Grupo:PROGRAMACION Y WEBMASTER
""" Ejercicio 1: Pide al usuario el color de un semáforo y muestra la acción que debe realizar el conductor. El
programa debe aceptar el color con mayúsculas o minúsculas, es decir, «Rojo», «rojo» y
«ROJO» son el mismo caso.
rojo: Alto total
amarillo: Precaución, disminuye la velocidad
verde: Puedes avanzar
cualquier otro valor: Color no válido"""

# solicita al usuario el color del semáforo.
color = input("Ingresa el color del semáforo: ")

# comprueba si el color es rojo.
if color == "rojo" or color == "Rojo" or color == "ROJO":
    # Indica que debe detenerse.
    print("Alto total")

# Comprueba si el color es amarillo.
elif color == "amarillo" or color == "Amarillo" or color == "AMARILLO":
    # Indica que debe disminuir la velocidad.
    print("Precaución, disminuye la velocidad")

# Comprueba si el color es verde.
elif color == "verde" or color == "Verde" or color == "VERDE":
    # indica que puede avanzar.
    print("Puedes avanzar")

# si el color no coincide con ninguna opción.
else:
    # muestra un mensaje de error.
    print("Color no válido")
