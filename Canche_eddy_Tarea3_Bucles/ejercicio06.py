# Nombre: eddy maria canche perez
# Grupo: 1er año programacion y webmaster
"""Ejercicio 6: Serie de Fibonacci
Pide cuántos términos de la serie de Fibonacci desea ver y muéstralos en una sola línea,
separados por comas, empezando en 0 y 1. Con 8 términos la salida es 0, 1, 1, 2, 3, 5, 8, 13.
Si pide 0 términos, no imprimas la serie y avisa; si pide 1, imprime solo 0.
Pista: Necesitas dos variables para los dos últimos términos y una temporal para la suma. Imprime el
término actual antes de actualizar los valores; si actualizas primero, pierdes el dato que necesitas para
el siguiente."""

# Pregunto cuántos términos quiere ver el usuario.
terminos = int(input("¿Cuántos términos? "))

# Si pide cero o una cantidad negativa, no hay términos que mostrar.
if terminos <= 0:
    # Aviso que no se puede imprimir una serie con esa cantidad.
    print("No hay términos para mostrar.")
else:
    # Guardo el primer término de Fibonacci.
    primero = 0
    # Guardo el segundo término de Fibonacci.
    segundo = 1
    # Inicio el contador para saber cuántos términos llevo.
    contador = 1

    # Repito hasta imprimir la cantidad de términos solicitada.
    while contador <= terminos:
        # En el primer término no necesito poner una coma antes.
        if contador == 1:
            # Imprimo el término actual sin cambiar de línea.
            print(primero, end="")
        # En los siguientes términos sí separo con una coma.
        else:
            # Imprimo el término actual después de la coma y un espacio.
            print(f", {primero}", end="")
        # Calculo el siguiente término sumando los dos anteriores.
        siguiente = primero + segundo
        # El segundo término pasa a ocupar el lugar del primero.
        primero = segundo
        # La suma calculada queda como el nuevo segundo término.
        segundo = siguiente
        # Aumento el contador porque ya imprimí un término.
        contador = contador + 1

    # Hago un salto de línea al terminar de imprimir la serie.
    print()