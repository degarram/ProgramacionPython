print("--- REGISTRO DE NOTAS DE ALUMNOS ---")

# Solicitar el número de alumnos con control de excepciones para asegurar que sea un entero válido
while True:
    try:
        total_alumnos = int(input("Introduce el número total de alumnos: "))
        if total_alumnos > 0:
            break
        else:
            print("El número de alumnos debe ser mayor que 0.")
    except ValueError:
        print("Error: Debes introducir un número entero válido.")

# Inicialización de variables (acumulador y contadores)
suma_notas = 0.0  # Acumulador para la nota media
contador_aprobados = 0
contador_suspensos = 0

# Estructura repetitiva (for) para procesar a cada alumno
for alumno_actual in range(1, total_alumnos + 1):
    print(f"\n--- Alumno {alumno_actual} ---")
    
    # Pedir el nombre del alumno
    nombre_alumno = input("Introduce el nombre del alumno: ")

    # Control de excepciones y validación del rango para la nota
    while True:
        try:
            # Solicitar la nota (puede ser decimal)
            nota_alumno = float(input(f"Introduce la nota de {nombre_alumno} (entre 0 y 10): "))
            
            # Condición compuesta: comprobar que esté estrictamente entre 0 y 10
            if 0.0 <= nota_alumno <= 10.0:
                break  # Rompe el bucle si la nota es válida
            else:
                print("Error: La nota debe estar comprendida entre 0 y 10.")
        
        except ValueError:
            # Control específico requerido para letras o texto no numérico
            print("Error: Debes introducir un valor numérico válido (ej. 7.5).")

    # Estructura if-else para determinar aprobado o suspenso
    if nota_alumno >= 5.0:
        print(f"Estado: {nombre_alumno} está APROBADO/A.")
        contador_aprobados += 1  # Incrementa el contador de aprobados
    else:
        print(f"Estado: {nombre_alumno} está SUSPENSO/A.")
        contador_suspensos += 1  # Incrementa el contador de suspensos

    # Acumular la nota para el cálculo posterior de la media
    suma_notas += nota_alumno

# Cálculo de la nota media (evitando división por cero por seguridad)
if total_alumnos > 0:
    nota_media = suma_notas / total_alumnos
else:
    nota_media = 0.0

# Mostrar los resultados finales de forma ordenada
print("\n" + "="*40)
print("       RESULTADOS FINALES DEL GRUPO")
print("="*40)
print(f"Total de alumnos evaluados : {total_alumnos}")
print(f"Nota media de la clase     : {nota_media:.2f}")
print(f"Número total de aprobados  : {contador_aprobados}")
print(f"Número total de suspensos  : {contador_suspensos}")
print("="*40)