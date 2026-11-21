"""
Ejercicio 4: factorial iterativo.
"""

def factorial_iterativo(numero: int) -> int:
    """
    Calcula el factorial de un entero no negativo con un bucle for.

    Parametros:
        numero (int): Numero entero cuyo factorial se calcula.

    Retorna:
        int: Factorial de numero. El factorial de cero es 1.

    Errores:
        ValueError: Si numero es negativo.
    """
    if numero < 0:
        raise ValueError("No se puede calcular el factorial de un negativo.")

    resultado = 1
    for valor in range(1, numero + 1):
        resultado *= valor

    return resultado

def main() -> None:
    """
    Solicita un entero y muestra su factorial.

    Parametros:
        Ninguno.

    Retorna:
        None: Gestiona la entrada y salida por consola.
    """
    try:
        numero = int(input("Introduce un numero: "))
    except ValueError:
        print("Error: debes introducir un numero entero.")
        return

    try:
        resultado = factorial_iterativo(numero)
        print(f"El factorial de {numero:d} es {resultado:d}.")
    except ValueError as error:
        print(f"Error: {error}")

if __name__ == "__main__":
    main()
