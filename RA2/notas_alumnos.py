# ENUNCIADO: Crea un programa para registrar las notas de varios alumnos.
# Solicitar el número de alumnos, comprobando que sea un número entero.
while True:
    try:
        num_alumnos = int(input("Ingrese el número de alumnos: "))
    except:
        print("El número de alumnos debe ser un número entero.")
    else:
        break

# Inicialización de las variables globales de todo el grupo de alumnos.
nota_media = 0
aprobados = 0
suspensos = 0

# Pedir el nombre y la nota de cada alumno.
for i in range(num_alumnos):
    nombre = input(f"Ingrese el nombre del alumno {i + 1}: ")
    nota = 0
    while True:
        try:
            nota = float(input(f"Ingrese la nota del alumno {i + 1}: "))
        except ValueError: # Si el tipo de valor de la nota no es float, saltará el error
            print("Debes introducir un número decimal del 0 al 10.")
        else: # Si el tipo es float, continuará con las comprobaciones
            if nota < 0 or nota > 10:
                print("La nota debe estar entre 0 y 10. Intente nuevamente.")
            else:
                nota_media += nota
                break
    # Se comprueba si el alumno ha aprobado o suspendido para poder añadirlo a la estadistica del grupo.
    if nota < 5:
        print(f"El alumno {nombre} ha suspendido con una nota de {nota}.")
        suspensos += 1
    else:
        print(f"El alumno {nombre} ha aprobado con una nota de {nota}.")
        aprobados += 1

# Finalmente se muestran tanto la nota media de los alumnos como el número de alumnos que han aprobado y suspendido.
nota_media /= num_alumnos
print(f"\nLa nota media de los alumnos es: {nota_media}, han aprobado {aprobados} alumnos y han suspendido {suspensos}.")
