# Nombre: eddy maria canche perez
# Grupo: 1er año programacion y webmaster
""" Ejercicio 10: Ahorro con interés compuesto
Un depósito de $1000.00 genera un interés del 5% anual. Calcula cuántos años deben pasar
para que el saldo llegue al menos a $2000.00. Cada año actualiza el saldo con saldo = saldo
+ (saldo * 0.05) y muéstralo con dos decimales. Al final indica cuántos años pasaron y el saldo
alcanzado.
Reto: pide al usuario el depósito inicial, la tasa y la meta, y usa esos valores. Valida que la tasa
sea mayor que cero, porque con una tasa de 0% el ciclo nunca termina.
Pista: Compara el saldo con la meta al final de cada año, no antes. Lleva un contador de años que
aumente en cada vuelta y detén el ciclo cuando el saldo alcance la meta."""


# Pido el depósito inicial y lo convierto a decimal.
saldo = float(input("Depósito inicial: "))

# Pido la tasa de interés en porcentaje.
tasa = float(input("Tasa de interés (%): "))

# Pido la cantidad que quiero alcanzar.
meta = float(input("Meta de ahorro: "))

# Valido que el depósito sea mayor que cero.
while saldo <= 0:
    # Aviso que el depósito debe ser positivo.
    print("El depósito debe ser mayor que 0.")
    # Vuelvo a pedir el depósito.
    saldo = float(input("Depósito inicial: "))

# Valido que la tasa sea mayor que cero para que el ahorro pueda crecer.
while tasa <= 0:
    # Aviso que la tasa debe ser positiva.
    print("La tasa debe ser mayor que 0.")
    # Vuelvo a pedir la tasa.
    tasa = float(input("Tasa de interés (%): "))

# Valido que la meta sea mayor que el depósito inicial.
while meta <= saldo:
    # Aviso que la meta debe superar al depósito.
    print("La meta debe ser mayor que el depósito inicial.")
    # Vuelvo a pedir la meta.
    meta = float(input("Meta de ahorro: "))

# Inicio el contador de años en cero.
anios = 0

# Repito mientras el saldo todavía no llegue a la meta.
while saldo < meta:
    # Aumento un año porque comienza un nuevo periodo de interés.
    anios = anios + 1
    # Calculo el interés del año y lo agrego al saldo.
    saldo = saldo + (saldo * (tasa / 100))
    # Muestro el saldo de ese año con dos decimales.
    print(f"Año {anios}: {saldo:.2f}")

# Cuando el ciclo termina, muestro cuántos años pasaron.
print(f"Pasaron {anios} años.")
# Muestro el saldo final que alcanzó la meta.
print(f"Saldo alcanzado: {saldo:.2f}")
