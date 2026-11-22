# Ejercicio 3: Promedio de un grupo
"""Pregunta cuántos alumnos hay en el grupo y pide la calificación de cada uno, una por una.
Calcula la suma de las calificaciones, el promedio con dos decimales y cuántos alumnos
aprobaron (6 o más) y cuántos reprobaron.
Con 0 alumnos, avisa que no hay calificaciones y termina; no dividas entre cero."""

# Pregunto cuántos alumnos hay
alumnos = int(input("¿Cuántos alumnos hay en el grupo? "))

# Compruebo que haya alumnos
if alumnos <= 0:

    # Aviso que no hay calificaciones
    print("No hay calificaciones.")

else:

    # Inicio la suma en cero
    suma = 0

    # Inicio el contador de aprobados
    aprobados = 0

    # Inicio el contador de reprobados
    reprobados = 0

    # Repito según la cantidad de alumnos
    for numero in range(1, alumnos + 1):

        # Pido la calificación de cada alumno
        calificacion = float(input(f"Escribe la calificación del alumno {numero}: "))

        # Voy sumando las calificaciones
        suma = suma + calificacion

        # Compruebo si el alumno aprobó
        if calificacion >= 6:

            # Aumento el contador de aprobados
            aprobados = aprobados + 1

        else:

            # Aumento el contador de reprobados
            reprobados = reprobados + 1

    # Calculo el promedio del grupo
    promedio = suma / alumnos

    # Muestro la suma de calificaciones
    print(f"Suma de calificaciones: {suma}")

    # Muestro el promedio con dos decimales
    print(f"Promedio del grupo: {promedio:.2f}")

    # Muestro los alumnos aprobados
    print(f"Alumnos aprobados: {aprobados}")

    # Muestro los alumnos reprobados
    print(f"Alumnos reprobados: {reprobados}")