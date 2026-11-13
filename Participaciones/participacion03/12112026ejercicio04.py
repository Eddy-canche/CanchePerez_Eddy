# Nombre: Eddy maria canche perez
# Grupo: PROGRAMACION Y WEBMASTER
""" Ejercicio 4: Piedra, papel o tijera Dos jugadores escriben su jugada: piedra, papel o tijera. El programa indica quién gana el
round.
piedra vence a tijera
tijera vence a papel
papel vence a piedra
Si ambos escriben lo mismo, el resultado es «Empate». Si alguna de las dos jugadas no es
piedra, papel o tijera, muestra «Jugada no válida» antes de comparar. Al final imprime uno de
estos mensajes: «Gana el jugador 1», «Gana el jugador 2», «Empate» o «Jugada no válida».
Puedes normalizar lo que escriben los jugadores con lower()."""

# solicita la jugada del jugador 1.
# lower() convierte el texto a minúsculas.
jugador1 = input("Jugador 1, escribe tu jugada: ").lower()

# solicita la jugada del jugador 2.
# lower() también convierte el texto a minúsculas.
jugador2 = input("Jugador 2, escribe tu jugada: ").lower()

# comprueba si alguna jugada no es válida.
if (jugador1 != "piedra" and jugador1 != "papel" and jugador1 != "tijera") or (jugador2 != "piedra" and jugador2 != "papel" and jugador2 != "tijera"):

    # Muestra un mensaje si alguna jugada es incorrecta.
    print("Jugada no válida")

# comprueba si los dos jugadores eligieron lo mismo.
elif jugador1 == jugador2:

    # Si son iguales, muestra empate.
    print("Empate")

# Comprueba las combinaciones en las que gana el jugador 1.
elif (jugador1 == "piedra" and jugador2 == "tijera") or (jugador1 == "tijera" and jugador2 == "papel") or (jugador1 == "papel" and jugador2 == "piedra"):

    # Muestra que gana el jugador 1.
    print("Gana el jugador 1")

# Si no se cumple ninguna condición anterior.
else:

    # Muestra que gana el jugador 2.
    print("Gana el jugador 2")

