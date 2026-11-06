"""
Diseña un programa que reciba una cantidad total de dulces y un número de niños. 
Debe calcular cuántos dulces le tocan a cada uno de forma equitativa y cuántos dulces s
obran en la caja.
"""
# Solicitar la cantidad total de dulces
dulces = int(input("Ingresa la cantidad de dulces: "))
# soolicitar el numero de niños
niños = int(input("Ingresa el numero de niños: "))
# calcular cuántos dulces recibe cada niño // se utiliza estre ya que es dividion entera,
reparto = dulces // niños
# calcular cuantos dulces sobran % se utilizan para los residuos de la division 
sobrantes = dulces % niños
# mosstrar los dulces que recibe cada niño
print("Cada niño recibe:", reparto)
# mostrar los dulces que sobran
print("Dulces sobrantes:", sobrantes)


"""
Haz un programa que reciba la velocidad de un automóvil y determine 
de forma booleana (True o False) si ha excedido el límite permitido de 90 km/h
"""
# solicitar la velocidad del automóvil
velocidad = float(input("Ingresa la velocidad del automóvil: "))
# comparar si la velocidad supera los 90 km/h
excedio = velocidad > 90
# mostrar el resultado booleano True o False
print("¿Excedió el límite de velocidad?:", excedio)


"""
Crea un programa que convierta una temperatura dada en grados Celsius a grados Fahrenheit.
Muestra en pantalla el resultado de la conversión.
"""
# solicitar la temperatura en grados Celsius
celsius = float(input("Ingresa la temperatura en Celsius: "))
# convertir Celsius a Fahrenheit multiplica la temperatura por 9, divide el resultado entre 5, suma 32 para obtener la temperatura en Fahrenheit.
fahrenheit = (celsius * 9/5) + 32
# mostrar la temperatura convertida
print("Temperatura en Fahrenheit:", fahrenheit)


"""
Pide al usuario la longitud de tres lados. 
Verifica si se pueden formar un triángulo válido evaluando con operadores lógicos, 
que la suma de cualquier par de lados sea mayor que el tercer lado.
"""
# solicitar la longitud del primer lado
lado1 = float(input("Ingresa el primer lado: "))
# dolicitar la longitud del segundo lado
lado2 = float(input("Ingresa el segundo lado: "))
# dolicitar la longitud del tercer lado
lado3 = float(input("Ingresa el tercer lado: "))
# verificar que la suma de dos lados sea mayor que el tercero
triangulo = (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1) and (lado1 > 0) and (lado2 > 0) and (lado3 > 0)
# mostrar si se puede formar un triángulo
print("¿Es un triángulo válido?:", triangulo)

"""
Solicita un número entero y determina si es un múltiplo simultaneo de 3 y de 5 
(Es decir, que al dividirlo entre ambos el residuo sea cero)
"""
# solicitar un número entero
numero = int(input("Ingresa un número entero: "))
# verificar si el residuo entre 3 y 5 es cero
multiplo = (numero % 3 == 0) and (numero % 5 == 0)
# mmostrar el resultado booleano True o False
print("¿Es múltiplo de 3 y 5?:", multiplo)