# Nombre: Eddy maria canche perez
# Grupo: PROGRAMACION Y WEBMASTER
""" Ejercicio 2: La pizzería Pide el tamaño de la pizza y la cantidad que desea el cliente. Los precios son:
1 = personal: $99
2 = mediana: $149
3 = familiar: $199
Si el tamaño no está entre 1 y 3, muestra «Tamaño no válido» y no calcules el total. Si el cliente
lleva tres pizzas o más, aplica 10 % de descuento sobre el total. Muestra el total a pagar con
dos decimales.
"""
# solicita el tamaño de la pizza.
tamaño = int(input("Ingresa el tamaño de la pizza (1, 2 o 3): "))

# dolicita la cantidad de pizzas.
cantidad = int(input("Ingresa la cantidad de pizzas: "))

# comprueba si el tamaño es 1.
if tamaño == 1:
    # Asigna el precio de la pizza personal.
    precio = 99

# comprueba si el tamaño es 2.
elif tamaño == 2:
    # Asigna el precio de la pizza mediana.
    precio = 149

# comprueba si el tamaño es 3.
elif tamaño == 3:
    # Asigna el precio de la pizza familiar.
    precio = 199

# si el tamaño no es válido.
else:
    # Muestra el mensaje de error.
    print("Tamaño no válido")
    precio = 0

# comprueba que el tamaño esté entre 1 y 3.
if tamaño >= 1 and tamaño <= 3:

    # Multiplica el precio por la cantidad.
    total = precio * cantidad

    # cumprueba si compra tres pizzas o más.
    if cantidad >= 3:
        # Aplica el descuento del 10%.
        total = total * 0.90

    # muestra el total con dos decimales.
    print("Total a pagar: $", format(total, ".2f"))
