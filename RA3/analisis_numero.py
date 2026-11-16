def es_par(numero: int) -> str:
    """
    Verifica si un número es par.
    """
    if numero % 2 == 0:
        return "El número es par."
    else:
        return "El número es impar."

def signo(numero: int) -> str:
    """
    Determina el signo de un número.
    """
    if numero > 0:
        return "El número es positivo."
    elif numero < 0:
        return "El número es negativo."
    else:
        return "El número es cero."

def cuadrado(numero: int) -> int:
    """
    Calcula el cuadrado de un número.
    """
    return numero ** 2

def factorial_iterativo(numero: int) -> int:
    """
    Calcula el factorial de un número de manera iterativa.
    """
    if numero < 0:
        return "El factorial no está definido para números negativos."
    elif numero == 0:
        return 1
    else:
        resultado = 1
        for i in range(1, numero + 1):
            resultado *= i
        return resultado
    

def factorial_recursivo(numero: int) -> int:
    """
    Calcula el factorial de un número de manera recursiva.
    """
    if numero < 0:
        return "El factorial no está definido para números negativos."
    elif numero == 0:
        return 1
    else:
        return numero * factorial_recursivo(numero - 1)

def suma_hasta(numero: int) -> int:
    """
    Calcula la suma de todos los números enteros desde 1 hasta el número dado.
    """
    if numero < 1:
        return "El número debe ser mayor o igual a 1."
    else:
        return sum(range(1, numero + 1))

def menu() -> None:
    """
    Muestra un menú de opciones para el usuario.
    """
    print("Seleccione una opción:")
    print("1. Verificar si un número es par o impar")
    print("2. Determinar el signo de un número")
    print("3. Calcular el cuadrado de un número")
    print("4. Calcular el factorial de un número (iterativo)")
    print("5. Calcular el factorial de un número (recursivo)")
    print("6. Calcular la suma de todos los números hasta un número dado")
    print("7. Salir")

if __name__ == "__main__":
    while True:
        menu()
        opcion = input("Ingrese el número de la opción deseada: ")

        if opcion == "1":
            numero = int(input("Ingrese un número: "))
            print(es_par(numero))
        elif opcion == "2":
            numero = int(input("Ingrese un número: "))
            print(signo(numero))
        elif opcion == "3":
            numero = int(input("Ingrese un número: "))
            print(f"El cuadrado de {numero} es {cuadrado(numero)}.")
        elif opcion == "4":
            numero = int(input("Ingrese un número: "))
            print(f"El factorial de {numero} (iterativo) es {factorial_iterativo(numero)}.")
        elif opcion == "5":
            numero = int(input("Ingrese un número: "))
            print(f"El factorial de {numero} (recursivo) es {factorial_recursivo(numero)}.")
        elif opcion == "6":
            numero = int(input("Ingrese un número: "))
            print(f"La suma de todos los números hasta {numero} es {suma_hasta(numero)}.")
        elif opcion == "7":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Por favor, intente nuevamente.")