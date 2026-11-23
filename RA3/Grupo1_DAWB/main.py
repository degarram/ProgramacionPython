# Proyecto: Laboratorio matemático modular
# Autores: Jesus Herrera Bailon y David Garcia Ramirez

# Este archivo tiene el menú y pide los datos al usuario.

import operaciones


def mostrar_menu():
    """Muestra el menú principal."""
    print("\n======= LABORATORIO MATEMÁTICO =======")
    print("1. Área y perímetro de un rectángulo")
    print("2. Comprobar si un número es par")
    print("3. Calcular factorial de forma iterativa")
    print("4. Calcular factorial de forma recursiva")
    print("5. Mostrar historial")
    print("6. Salir")


# ---------- PROGRAMA PRINCIPAL ----------

# Lista donde guardamos todas las operaciones
historial = []

while True:
    mostrar_menu()
    opcion = input("Selecciona una opción: ")

    # Opción 1: rectángulo
    if opcion == "1":
        try:
            base = float(input("Introduce la base: "))
            altura = float(input("Introduce la altura: "))

            if base <= 0 or altura <= 0:
                print("Error: la base y la altura deben ser mayores que cero.")
            else:
                area = operaciones.calcular_area_rectangulo(base, altura)
                perimetro = operaciones.calcular_perimetro_rectangulo(base, altura)
                print(f"Área: {area:.2f}")
                print(f"Perímetro: {perimetro:.2f}")

                descripcion = f"Rectángulo de base {base:.2f} y altura {altura:.2f}: área {area:.2f} y perímetro {perimetro:.2f}"
                operaciones.registrar_resultado(historial, descripcion)
        except ValueError:
            print("Error: debes introducir un valor numérico.")

    # Opción 2: par o impar
    elif opcion == "2":
        try:
            numero = int(input("Introduce un número entero: "))

            if operaciones.es_par(numero):
                texto = f"El número {numero} es par"
            else:
                texto = f"El número {numero} es impar"

            print(texto + ".")
            operaciones.registrar_resultado(historial, texto)
        except ValueError:
            print("Error: debes introducir un valor numérico.")

    # Opción 3: factorial con bucle
    elif opcion == "3":
        try:
            numero = int(input("Introduce un número entero: "))

            if numero < 0:
                print("Error: el factorial no está definido para números negativos.")
            else:
                resultado = operaciones.factorial_iterativo(numero)
                texto = f"Factorial iterativo de {numero}: {resultado}"
                print(texto)
                operaciones.registrar_resultado(historial, texto)
        except ValueError:
            print("Error: debes introducir un valor numérico.")

    # Opción 4: factorial con recursividad
    elif opcion == "4":
        try:
            numero = int(input("Introduce un número entero: "))

            if numero < 0:
                print("Error: el factorial no está definido para números negativos.")
            else:
                resultado = operaciones.factorial_recursivo(numero)
                texto = f"Factorial recursivo de {numero}: {resultado}"
                print(texto)
                operaciones.registrar_resultado(historial, texto)
        except ValueError:
            print("Error: debes introducir un valor numérico.")

    # Opción 5: ver el historial
    elif opcion == "5":
        operaciones.mostrar_historial(historial)

    # Opción 6: salir
    elif opcion == "6":
        print("Programa finalizado.")
        print("Gracias por utilizar el laboratorio matemático.")
        break

    # Cualquier otra cosa
    else:
        print("Opción no válida. Selecciona una opción del 1 al 6.")